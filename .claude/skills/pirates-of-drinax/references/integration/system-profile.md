# Traveller 2e — System Profile (the mythic-gm RPG seam)

> Use this when: mythic-gm needs to resolve a Traveller action or stat an NPC. **Copy this file into the campaign folder at Session Zero** (it is the `system-profile.md` the engine reads). Full rules live in `references/rules/`; this is the routing summary.

## Dice convention
- Core mechanic: **2D6 + DMs**. Express rolls for the engine as `python3 scripts/dice.py roll 2d6+<DM>`. Damage: `roll 3d6`, `roll 2d6+2`, etc.
- **Boon** (roll 3D, keep best 2) → `roll 2d6+<DM> adv`. **Bane** (keep worst 2) → `... dis`. (The engine's adv/dis models Traveller's Boon/Bane.)
- Always roll through the engine and show the dice; never estimate.

## Core resolution
- A check = **2D6 + characteristic DM + skill level + situational DMs vs a Difficulty target**. Default Average = **8+**.
- Difficulty ladder: Simple 2+ · Easy 4+ · Routine 6+ · Average 8+ · Difficult 10+ · Very Difficult 12+ · Formidable 14+ · Impossible 16+.
- Untrained = **−3**. Characteristic DM runs −3 (score 0) to +3 (15+).
- **Degrees of success: YES.** Effect = roll − target. ≥+6 Exceptional · +1..+5 Success · 0 Marginal · −1..−5 Failure · ≤−6 Exceptional Failure. In rule-mode Fate Questions, map Exceptional Yes → Effect ≥+6, Exceptional No → ≤−6.
- Opposed: higher **Effect** wins (ties → reroll or favour defender).
- Detail: `references/rules/task-system.md`.

## Stats & skills
- Characteristics: **STR DEX END INT EDU SOC** (+PSI if psionic). DM by score.
- Skills: level 0..n with specialities; untrained −3. Full list + uses: `references/rules/characters-and-skills.md`. Char-gen: `references/rules/character-creation.md`.

## Combat — personal
- Initiative: 2D6 + DEX DM (+ Tactics). Action economy: Minor / Significant / Reaction.
- Attack: 2D6 + skill + char DM vs **8+** (apply range & situational DMs); Effect adds to damage.
- Damage: weapon dice − armour, applied to characteristics (END, then STR/DEX). Two characteristics at 0 → out of the fight / dying. **Defeat and death are real; Peril Points are OFF.**
- Detail incl. boarding, hazards (vacuum, decompression): `references/rules/personal-combat.md`. Gear: `references/rules/equipment.md`.

## Combat — space (the raider's bread and butter)
- Run on Core + High Guard. Pirate doctrine: **disable, don't destroy** — a wreck pays nothing. Force surrender, then board (→ personal combat).
- Detail: `references/rules/space-combat.md`. Ship ops/jump/sensors/fuel: `references/rules/starship-operations.md`.

## NPC & ship stat convention
- NPC result format: characteristics line + key skills + weapon/armour/gear (+ 1-line motive).
- Ship result format: TL, tonnage, Hull, Armour, Thrust, Jump, Power, weapons (+damage), key systems, crew, cargo.
- **On-the-fly statting (mythic NPC Statistics):** decide the expected value → Fate Question → read `npc_statistics` (Yes = as expected; ExcYes +25%; No −25%; ExcNo −50%). Pre-built blocks: `references/setting/ships-of-the-reach.md`, `references/setting/personalities-and-factions.md`, `references/setting/the-harrier.md`.

## Routing — what the RPG resolves vs. a Fate Question
- **RPG (roll it):** any skill/characteristic task; personal & space combat; the piracy procedure; trade; jump/astrogation/sensors/repairs; reading world (UWP) data.
- **Fate Question (ask the oracle):** world/NPC facts not in canon; "does X happen / is Y true"; offscreen developments; scene mood/disposition.
- **Precedence:** this profile + `references/` + `sources/` **>** training memory. When all are silent, a Fate Question decides and the answer is **written back to `setting-canon.md`** so it stays consistent.

## Ported subsystems (run as their own procedures, not bare Fate Questions)
- **Commerce raiding / piracy** → `references/rules/piracy-raiding.md` (own tables: prey, interception, surrender, loot, heat, fencing).
- **Empire / reputation** → `references/campaign/empire-reputation.md` (world Attitudes, recruitment, Fighting Strength).
- **Trade** → `references/rules/trade-commerce.md`.
- Anything else (morale, sanity-style strain, chases not covered) → Fate Question "in the tone and intent of the original".

## Source
Mongoose Traveller 2e Core Rulebook (2022) + High Guard (2022); supplements as cited per file. Full text in `sources/`.
