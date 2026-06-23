# Pirates of Drinax — Reference Index

> Use this when: deciding which reference to load. Read only what the current scene needs. `SKILL.md` is the operating manual; this is the map of `references/` (full verbatim books are in `sources/`, maps in `assets/maps/`).

## ../bridge/ — the mythic-gm companion bridge (fills the engine's hooks; loaded at Session Zero)
> These live in the skill's `bridge/` (a sibling of `references/`), not in `references/`. The engine reads them directly via `bridge.py`; nothing is copied into the campaign folder.

| File | Purpose | Hook |
|---|---|---|
| `bridge/system-profile.md` | Traveller 2e task resolution & combat — the RPG seam the engine reads. | resolve |
| `bridge/setting-canon.md` | Lean world ground-truth (consult before inventing). | (canon) |
| `bridge/interpretation.md` | Tone, "maximal honest consequence," and the per-faction NPC lens. | meaning |
| `bridge/chaos-tendency.md` · `bridge/theme-weights.md` | Chaos start/volatility/floor; fixed Adventure-Crafter theme weights. | chaos · themes |
| `bridge/subsystems.md` | The Reach doom clocks (Imperial Heat, ihatei pressure, Drinax decay, rivals…). | world-tick |
| `bridge/seeds.md` · `bridge/generators/` | Seed-deck sources; verified `list_d100`/`list_d10` tables + routing index. | seeds · generate:* |
| `bridge/adventures/pirates-of-drinax.md` | The set campaign ingested as pure-sandbox clusters (→ `campaign/adventures/`). | adventure-ingest |
| `bridge/bridge.md` | The manifest (which hooks are overridden + file map). | — |

## rules/ — Traveller 2e (play-ready)
| File | Purpose |
|---|---|
| `rules/task-system.md` | 2D6 checks, DMs, difficulty, Effect, Boon/Bane, opposed, chains. |
| `rules/characters-and-skills.md` | Characteristics, the full skill list, checks. |
| `rules/character-creation.md` | Lifepath careers & PC build. |
| `rules/personal-combat.md` | Combat round, damage, armour, wounds, hazards, boarding. |
| `rules/equipment.md` | Weapons, armour, gear, traits. |
| `rules/starship-operations.md` | Crew, jump, fuel, sensors, repairs, costs. |
| `rules/space-combat.md` | Ship-to-ship combat; disable-and-board doctrine. |
| `rules/trade-commerce.md` | Speculative trade, freight, passengers, finances. |
| `rules/piracy-raiding.md` | **The piracy core loop:** prey, interception, surrender, loot, fencing, heat. |
| `rules/world-and-system-gen.md` | Reading UWPs, trade codes, starports, zones. |

## setting/ — the Trojan Reach
| File | Purpose |
|---|---|
| `setting/00_index.md` | Map of the setting folder. |
| `setting/trojan-reach.md` | Sector overview, astrography, history, travel. |
| `setting/factions.md` | The powers (Imperium, Aslan, Florian, Vargr, Sindal, Theev, GeDeCo). |
| `setting/drinax.md` | Drinax, the Floating Palace, King Oleb, the court. |
| `setting/worlds/00_world-index.md` | Master UWP table for all Reach worlds. |
| `setting/worlds/key-worlds.md` | Detailed profiles of campaign-critical worlds. |
| `setting/personalities-and-factions.md` | Recurring NPCs (stats + wants). |
| `setting/the-harrier.md` | The party's ship: stats, defects, deck plan, upgrades. |
| `setting/ships-of-the-reach.md` | NPC/enemy ship stat blocks (prey & threats). |

## campaign/ — the metagame & adventures
| File | Purpose |
|---|---|
| `campaign/00_overview.md` | The campaign arc & how the sandbox flows. |
| `campaign/empire-reputation.md` | **The empire-building / reputation metagame.** |
| `campaign/the-crew.md` | PoD char-gen + a ready pregen crew + solo-crew handling. |
| `campaign/seed-lists.md` | Session-Zero Threads/Characters/Features Lists. |
| `campaign/adventures/00_index.md` | Index of all set adventures (spoiler-gated). |
| `campaign/adventures/01..18_*.md` | The individual adventures. |

## discipline/
| File | Purpose |
|---|---|
| `discipline/pod-gm-notes.md` | PoD-specific GMing reminders (layered on mythic-gm's discipline). |

## Loading discipline
Load lean. For most scenes you need only the current adventure file + `piracy-raiding.md` or `empire-reputation.md` + the relevant `setting/worlds` entry. Drill into `sources/` only when a reference is thin.
