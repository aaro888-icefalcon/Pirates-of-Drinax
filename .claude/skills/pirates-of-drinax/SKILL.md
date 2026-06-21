---
name: pirates-of-drinax
description: >-
  Complete content pack for running the PIRATES OF DRINAX campaign in Mongoose Traveller
  2e (Trojan Reach setting) as a solo / GM-less game on top of the mythic-gm engine.
  Bundles the full Traveller 2e ruleset (task system, personal & space combat, trade,
  commerce-raiding/piracy, starship ops, character creation), the Trojan Reach setting
  and world data, the empire-building reputation metagame, and spoiler-gated breakdowns
  of every set adventure (Honour Among Thieves, Treasure Ship, Ihatei!, The Demon's Eye,
  and the rest). USE THIS whenever the user wants to play, run, GM, start, or continue
  Pirates of Drinax or a Traveller game in the Trojan Reach; mentions Drinax, King Oleb,
  the Harrier, a letter of marque, commerce raiding, the Aslan Hierate, "become king of
  Drinax", the Floating Palace, or any Reach world/adventure by name; or asks to play
  Traveller solo. Layers onto mythic-gm, which runs the dice/oracle/loop.
---

# PIRATES OF DRINAX — Traveller 2e Campaign Content Pack

This skill turns **Mongoose Traveller 2e** + the **Pirates of Drinax** campaign into solo / GM-less play. It is the **content**; **mythic-gm is the engine.** mythic-gm runs the play loop, rolls every die honestly through its scripts, asks Fate Questions, and enforces the no-softening discipline. This pack supplies the *ruleset, setting, world data, the piracy & empire subsystems, and the adventures*, shaped to slot into mythic-gm's adaptation contract.

> **The pitch:** The Travellers are a pirate crew granted a *letter of marque* by Oleb, last King of Drinax, and gifted the ancient warship **Harrier**. They prey on shipping in the Trojan Reach, build alliances, and — maybe — restore the Kingdom of Drinax to power. The Reach is a **sandbox**; the ten+ set adventures are content the oracle plays through honestly, never rails.

---

## ⚠️ FIRST ACTIONS (every time this skill is invoked)

1. **Ensure the engine is loaded.** This pack assumes **mythic-gm**. If it is available, it owns the loop, dice, oracle, Chaos, Lists, and discipline — defer to its `SKILL.md`. If it is *not* loaded, tell the user this campaign is built to run on the mythic-gm skill and ask them to enable it; do not reinvent the engine.
2. **Read the live state.** Look for `campaign-state.md` in the campaign folder.
   - **Present** → continue: recap the last beat, reload only the references the current scene needs (see Reference Loading Guide), resume mythic-gm's Turn.
   - **Absent** → run **PoD SESSION ZERO** (below).
3. **Honor mythic-gm's CREED and discipline.** Honest dice, pre-committed stakes, NPCs act to win, the oracle's answer stands, **Player ≠ PC knowledge** (critical here — the adventures are spoiler-gated; see below).
4. **Look up; don't improvise.** Every Traveller rule, world, NPC, ship, and adventure beat is in `references/` (and verbatim in `sources/`). Never invent a mechanic or a canon fact you can read.

---

## How this pack plugs into mythic-gm (the seam)

