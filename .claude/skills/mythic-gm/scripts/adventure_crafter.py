#!/usr/bin/env python3
"""
adventure_crafter.py — Adventure Crafter generation for the Mythic loop. All dice
honest; Plot Point titles, structure (Conclusion / None / Meta) and the Meta Plot
Points Table are hard-coded. Threads/Characters are read from the campaign's JSON
Lists (lists.py) so rolls cover the FULL list, however long.

Commands:
  themes [--style action|horror|mystery|intrigue|drama|balanced] [--campaign DIR] [--bridge DIR]
        Roll the adventure's 5 Theme priorities (1st..5th). With --bridge, weights come from the
        companion's theme-weights.md (+ optional first_priority); else from the built-in RPG style.
        With --campaign, save them to adventure.json (theme_order).
  theme [--style ...]                Roll a single Theme (style-weighted)
  turning-point [--campaign DIR] [--bridge DIR] [--existing] [--themes A,B,..] [--tens T] [--threads N]
        Generate a Turning Point: roll the Thread (two-stage on threads.json), then
        ALWAYS roll five Plot Points (≤3 'None', a 4th None rerolled). Conclusion (1-8)
        on any roll if --existing. 96-100 rolls the Meta Plot Points Table.
        Plot Points that call for a Character are flagged «invokes a Character» and, with
        --campaign, auto-invoke the Characters List (a NEW result generates one; --bridge
        applies the companion's character generator). A Meta Thread Combo invokes Threads ×2.
        With --campaign, theme order + the Tens-cycle counter are read from / written to
        adventure.json (no need to pass --themes/--tens by hand).
"""
import json, os, random, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lists

DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
def load(name): return json.load(open(os.path.join(DATA, name), encoding="utf-8"))
def d(n): return random.randint(1, n)
def entry_at(entries, r):
    for e in entries:
        if e["min"] <= r <= e["max"]: return e
    return {}
def lookup(entries, r): return entry_at(entries, r).get("value")
def _oracle():
    import oracle; return oracle              # lazy sibling import (for auto-invoking the Lists)

THEME_TBL = load("adventure_crafter/plot_point_theme.json")
THEMES_DEF = load("adventure_crafter/themes.json")
STRUCT = load("adventure_crafter/plot_point_structure.json")["universal"]
META_TBL = load("adventure_crafter/meta_plot_points.json")

def weighted_order(weights):
    """Draw a priority order by weight (higher weight → likelier earlier). Zero-weight themes still
    appear, at the end, so all themes are always present in the 5-priority order."""
    order = []
    pool = [(t, wt) for t, wt in weights.items() if wt > 0]
    zeros = [t for t, wt in weights.items() if wt <= 0]
    while pool:
        total = sum(x[1] for x in pool); r = random.uniform(0, total); acc = 0
        for i, (t, wt) in enumerate(pool):
            acc += wt
            if r <= acc:
                order.append(t); pool.pop(i); break
    order.extend(zeros)
    return order

def weighted_theme_order(style):
    return weighted_order(dict(THEMES_DEF["style_weights"].get(style, THEMES_DEF["style_weights"]["balanced"])))

def parse_bridge_theme_weights(bridge_dir):
    """Read a companion bridge's theme-weights.md → ({theme: weight}, first_priority|None), or
    (None, None) if absent. Ignores # comments and > blockquotes (e.g. the Operative digest)."""
    if not bridge_dir: return None, None
    p = os.path.join(bridge_dir, "theme-weights.md")
    if not os.path.exists(p): return None, None
    names = {n.lower(): n for n in THEMES_DEF["themes"]}
    weights = {}; first = None
    for ln in open(p, encoding="utf-8"):
        s = ln.strip()
        if not s or s.startswith("#") or s.startswith(">"): continue
        m = re.match(r"([A-Za-z]+)\s*:\s*(\d+)\s*$", s)
        if m and m.group(1).lower() in names:
            weights[names[m.group(1).lower()]] = int(m.group(2)); continue
        fm = re.match(r"first_priority\s*:\s*([A-Za-z]+)", s)
        if fm and fm.group(1).lower() != "none" and fm.group(1).lower() in names:
            first = names[fm.group(1).lower()]
    if not weights: return None, None
    for n in THEMES_DEF["themes"]: weights.setdefault(n, 1)   # ensure all 5 themes appear
    return weights, first

