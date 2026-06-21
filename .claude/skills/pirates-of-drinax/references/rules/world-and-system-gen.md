# World & System Data (reading UWPs)
> Use this when: reading a Reach-gazetteer world line, judging starport facilities/fuel, deciding what's legal to carry, working out refuelling, applying trade codes, or rolling a space encounter. This is the decoder for every world in the setting/worlds files.

## Contents
- UWP at a glance (how to parse one line)
- Hex code key (0–9, A–F)
- Each digit's table: Starport, Size, Atmosphere, Hydrographics, Population, Government, Law Level, Tech Level
- Starport classes (facilities / fuel / repair / bases)
- Bases (Naval, Scout, Corsair, Depot, Military, Way Station)
- Travel zones (Green / Amber / Red)
- Trade codes (Ag…Wa) — conditions + trade meaning
- Law level vs weapons/armour + getting caught
- System contents & refuelling (gas giants, belts)
- Encounter generation (pointer)

---

## UWP at a glance
A world line reads: `Name (hex) Starport-Size-Atmo-Hydro-Pop-Gov-Law–Tech  Bases  Trade codes  TravelZone` (Core p.247).
Example: `Cogri 0101 CA6A643-9 N Ri Wa A` =
- `C` Starport (routine), `A` Size 10, `6` Atmo standard, `A` Hydro waterworld, `6` Pop millions, `4` Gov representative democracy, `3` Law, **dash**, `9` Tech.
- `N` = Naval base. `Ri Wa` = Rich Waterworld. `A` = Amber Zone (R=Red; blank=Green/unclassified).
- The dash always sits between **Law** and **Tech**. The four-digit number after the name is the **hex** (column/row on the subsector map).

## Hex code key
Codes are base-16. 0–9 = digits; A=10, B=11, C=12, D=13, E=14, F=15 (occasionally G=16 for TL16). Read each UWP digit against its own table below (Core p.247–248).

---

## Starport (1st digit: A–E, X)
Quality, fuel and build/repair capability. Imperial-run and **extraterritorial** (locally-illegal goods are legal *inside* the port; paranoid worlds may board anyway). Port law ≈ Law Level 1; psionics forbidden (Core p.258).

| Code | Quality | Berth/week | Fuel | Build/Repair | Highport? |
|---|---|---|---|---|---|
| A | Excellent | 1D×Cr1000 | Refined | Shipyard (all types, incl. **jump-capable**); full Repair | on 6+ |
| B | Good | 1D×Cr500 | Refined | Shipyard (spacecraft ≤5000t, **non-jump**); full Repair | on 8+ |
| C | Routine | 1D×Cr100 | **Unrefined** | Shipyard (small craft <100t); full Repair | on 10+ |
| D | Poor | 1D×Cr10 | **Unrefined** | **Limited Repair** (hull only) | on 12+ |
| E | Frontier | 0 | **None** | None | — |
| X | None | 0 | None | None (bare beacon / interdicted) | — |

- Only **Class A** can build jump drives / jump-capable ships. **Limited Repair** (D) fixes Hull damage only.
- Refined fuel Cr500/ton (safe to jump on). Unrefined Cr100/ton (jump risk — see starship-operations.md). Naval/Scout bases supply **refined** fuel to their own ships.
- Quality can vary from the code (a decayed Class A, an expert-run Class D); starport TL can exceed the world's TL.

## Size (2nd digit: 0–A)
Diameter (thousands km) → surface gravity. 0 = asteroid/orbital (<1000km).

| Size | Diam | Gravity | | Size | Diam | Gravity |
|---|---|---|---|---|---|---|
| 0 | <1000km | negligible | | 6 | 9,600 | 0.7 G |
| 1 | 1,600 | 0.05 | | 7 | 11,200 | 0.9 |
| 2 | 3,200 | 0.15 | | 8 | 12,800 (Earth) | 1.0 |
| 3 | 4,800 | 0.25 | | 9 | 14,400 | 1.25 |
| 4 | 6,400 (Mars) | 0.35 | | A(10) | 16,000 | 1.4 |
| 5 | 8,000 | 0.45 | | | | |