mythic-gm reads a small fixed set of files from the **campaign folder** (defined by mythic-gm's own adaptation guide, its `compatibility-spec.md`). This pack ships those files **ready-made** so Session Zero is copy-not-derive:

| mythic-gm expects | This pack provides (copy into campaign folder) |
|---|---|
| `system-profile.md` (task resolution & combat) | `references/integration/system-profile.md` |
| `setting-canon.md` (world ground-truth) | `references/integration/setting-canon.md` |
| `keyed-scenes.md` + seeded Threads/Characters/Features | `references/integration/keyed-scenes.md` + `references/campaign/seed-lists.md` |
| `character-sheet.md` (per PC) | built via `references/rules/character-creation.md` flow |

The engine never changes; only these campaign files do. When a rule, place, or NPC is unstated, mythic-gm decides it with a Fate Question and records it to canon/state. **Precedence:** this pack's references/sources > Claude's training memory of Traveller or Drinax.

---

## PoD SESSION ZERO (no state yet)

Run mythic-gm's Session Zero, making these PoD choices:

1. **Engine & tone.** mythic-gm; honest dice; genre = **space-opera piracy with hard consequences** (`references/integration/genre-pirates-of-drinax.md`). Resolution: Fate Chart, Chaos Factor 5.
2. **Ruleset.** Copy `references/integration/system-profile.md` → campaign folder (Traveller 2e seam).
3. **Setting.** Copy `references/integration/setting-canon.md` → campaign folder. Skim `references/setting/00_index.md`.
4. **Adventure mode = Prepared Adventure (sandbox).** Copy `references/integration/keyed-scenes.md`; seed the Threads/Characters/Adventure-Features Lists from `references/campaign/seed-lists.md`.
5. **Create the crew.** Use `references/rules/character-creation.md` (Traveller lifepath). Fast option: the pregen crew in `references/campaign/the-crew.md`. Record each to a `character-sheet.md`.
6. **The ship.** Assign the **Harrier** (`references/setting/the-harrier.md`) as the shared party asset; copy `assets/templates/harrier-ship-log.md` into state.
7. **The reputation metagame.** Initialize the empire/attitude tracker from `references/campaign/empire-reputation.md` (`assets/templates/reputation-tracker.md`).
8. **Open with the inciting adventure** — `references/campaign/adventures/01_honour-among-thieves.md` (the King's offer). Read only its *Setup/Player-facing* section aloud, describe the Floating Palace scene, then **"What do you do?"** and STOP.

---

## The PoD campaign loop (inside mythic-gm's Turn)

The Reach is a sandbox. Within mythic-gm's scene loop, the crew cycle through **pirate activities**. Each is a subsystem with its own reference; route every uncertain action through mythic-gm (Traveller mechanic → roll via `system-profile`; world question → Fate Question):

- **TRAVEL the Reach** — jump-by-jump across subsectors; refuel, dodge patrols. → `references/setting/worlds/`, `references/rules/starship-operations.md`
- **COMMERCE-RAIDING / PIRACY** — pick a hunting ground, find prey, intercept, hail/threaten, board, plunder, then fence the goods and dodge the consequences. → `references/rules/piracy-raiding.md`
- **TRADE** — speculative trade, freight, passengers (cover identity + income). → `references/rules/trade-commerce.md`
- **DIPLOMACY & EMPIRE** — shift world Attitudes toward Drinax, recruit allies, rebuild the kingdom; the campaign's long victory track. → `references/campaign/empire-reputation.md`
- **SET-PIECE ADVENTURES** — triggered by patrons, travel, reputation, or Random Events. → `references/campaign/adventures/00_index.md`
- **COMBAT** — space combat (ship vs ship, the raider's bread and butter) and personal combat (boarding actions, dirtside trouble). → `references/rules/space-combat.md`, `references/rules/personal-combat.md`

**Sandbox clocks** (advance in bookkeeping): Imperial Navy "heat", Aslan *ihatei* migration pressure, Drinax's decay, rival pirates. Track in state.

---

## Spoiler discipline — the adventures are GATED

Every adventure file in `references/campaign/adventures/` is split into:

- **Player-facing** (the hook, what the crew can openly perceive) — safe to narrate.
- **GM-only / Truth** (secrets, twists, villains' real plans, hidden stats) — **read only as the crew earns it in play.** Apply mythic-gm's *Player ≠ PC knowledge*: these facts are only *potential* until discovered, and honest dice may overturn them. Never steer toward or leak un-earned knowledge.

When opening an adventure, read its **Setup** + **Player-facing** first. Pull GM-only details one beat at a time, as the fiction reaches them.

---

## Reference Loading Guide

| When you need… | Read |
|---|---|
| The whole reference map | `references/00_index.md` |
| Core resolution (2D6, DMs, difficulty, boons/banes, opposed, tasks) | `references/rules/task-system.md` |
| Characteristics, skills, checks | `references/rules/characters-and-skills.md` |
| Build a Traveller (lifepath careers) | `references/rules/character-creation.md` |
| Personal combat, damage, armour, criticals | `references/rules/personal-combat.md` |
| Weapons, armour, gear | `references/rules/equipment.md` |
| Crew roles, jump, fuel, sensors, repairs | `references/rules/starship-operations.md` |
| Ship-to-ship combat | `references/rules/space-combat.md` |
| Speculative trade, freight, passengers | `references/rules/trade-commerce.md` |
| **Commerce raiding / piracy procedure** | `references/rules/piracy-raiding.md` |
| World & system data (UWP), encounters | `references/rules/world-and-system-gen.md` |
| The Trojan Reach: astrography, factions, history | `references/setting/00_index.md` |
| Drinax, King Oleb, the Floating Palace, the court | `references/setting/drinax.md` |
| Any Reach world / subsector data | `references/setting/worlds/00_world-index.md` |
| Recurring NPCs & factions | `references/setting/personalities-and-factions.md` |
| The Harrier (stats, deck plan, defects, ops) | `references/setting/the-harrier.md` |
| NPC & enemy ship stats | `references/setting/ships-of-the-reach.md` |
| **Empire-building / reputation metagame** | `references/campaign/empire-reputation.md` |
| The campaign arc & how the sandbox flows | `references/campaign/00_overview.md` |
| A specific adventure (spoiler-gated) | `references/campaign/adventures/00_index.md` → the file |
| Tone & stakes vocabulary | `references/integration/genre-pirates-of-drinax.md` |
| Verbatim rules/lore (when a reference is thin) | `sources/` (full converted books) |
| Maps (Reach, subsectors, Harrier deck plan, Drinax) | `assets/maps/` |

## Campaign state additions (PoD)

Beyond mythic-gm's `campaign-state.md`, track (template: `assets/templates/pod-campaign-state.md`):
the **Harrier**'s condition & upgrades, the **crew** & morale, **letter-of-marque** standing, **finances/plunder**, **Reputation with Drinax + per-world Attitudes** (the empire track), **adventures in play / completed**, and the **sandbox clocks**. Overwrite each scene, as mythic-gm requires.

## Failure modes (DO NOT)

| Failure | Prevention |
|---|---|
| Running the loop/dice yourself | mythic-gm owns the engine; defer to it; all randomness via its scripts |
| Improvising a Traveller rule | Read `references/rules/`; it's there |
| Leaking an adventure's twist | Adventures are spoiler-gated; Player ≠ PC knowledge |
| Treating the module as rails | Sandbox + keyed scenes; the dice decide; adapt when they overturn the script |
| Inventing a world/NPC that exists | Check `references/setting/`; canon over memory |
| Playing the Imperium/Aslan/rivals dumb | NPCs & navies act to win; stat them via mythic-gm and roll |

---

*This pack is for personal use. Traveller © Mongoose Publishing / Far Future Enterprises; Pirates of Drinax and the Drinaxian Companion © Mongoose Publishing. Bundled source text is the user's own converted copies.*
