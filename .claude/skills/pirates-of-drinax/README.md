# Pirates of Drinax — a Traveller 2e campaign content pack for solo play

This skill lets you play **Pirates of Drinax** — Mongoose Traveller 2e's sandbox piracy campaign in the Trojan Reach — solo / GM-less. It is a **content pack**: it supplies the ruleset, setting, world data, the piracy & empire-building subsystems, and spoiler-gated breakdowns of every adventure. The **mythic-gm** skill is the engine that runs the play loop, rolls every die honestly, asks the oracle, and enforces the no-softening discipline.

> You are a pirate crew with a royal letter of marque and an ancient warship, the *Harrier*. Raid the shipping lanes, build alliances, and — maybe — win back the crown of Drinax.

## Requirements
- **mythic-gm** (the engine — install it too). This pack is built to mythic-gm's adaptation contract.
- It assumes Mongoose Traveller 2e. The full converted rulebooks and campaign books are bundled in `sources/` for verbatim lookup, so no other files are needed to play.

## How to use
Install both skills, then say e.g. *"Let's play Pirates of Drinax solo"* or *"Be my GM for a Traveller pirate campaign in the Trojan Reach."* Claude runs PoD Session Zero: it loads this pack's `bridge/` into the engine, builds your crew, assigns the Harrier, seeds the sandbox, and opens with *Honour Among Thieves*.

## What's inside
- `SKILL.md` — the operating manual: how it plugs into mythic-gm, Session Zero, the pirate play loop, spoiler discipline, and the reference map.
- `references/rules/` — Traveller 2e, play-ready: task system, personal & space combat, equipment, starship ops, trade, **commerce-raiding/piracy**, world data, character creation.
- `references/setting/` — the Trojan Reach: overview, factions, Drinax & the court, a master world index (all 16 subsectors), key-world profiles, recurring NPCs, the Harrier, and enemy/prey ships.
- `references/campaign/` — the campaign arc, the **empire-building reputation metagame**, the crew/pregens, Session-Zero seed Lists, and `adventures/` (spoiler-gated breakdowns of all set adventures + the Patrons collection + the optional *Shadows of Sindal*).
- `bridge/` — the **mythic-gm companion bridge** (fills the engine's hooks): `system-profile.md` (Traveller 2e seam), `setting-canon.md`, `interpretation.md` (tone + faction lens), `chaos-tendency.md`, `theme-weights.md`, `subsystems.md` (doom clocks), `seeds.md`, `generators/` (verified tables), and `adventures/` (the set campaign ingested as pure-sandbox clusters). Validate with `python3 ../mythic-gm/scripts/bridge.py validate ./bridge`.
- `references/discipline/` — PoD-specific GMing reminders.
- `assets/templates/` — campaign-state, reputation tracker, and Harrier ship-log templates.
- `assets/maps/` — key maps (Trojan Reach, Drinax, the Harrier deck plan) where available.
- `sources/` — the full converted rulebooks & campaign books for deep lookup.

## Spoilers
The adventure files are **spoiler-gated** (Player-Facing vs. GM-Only). If you intend to play, read only the Player-Facing sections; let the engine reveal the rest in play.

## Attribution / personal use
Traveller © Mongoose Publishing / Far Future Enterprises. *Pirates of Drinax*, the *Drinaxian Companion*, and related material © Mongoose Publishing. The bundled source text consists of the user's own converted copies, included for personal use. Distribute the engine and this pack without the copyrighted source text if sharing.
