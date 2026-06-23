# Bridge manifest — Pirates of Drinax

Companion bridge for the **mythic-gm** engine. Supplies the **Mongoose Traveller 2e** ruleset (task resolution,
personal & space combat, NPC/ship statting), the **Trojan Reach** setting (ground-truth canon + the powers' wants and
GM lens), the **piracy & empire-building** subsystems and doom clocks, Reach-specific generators, and the full set
campaign ingested as pure-sandbox clusters. The engine still rolls every die, runs the scene/Chaos/Fate/Turning-Point
loop, and holds the no-softening discipline; this bridge only fills the engine's hooks. Validate with
`python3 ../../mythic-gm/scripts/bridge.py validate .` and summarize with `... summary .`.

```json
{
  "companion": "Pirates of Drinax",
  "engine": "mythic-gm>=2",
  "overrides": ["resolve","meaning","chaos","themes","generate:character","generate:element","world-tick","seeds","adventure-ingest"],
  "files": {
    "system_profile": "system-profile.md",
    "interpretation": "interpretation.md",
    "chaos": "chaos-tendency.md",
    "themes": "theme-weights.md",
    "generators": "generators/registry.md",
    "subsystems": "subsystems.md",
    "seeds": "seeds.md",
    "canon": "setting-canon.md",
    "adventures": "adventures/pirates-of-drinax.md"
  }
}
```

## Hooks NOT overridden (engine defaults apply)
- None of the engine's core machinery is touched — scenes, the Scene Test, Chaos math, Fate Questions, Random Events,
  Turning Points, the Lists, and the discipline stay the engine's. `generate:location` / `generate:faction` fall through
  to canon + Fate Questions (see `generators/registry.md`), not a blanket table override.

## Live play state (not part of the bridge)
The in-progress game lives in the repo's `campaign/` folder (`campaign-state.md` is the source of truth, plus the PoD
trackers: `reputation-tracker.md`, `harrier-ship-log.md`, `sector-map.md`, `story-so-far.md`, `character-sheet-*.md`).
The bridge is fixed reference shared across campaigns; `campaign/` is what changes as you play.
