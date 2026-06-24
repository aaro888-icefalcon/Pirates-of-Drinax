#!/usr/bin/env python3
"""
tick.py — world-tick dispatcher (hook: world-tick). At bookkeeping, reads the
companion's subsystems.md registry and reports which subsystems are DUE this scene
and how to advance them (the engine then rolls the named tables honestly).

Usage:
  python3 scripts/tick.py --bridge <bridge_dir> --campaign <campaign_dir>
        preferred — reads the scene # from the campaign's adventure.json
  python3 scripts/tick.py <bridge_dir> <scene_number>            (legacy positional)
  python3 scripts/tick.py <bridge_dir> --campaign <campaign_dir> (mixed: positional bridge)

A subsystem row is:  | name | cadence | advance by |
cadence: 'every scene' | 'every N scenes' | 'on trigger: …'

RUN THIS EVERY BOOKKEEPING STEP. When nothing is due it still prints
'(nothing due this scene)' — so the tick's *absence* is conspicuous, not silent.
"""
import os, re, sys

def run_tick(bdir, scene):
    p = os.path.join(bdir, "subsystems.md")
    print(f"🌍 WORLD TICK — scene {scene}")
    if not os.path.exists(p):
        print("   No subsystems.md — only Mythic's default offscreen-clock advance applies."); return
    due = []
    for ln in open(p, encoding="utf-8"):
        if not ln.strip().startswith("|"): continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[0].lower() in ("subsystem", "name", "") or set(cells[0]) <= set("-"):
            continue
        name, cadence, advance = cells[0], cells[1].lower(), cells[2]
        fire = False
        if "every scene" in cadence:
            fire = True
        else:
            m = re.search(r"every\s+(\d+)", cadence)
            if m and scene and scene % int(m.group(1)) == 0:
                fire = True
            elif "trigger" in cadence:
                fire = None  # conditional — surface for the GM to judge
        if fire is True:
            due.append((name, advance, "DUE"))
        elif fire is None:
            due.append((name, advance, "check trigger"))
    if not due:
        print("   (nothing due this scene)")
    for name, advance, status in due:
        print(f"   • [{status}] {name} → {advance}")
    if due:
        print("   → advance each by rolling its named table (dice.py table <path>) / ticking its clock; record to state.")

def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__); return
    def opt(f): return a[a.index(f) + 1] if (f in a and a.index(f) + 1 < len(a)) else None
    camp = opt("--campaign"); brg = opt("--bridge")
    flagvals = {v for v in (camp, brg) if v}
    pos = [x for x in a if not x.startswith("--") and x not in flagvals]
    bdir = brg or (pos[0] if pos else None)
    if not bdir:
        sys.exit("Need a bridge dir: --bridge <dir> or positional <bridge> <scene#>.")
    if camp:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import lists
        scene = int(lists.load_adventure(camp).get("scene", 0))
    elif len(pos) >= 2:
        scene = int(pos[1])
    else:
        sys.exit("Need a scene #: pass --campaign <dir> (read from adventure.json) or positional <bridge> <scene#>.")
    run_tick(bdir, scene)

if __name__ == "__main__":
    main()
