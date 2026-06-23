# Campaign folder — your live game lives here

This is the **campaign folder** that the engine reads and writes for live play.
It is the single source of truth for an in-progress game. Everything in
`.claude/skills/` is fixed reference material — including the Traveller 2e seam,
the Reach canon, the doom clocks, and the ingested adventures, which now live in
the companion's **`bridge/`** (read in place by the engine, *not* copied here).
The files below are only the parts that **change as you play**.

## What ends up in this folder

When you start a game, the GM (Claude, running the skills) creates these here:

| File | What it is | Created during |
|---|---|---|
| `campaign-state.md` | **The source of truth.** Chaos Factor, Threads/Characters Lists, crew, the Harrier, finances, reputation, sandbox clocks, last-scene recap, and canon questions answered in play. Overwritten every scene. | Session Zero (template: skill `assets/templates/pod-campaign-state.md`) |
| `character-sheet-*.md` | One per crew member (the PC has `character-sheet-shake.md`). | Crew creation |
| `reputation-tracker.md` | The live empire / per-world Attitude metagame (mechanics: `bridge/subsystems.md` + skill `references/campaign/empire-reputation.md`). | Session Zero |
| `harrier-ship-log.md` | The Harrier's condition, fuel, upgrades, defects. | Session Zero |
| `sector-map.md` | The crew's working chart of the Reach (explored space, routes). | As play proceeds |
| `story-so-far.md` | Narrative recap / archive for resuming in a new session. | As play proceeds |

> **The seam files moved.** `system-profile.md`, `setting-canon.md`, the genre
> pack, and the keyed scenes used to be copied into this folder; in the v2
> engine they are **bridge** files (`.claude/skills/pirates-of-drinax/bridge/`)
> the engine reads directly. Canon discovered in play is recorded in
> `campaign-state.md`, not by editing the bridge.

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
