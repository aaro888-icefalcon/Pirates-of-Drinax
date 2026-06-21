# Campaign folder — your live game lives here

This is the **campaign folder** that both skills read and write. It is the
single source of truth for an in-progress game; everything in
`.claude/skills/` is fixed reference material, but the files here change as
you play.

## What ends up in this folder

When you start a game, the GM (Claude, running the skills) creates these here:

| File | What it is | Created during |
|---|---|---|
| `campaign-state.md` | **The source of truth.** Chaos Factor, Threads/Characters Lists, crew, the Harrier, finances, reputation, sandbox clocks, last-scene recap. Overwritten every scene. | Session Zero (template: `pod-campaign-state.md`) |
| `system-profile.md` | The Traveller 2e task/combat seam the engine routes rolls through. | Session Zero (copied from the PoD skill) |
| `setting-canon.md` | Trojan Reach ground-truth (overrides invention). | Session Zero (copied from the PoD skill) |
| `keyed-scenes.md` | The set adventures as trigger-based content (never rails). | Session Zero (copied from the PoD skill) |
| `character-sheet.md` | One per crew member (or a shared file). | Crew creation |
| `reputation-tracker.md` | The empire / per-world Attitude metagame. | Session Zero |
| `harrier-ship-log.md` | The Harrier's condition, fuel, upgrades, defects. | Session Zero |
| `archive.md` | Resolved Threads / dead Characters moved out of state. | As play proceeds |

## How play starts and resumes

- **No `campaign-state.md` here** → the GM runs **Session Zero** (builds the
  crew, assigns the Harrier, seeds the sandbox, opens with *Honour Among
  Thieves*).
- **`campaign-state.md` present** → the GM recaps the last beat and continues.

## Persistence (important in this environment)

This repo runs in an **ephemeral** container — it is cloned fresh each session
and reclaimed afterward. **Your campaign only survives if it is committed and
pushed.** Commit this folder at the end of a play session so the next session
can pick up exactly where you left off.