Low-G ≤0.7 (Size ≤6); High-G ≥1.4 (penalties, Core p.80).

## Atmosphere (3rd digit: 0–F)
Gear column = what a Traveller needs to breathe/survive.

| Code | Type | Gear required |
|---|---|---|
| 0 | None (vacuum) | Vacc suit |
| 1 | Trace | Vacc suit |
| 2 | Very thin, tainted | Respirator + filter |
| 3 | Very thin | Respirator |
| 4 | Thin, tainted | Filter |
| 5 | Thin | — |
| 6 | Standard (Earth) | — |
| 7 | Standard, tainted | Filter |
| 8 | Dense | — |
| 9 | Dense, tainted | Filter |
| A(10) | Exotic | Air supply |
| B(11) | Corrosive | Vacc suit (1D dmg/round if exposed) |
| C(12) | Insidious | Vacc suit (eats seals after ~2D hrs) |
| D(13) | Very dense | — (high-pressure; livable only at altitude) |
| E(14) | Low | — (thin; livable only in lowlands) |
| F(15) | Unusual | Varies |

Tainted = filter or take 1D dmg periodically. Corrosive/Insidious are lethal without sealed gear.

## Hydrographics (4th digit: 0–A)
Surface liquid (usually water; on Fl worlds it's ammonia/methane etc.), in 10% bands.

| 0 | 0–5% desert | 4 | 36–45% wet | 8 | 76–85% islands |
|---|---|---|---|---|---|
| 1 | 6–15% dry | 5 | 46–55% large ocean | 9 | 86–95% |
| 2 | 16–25% | 6 | 56–65% | A(10) | 96–100% waterworld |
| 3 | 26–35% | 7 | 66–75% Earth-like | | |

## Population (5th digit: 0–C)
Number of zeroes after a 1 (e.g. 6 = millions). 0 = uninhabited (Gov, Law, TL also 0).

| 0 | none | 4 | tens of thousands | 8 | hundreds of millions |
|---|---|---|---|---|---|
| 1 | few (1+) | 5 | hundreds of thousands | 9 | billions (Earth) |
| 2 | hundreds | 6 | millions | A(10) | tens of billions |
| 3 | thousands | 7 | tens of millions | B/C | hundreds of billions / trillions |

Pop ≤3 = tiny colony (Gov can change on a whim).

## Government (6th digit: 0–F)
Drives factions and the "Common Contraband" likely banned (not absolute).

| Code | Type | Likely contraband |
|---|---|---|
| 0 | None / anarchy / family | None |
| 1 | Company/Corporation | Weapons, Drugs, Travellers |
| 2 | Participating democracy | Drugs |
| 3 | Self-perpetuating oligarchy | Technology, Weapons, Travellers |
| 4 | Representative democracy | Drugs, Weapons, Psionics |
| 5 | Feudal technocracy | Technology, Weapons, Computers |
| 6 | Captive govt / colony | Weapons, Technology, Travellers |
| 7 | Balkanisation (Law = port's govt) | Varies |
| 8 | Civil service bureaucracy | Drugs, Weapons |
| 9 | Impersonal bureaucracy | Technology, Weapons, Drugs, Travellers, Psionics |
| A(10) | Charismatic dictator | None |
| B(11) | Non-charismatic leader | Weapons, Technology, Computers |
| C(12) | Charismatic oligarchy | Weapons |
| D(13) | Religious dictatorship | Varies |
| E(14) | Religious autocracy | Varies |
| F(15) | Totalitarian oligarchy | Varies |

Factions: roll D3 (DM+1 if Gov 0/7, DM-1 if Gov 10+); re-roll Gov table for each (Core p.254).

## Law Level (7th digit: 0–F)
Sets what's illegal to **carry** and how often the law bothers you. See weapons/armour table below.

## Tech Level (8th digit, after dash: 0–F+)
Average tech; local production/repair ceiling. A rich buyer can usually get TL+2; govt/military often higher; **starport TL may exceed world TL**. Field-by-field variance is normal. Quick read: 0 stone; 3–4 pre-industrial; 5–6 industrial/early electronics; 7 nuclear/early space; 8 today's Earth; 9 grav vehicles cheap & global comms; 10–11 early jump-capable, fusion; 12 = "High Tech" threshold; 13–15 advanced Imperial. Atmosphere survival needs minimum TL (e.g. Atmo 0/1 needs TL8; B needs TL9; C needs TL10) or the population slowly dies out (Core p.259).

---

## Bases (the letters after the UWP)
Each rolled separately at world-gen; treat as present if listed in the gazetteer.

| Code | Base | Use to the crew |
|---|---|---|
| N | Naval | Refined fuel & supplies, repair, hospital (navy only), navy-surplus weapons; always armed/defended. Pirates: hostile, well-guarded. |
| S | Scout | Refined fuel & supplies to scouts; rumours & news. |
| W | Way Station | Imperial Scout x-boat comms hub; services scouts. |
| C | Corsair | Refuel/maintain corsair ships; common pirate staging base. Likely where Law 0. |
| D | Depot | Massive sector-fleet naval base (can fill a system): build/repair/rearm. Heavily defended. |
| M | Military | Planetary ground-forces base (vehicles/troops). |

Combos in setting files may also use scout/naval shorthand; treat any unlisted letter as a minor installation.

## Travel zones
- **Green / blank** — normal; no special warning.
- **Amber (A)** — Imperium-flagged dangerous (upheaval, hazard, lawlessness). Be on guard; encounters DM toward "Wild Space" (see below). Candidate when Atmo 10+, Gov 0/7/10, **and** Law 0 or 9+.
- **Red (R)** — interdicted; entry forbidden and enforced by the Imperial Navy (quarantine, war, preservation, or edict). Going in is itself the adventure/crime.

---

## Trade codes
A world gets a code only if it matches **every** condition in its row (Core p.260; WBH p.186). Blank cell = no condition. Hex digits.

| Code | Name | Conditions (UWP) | Trade meaning |
|---|---|---|---|
| Ag | Agricultural | Atmo 4–8, Hydro 5–7, Pop 5–7 | Farming world; food/livestock cheap to buy, sells high to Hi/In/Na/Po. |
| As | Asteroid | Size 0, Atmo 0, Hydro 0 | Mining/orbital colony; ores, no real gravity. Va implied. |
| Ba | Barren | Pop 0, Gov 0, Law 0 | Uninhabited/empty; salvage, no market. |
| De | Desert | Atmo 2–9, Hydro 0 | Dry, barely habitable. |
| Fl | Fluid Oceans | Atmo A–C or F+, Hydro 1+ | Oceans of non-water (ammonia/methane); hostile to Earth-life. |
| Ga | Garden | Size 6–8, Atmo 5/6/8, Hydro 5–7 | Earth-like paradise; desirable, high land value. |
| Hi | High Pop | Pop 9+ | Billions; huge market & labour, imports food/raw goods. |
| Ht | High Tech | TL 12+ (C+) | Cutting-edge; sells advanced tech, electronics, drugs. |
| Ic | Ice-Capped | Atmo 0–1, Hydro 1+ | Cold, dry, water locked in caps. |
| In | Industrial | Atmo 0–2/4/7/9–C, Pop 9+ | Factory/city world; manufactured goods cheap, imports food & raw materials. |
| Lo | Low Pop | Pop 1–3 | A few thousand or fewer; thin market. |
| Lt | Low Tech | Pop 1+, TL 0–5 | Pre-industrial; buys tech, sells raw/handmade. |
| Na | Non-Agricultural | Atmo 0–3, Hydro 0–3, Pop 6+ | Can't feed itself; imports food at a premium. |
| Ni | Non-Industrial | Pop 4–6 | Imports manufactured goods. |
| Po | Poor | Atmo 2–5, Hydro 0–3 | Marginal; little to sell, cheap labour. |
| Ri | Rich | Atmo 6 or 8, Pop 6–8, Gov 4–9 | Economic powerhouse; luxury market, buys high-value goods. |
| Va | Vacuum | Atmo 0 | No air; everything sealed/underground. |
| Wa | Water World | Hydro A (Size 2–9 or D/E) | Ocean world; sells water/marine goods, scarce land. |

Trade codes feed buy/sell DMs in the Trade rules — use them to pick cargo and predict prices. (Detailed speculative-trade DMs live in the trade/economy reference, not here.)

---

## Law level vs weapons & armour
Roll-up aside, just **read the Law digit** to know what's contraband. A ban includes everything *above* it (e.g. Law 6 also bans the Law 1–5 items).

| Law | Weapons banned | Armour banned |
|---|---|---|
| 0 | none (carry freely) | none |
| 1 | poison gas, explosives, undetectable weapons, WMD | Battle dress |
| 2 | portable energy & laser weapons | Combat armour |
| 3 | military weapons (assault rifles, etc.) | Flak |
| 4 | light assault weapons & SMGs | Cloth |
| 5 | personal concealable weapons | Mesh |
| 6 | all firearms except shotguns & stunners; carrying discouraged | — |
| 7 | shotguns | — |
| 8 | all blades, stunners | all visible armour |
| 9+ | all weapons | all armour |

Also restricted with rising Law: Drugs, Information/computers, Technology, Travellers (offworlders confined to port), Psionics (Core p.255–256).

### Getting caught (when it matters in play)
Roll 2D + DM; if ≤ Law Level, the crew is checked/stopped (Core p.256):

| Situation | DM | Response |
|---|---|---|
| First approach to planet | +0 | Check |
| Wandering streets (1×/day) | +0 | Check |
| Acting suspiciously | -1 | Check |
| Bar fight | -1 | Apprehended |
| Shots fired | -2 | Apprehended |
| Breaking & entering | -2 | Investigate |
| Firefight w/ armour & mil weapons | -4 | Apprehended |
| Murder / carnage | -4 | Investigate |

**Check** = ID checked (Admin/Streetwise to allay; fail → Investigate). **Investigate** = deeper probe, ship searched. **Apprehended** = police arrive armed proportional to threat. Smuggling-sentence DM = (world Law Level − the banned item's law threshold). Sentencing on 2D+DM runs from Dismissed (≤0) up to Death (15+) (Core p.257).

---

## System contents & refuelling
- The UWP describes only the **mainworld** (most-travelled body) — which may itself be a moon or a belt object, not a planet. Other planets/moons exist at referee discretion.
- **Gas giants**: roll **10+ for one *not* to be present** (so usually present). A streamlined ship can **skim** a gas giant for free (unrefined) fuel — no starport needed; takes **1D days** to reach and start skimming (Core p.246, p.156). This is the pirate's standard wilderness refuel.
- **Asteroid/planetoid belts** and water-bearing worlds also give **unrefined** fuel (skim/scoop). Unrefined fuel risks misjump unless processed — see starship-operations.md.
- **Refined** fuel only at Class A/B starports and Naval/Scout bases. No starport + no gas giant/water + your jump range = strand risk; jump routes are rated by the largest refuelling "gap" they cross (jump-1 = fuel every hex; jump-2 = ≤1 empty hex; etc., Core p.247).

## Encounter generation (pointer — keep light)
- **Space**: each day in a system roll **1D; on a 6** an encounter occurs → roll **D66** on the Space Encounters table, applying the region DM to the *first* die only: Highport +3, High-Traffic (industrial+good port) +2, Settled +1, Border +0, **Amber/Red "Wild Space" -1**, Empty -4. Bold results (Pirate, Hostile/Daring Pirate, Warship, Police, Patron, etc.) **can't be ignored** (Core p.155). Pirate hits cluster low on the D66; patrons/traffic high.
- **On a world / personal**: when an encounter is called, roll 2D on the **Encounter Distance** table (Close → Very Distant) to set first-contact range (Core p.84). For *what* shows up and whether it happens, prefer the mythic-gm oracle/Lists over rolling random tables — generate to taste, then place with the distance table.

## Source
Traveller Core Rulebook 2022, "Reading World Profiles / World Creation" (p.247–261: Size, Atmosphere, Hydrographics, Population, Government, Law Level, Tech Level, Starport, Bases, Travel Codes, Trade Codes), Law/Travellers p.255–257, Encounters p.84 & p.155, Gas Giants/Refuelling p.156 & p.246. World Builder's Handbook (Trade Codes p.186) used to reconcile garbled Core table columns.