def cmd_themes(style, campaign=None, bridge_dir=None):
    bw, first = parse_bridge_theme_weights(bridge_dir)
    if bw:
        order = weighted_order(bw)
        if first and first in order:
            order.remove(first); order.insert(0, first)
        src = "bridge:theme-weights.md (" + ", ".join(f"{t} {bw[t]}" for t in THEMES_DEF["themes"]) \
              + (f"; first_priority={first}" if first else "") + ")"
        used_style = "bridge"
    else:
        order = weighted_theme_order(style); src = f"style:{style}"; used_style = style
    print(f"🎭 ADVENTURE THEMES ({src}) — priority order:")
    for i, t in enumerate(order, 1):
        print(f"   {i}. {t}")
    if campaign:
        adv = lists.load_adventure(campaign); adv["theme_order"] = order; adv["style"] = used_style
        lists.save_adventure(campaign, adv)
        print(f"   ✔ saved to {os.path.join(campaign,'adventure.json')} (theme_order).")
    print("   [src ac.themes; bridge-weighted if a companion theme-weights.md is present, else style-weighted]")

def cmd_theme(style):
    order = weighted_theme_order(style); print(f"🎭 Theme (style {style}): {order[0]}")

def roll_thread(campaign, n_fallback):
    """Two-stage Thread roll on threads.json (covers the full list, any length).
    Falls back to a legacy count-based 1d100→line when no campaign JSON is given."""
    if campaign:
        obj = lists.load_list(campaign, "thread")
        res = lists.two_stage(obj["entries"], "thread")
        return "Thread — " + lists.describe(res, "thread")
    if n_fallback <= 0: return "Thread — Threads List empty → automatic NEW THREAD"
    r = d(100); line = (r - 1)//4 + 1
    if line <= n_fallback:
        return f"Thread — 1d100={r} → line {line} (≤{n_fallback}) → INVOKE existing Thread on line {line}"
    default = "NEW THREAD" if line in lists.THREAD_NEW_LINES else "CHOOSE MOST LOGICAL THREAD"
    return f"Thread — 1d100={r} → line {line} (blank) → {default}"

PRIORITY_IDX = {"First Priority":0, "Second Priority":1, "Third Priority":2}
def plot_point(theme, existing):
    """Roll 1d100 on the per-theme Plot Point table; apply structure.
    Returns (roll, value, is_none, is_conclusion, invoke). invoke ∈ {None,'character','thread2'}
    flags a Plot Point that calls for the Characters List (most) or, for a Meta Thread Combo,
    two Thread invokes. 1-8 = Conclusion (existing) / None (new); 9-24 = None; 96-100 = Meta."""
    t = load(f"adventure_crafter/plot_points_{theme.lower()}.json")
    pp = d(100)
    if pp <= 8:
        if existing: return pp, "** CONCLUSION ** (this Turning Point ends the Thread)", False, True, None
        return pp, "None (Conclusion can't apply to a New Thread)", True, False, None
    if pp <= 24: return pp, "None (empty slot)", True, False, None
    if pp >= 96:
        mr = d(100); me = entry_at(META_TBL["entries"], mr)
        invoke = "character" if me.get("char") else ("thread2" if me.get("thread2") else None)
        return pp, f"META PLOT POINT → 1d100={mr} → **{me.get('value')}** ({me.get('effect','')})", False, False, invoke
    e = entry_at(t["entries"], pp)
    return pp, e.get("value"), False, False, ("character" if e.get("char") else None)

def _do_invoke(invoke, campaign, bridge):
    """Resolve a Plot Point's Character (or Thread Combo) invoke. With a campaign it rolls the
    Lists now (auto-generating a NEW Character); otherwise it prints the command to run."""
    if invoke == "character":
        print("       ↳ this Plot Point INVOKES A CHARACTER:")
        if campaign:
            _oracle().invoke_two_stage("character", campaign, bridge_dir=bridge)
        else:
            print("          → oracle.py character-list --campaign <dir>   (a NEW result auto-generates one)")
    elif invoke == "thread2":
        print("       ↳ THREAD COMBO — invoke the Threads List TWICE and merge the two Threads:")
        if campaign:
            _oracle().invoke_two_stage("thread", campaign); _oracle().invoke_two_stage("thread", campaign)
        else:
            print("          → oracle.py thread-list --campaign <dir>   (run twice)")

