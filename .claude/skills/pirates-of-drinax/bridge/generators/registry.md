# Generator Index — Pirates of Drinax / Trojan Reach   (hooks: generate:*)

> Routing **index**, not a blanket override. Each row: *need · when called · table(s) · mode*.
> mode = `replace` (use the companion table) · `conjunction` (layer the companion table on the AC/Mythic core) · `default` (fall through to Mythic/AC).
> Anything not listed → Mythic/AC default. Roll a table with:
> `python3 ../../mythic-gm/scripts/dice.py table <abs path to the .json>` (the engine rolls it honestly).

| need | when it's called | table(s) | mode |
|---|---|---|---|
| new NPC (generic) | any new Character invoked, no faction tie | AC Character Crafter **+** `npc_role.json` | **conjunction** |
| new NPC (faction-tied) | NPC clearly belongs to a power/court | `npc_role.json` (pick the faction row) + `../setting-canon.md` wants + `../interpretation.md` lens | conjunction |
| prey vessel | crew pick a hunting ground and look for a target | `prey_ship.json` | **replace** |
| travel / sandbox complication | a jump leg or an Adventure-Feature slot needs an event | `reach_hazard.json` | replace |
| patron / rumour / adventure seed | a Random Event or port visit should surface a hook | `rumour_of_the_reach.json` | replace |
| location / world | a scene needs a Reach place | `../../references/setting/worlds/00_world-index.md` (canon UWPs) → Fate Question for unstated detail | default+canon |
| faction / org | a new faction surfaces | `../setting-canon.md` "Powers/Factions" → Fate Question | default+canon |
| ship stat block | NPC/enemy hull needed | `../../references/setting/ships-of-the-reach.md` + NPC Statistics Table | default+canon |
| generic inspiration | Discover Meaning, no specific need | Mythic Elements (engine) | **default** |

## Notes
- The Reach is heavily **authored**: worlds, ships, and named NPCs have canon stat blocks and wants. Prefer canon
  (`../setting-canon.md`, `../../references/setting/…`, `../../references/setting/ships-of-the-reach.md`) over a random
  roll whenever the place/person already exists; roll the tables above only to *generate* the unstated.
- Every `*.json` here is a verified `list_d100` / `list_d10` table (contiguous ranges; roll-tested by
  `bridge.py validate`). To add one, copy the schema of an existing file and keep the ranges contiguous.
