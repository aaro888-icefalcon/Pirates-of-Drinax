#!/usr/bin/env python3
"""
bridge.py — discover / validate / summarize a companion bridge.

A bridge is a folder with a bridge.md manifest (containing a fenced ```json block)
that declares which engine hooks the companion overrides and where its files are.
The engine reads the manifest at load and uses an override where present, else the
Mythic/AC default.

Commands:
  summary  <bridge_dir>    Print overrides-vs-defaults for the 9 hooks (names only)
  brief    <bridge_dir>    Print each overridden hook's OPERATIVE DIGEST (the imperative, not just
                           the name) — run at boot so the discipline is LOADED, not merely pointed at
  validate <bridge_dir>    Check the manifest + declared files exist; roll-test tables; lint digests
  manifest <bridge_dir>    Print the parsed JSON manifest
"""
import json, os, re, sys, glob

HOOKS = ["resolve","generate:character","generate:element","meaning","chaos",
         "themes","world-tick","seeds","adventure-ingest"]

# Which manifest 'files' key carries each hook's operative digest.
HOOK_FILE = {"resolve":"system_profile", "meaning":"interpretation", "chaos":"chaos",
             "themes":"themes", "world-tick":"subsystems", "seeds":"seeds",
             "generate:character":"generators", "generate:element":"generators",
             "adventure-ingest":"adventures"}

def extract_digest(path):
    """Pull the '> **Operative digest:** …' blockquote out of a bridge file (the 2-4 imperative
    lines a companion author writes per hook). Returns the text, or None if absent."""
    if not path or not os.path.exists(path): return None
    out, grab = [], False
    for ln in open(path, encoding="utf-8"):
        s = ln.rstrip("\n").strip()
        if not grab:
            if s.startswith(">") and "operative digest" in s.lower():
                grab = True
                seg = re.sub(r"^>\s*\*\*operative digest:?\*\*\s*:?\s*", "", s, flags=re.I).strip()
                if seg: out.append(seg)
        else:
            if s.startswith(">"): out.append(s.lstrip(">").strip())
            else: break
    return "\n".join(x for x in out if x) or None

def read_manifest(bdir):
    p = os.path.join(bdir, "bridge.md")
    if not os.path.exists(p): sys.exit(f"No bridge.md in {bdir}")
    txt = open(p, encoding="utf-8").read()
    m = re.search(r"```json\s*(\{.*?\})\s*```", txt, re.DOTALL)
    if not m: sys.exit("bridge.md has no ```json manifest block")
    try: return json.loads(m.group(1))
    except Exception as e: sys.exit(f"manifest JSON error: {e}")

def _manifest_safe(bdir):
    """read_manifest without exiting — returns {} when there's no usable bridge."""
    try: return read_manifest(bdir)
    except SystemExit: return {}

def char_gen(bdir):
    """Resolve the companion's NEW-character generation override, or None for the engine
    default (AC Character Crafter). Reads manifest.generators_map.character:
      {"mode": "replace"|"conjunction"|"default", "table": "generators/x.json", "note": "<lore>"}
    'replace' uses the companion generator INSTEAD of the AC Crafter; 'conjunction' uses BOTH;
    a bare note (no table) = lore-based generation the GM performs from setting-canon. Table
    paths are returned absolute. Only honored when 'generate:character' is in overrides."""
    if not bdir: return None
    man = _manifest_safe(bdir)
    if not man: return None
    gm = (man.get("generators_map") or {}).get("character")
    if not gm or "generate:character" not in man.get("overrides", []): return None
    out = dict(gm); out.setdefault("mode", "conjunction")
    if out.get("table"): out["table"] = os.path.join(bdir, out["table"])
    return out

def cmd_summary(bdir):
    man = read_manifest(bdir); ov = set(man.get("overrides", []))
    print(f"Companion: {man.get('companion','?')}   engine: {man.get('engine','?')}")
    for h in HOOKS:
        hit = h in ov or any(o.startswith("generate:") for o in ov) if h.startswith("generate:") else h in ov
        print(f"  {'OVERRIDE' if h in ov else 'default ':8}  {h}")

def cmd_brief(bdir):
    """Boot-time load: print the OPERATIVE DIGEST of every overridden hook, not just its name."""
    man = read_manifest(bdir); ov = man.get("overrides", []); files = man.get("files", {})
    print(f"Companion: {man.get('companion','?')}   engine: {man.get('engine','?')}")
    print("OPERATIVE DIGESTS (read before play — the imperatives behind each override, loaded not pointed-at):\n")
    shown = total = 0
    for h in HOOKS:
        if h not in ov: continue
        total += 1
        rel = files.get(HOOK_FILE.get(h, ""))
        dig = extract_digest(os.path.join(bdir, rel)) if rel else None
        print(f"▸ {h}  ({rel or '—'})")
        if dig:
            for line in dig.splitlines(): print(f"    {line}")
            shown += 1
        else:
            print(f"    (no Operative digest — add '> **Operative digest:** …' to {rel or 'the hook file'})")
        print()
    cg = (man.get("generators_map") or {}).get("character")
    if cg:
        print(f"▸ generate:character → mode={cg.get('mode','conjunction')}  table={cg.get('table','—')}")
        if cg.get("note"): print(f"    {cg['note']}")
        print()
    print(f"({shown}/{total} overridden hooks surfaced a digest)")

def cmd_validate(bdir):
    man = read_manifest(bdir); problems = []; warnings = []
    for key, rel in man.get("files", {}).items():
        if not os.path.exists(os.path.join(bdir, rel)):
            problems.append(f"missing file '{rel}' (declared as {key})")
    for h in man.get("overrides", []):
        if h not in HOOKS and not h.startswith("generate:"):
            problems.append(f"unknown hook '{h}'")
    # roll-test any generator tables
    tested = 0
    for f in glob.glob(os.path.join(bdir, "generators", "*.json")):
        try:
            t = json.load(open(f))
            if t.get("type","").startswith("list_"):
                cov = sum(e["max"]-e["min"]+1 for e in t["entries"])
                need = 100 if t["type"]=="list_d100" else 10
                if cov != need: problems.append(f"{os.path.basename(f)}: coverage {cov}/{need}")
                tested += 1
        except Exception as e:
            problems.append(f"{os.path.basename(f)}: {e}")
    # enforcement lint: every overridden hook should surface an Operative digest so boot can LOAD it
    warned = set()
    for h in man.get("overrides", []):
        rel = man.get("files", {}).get(HOOK_FILE.get(h, ""))
        if not rel or rel in warned: continue
        if not extract_digest(os.path.join(bdir, rel)):
            warned.add(rel)
            warnings.append(f"{rel}: no '**Operative digest:**' block — `brief` can't surface its imperative at boot")
    if problems:
        print("INVALID:"); [print("  X", p) for p in problems]; sys.exit(1)
    print(f"Bridge valid ✓  ({len(man.get('overrides',[]))} overrides, {tested} generator tables roll-tested)")
    for w in warnings: print("  ⚠ enforcement:", w)

def cmd_manifest(bdir):
    print(json.dumps(read_manifest(bdir), indent=2))

def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h","--help"): print(__doc__); return
    if len(a) < 2: sys.exit("Need a bridge directory.")
    {"summary":cmd_summary,"brief":cmd_brief,"validate":cmd_validate,"manifest":cmd_manifest}.get(
        a[0], lambda d: sys.exit(f"Unknown command '{a[0]}'"))(a[1])

if __name__ == "__main__":
    main()