def gen_turning_point(campaign, existing, order, tens, n_fallback, bridge=None):
    print("════════ ADVENTURE CRAFTER — TURNING POINT ════════")
    print(f"Theme priority: {', '.join(order)}   |   Thread: {'Advancement (existing)' if existing else 'New'}")
    print(roll_thread(campaign, n_fallback))
    print("\nRolling FIVE Plot Points (always 5; ≤3 may be 'None', a 4th None is rerolled):")
    kept = 0; none_count = 0; concluded = False; char_count = 0
    pending = []                                      # (invoke,) to resolve after the five are listed
    while kept < 5:
        tr = d(10)
        if tr == 10:                                  # Fourth/Fifth — staggered by count of 10s, spans Turning Points
            ptens = tens + 1; idx = 3 if ptens % 2 == 1 else 4
            plabel = f"Fourth/Fifth (10 #{ptens} → {'Fourth' if idx == 3 else 'Fifth'})"
        else:
            prio = lookup(THEME_TBL["entries"], tr); idx = PRIORITY_IDX[prio]; plabel = prio
        theme = order[idx % len(order)]
        pp, val, is_none, is_concl, invoke = plot_point(theme, existing)
        if is_none and none_count >= 3:               # 4th None → disregard and reroll this slot
            print(f"   (4th 'None' [{theme} {pp}] — disregarded, rerolling)")
            continue                                  # do NOT commit the tens cycle for a disregarded roll
        if tr == 10: tens += 1
        if is_none: none_count += 1
        if is_concl: concluded = True
        kept += 1
        tag = "  «invokes a Character»" if invoke == "character" else ("  «Thread Combo»" if invoke == "thread2" else "")
        print(f"  Plot Point {kept}: 1d10={tr} ({plabel} → {theme}); 1d100={pp} → {val}{tag}")
        if invoke:
            pending.append(invoke)
            if invoke == "character": char_count += 1
    print(f"\n→ {5 - none_count} Plot Point(s), {none_count} None"
          f"{(' · ' + str(char_count) + ' invoke a Character') if char_count else ''}"
          f"{' · the THREAD CONCLUDES this Turning Point' if concluded else ''}")
    if pending:
        print("\nResolving the Plot Points that call for the Lists:")
        for invoke in pending: _do_invoke(invoke, campaign, bridge)
    if campaign:
        adv = lists.load_adventure(campaign); adv["tens"] = tens; lists.save_adventure(campaign, adv)
        print(f"\n   ✔ Tens-cycle counter = {tens} saved to adventure.json.")
    else:
        print(f"\n   Tens-cycle counter now {tens} — pass back as --tens {tens} next Turning Point.")
    print("↳ Record Invoked/added Threads & Characters:  state.py thread|char add <campaign> \"<name>\"")
    print("[src ac.plot_points.<theme> (char-tagged) + structure + meta — fully hard-coded]")

def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h","--help"): print(__doc__); return
    def opt(f, dv): return type(dv)(a[a.index(f)+1]) if f in a else dv
    style = opt("--style", "balanced")
    campaign = opt("--campaign", "") or None
    bridge = opt("--bridge", "") or None
    if a[0] == "themes": cmd_themes(style, campaign, bridge)
    elif a[0] == "theme": cmd_theme(style)
    elif a[0] == "turning-point":
        if "--themes" in a:
            order = a[a.index("--themes")+1].split(",")
        elif campaign:
            order = lists.load_adventure(campaign)["theme_order"]
        else:
            bw, first = parse_bridge_theme_weights(bridge)
            if bw:
                order = weighted_order(bw)
                if first and first in order: order.remove(first); order.insert(0, first)
            else:
                order = THEMES_DEF["themes"]
        tens = opt("--tens", -1)
        if tens < 0:
            tens = lists.load_adventure(campaign)["tens"] if campaign else 0
        gen_turning_point(campaign, "--existing" in a,
                          [t.strip().capitalize() for t in order], tens, opt("--threads", 0), bridge)
    else: sys.exit(f"Unknown command '{a[0]}'. See --help.")

if __name__ == "__main__":
    main()
