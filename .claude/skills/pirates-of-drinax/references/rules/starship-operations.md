# Starship Operations (non-combat)
> Use this when: adjudicating crew duties, jumping, refuelling, fuel, power, sensors/detection, comms, repairs, life support, or running/operating costs for the corsair. For shooting, see space-combat.

## Contents
- Crew positions & skills
- Minimum vs full crew
- JUMP procedure (plot → fuel → initiate → transit → emerge)
- Misjump
- Fuel: refined vs unrefined, refuelling, scoops & processors
- Power management
- Sensors & detection (DMs, ranges, lock, stealth, jamming, ELINT)
- Communications
- Common spacecraft tasks (non-combat)
- Repairs & damage control
- Life support & staterooms
- Operating costs

---

## Crew positions & skills
Each duty uses a primary skill. One person may legally hold two jobs (75% pay each); doing three jobs is unregulated and common on corsairs (SOM p.116).

| Position | Skill used | What they do | Commercial need |
|---|---|---|---|
| Captain | Leadership, Tactics (naval), Persuade/Broker, Admin | Commands; in combat boosts Initiative; negotiates deals & passengers | Usually the leading officer (1) |
| Pilot | Pilot (spacecraft / small craft) | Flies, lands, docks, evasion, gas-giant skim | 1 + 1 per small craft |
| Astrogator | Astrogation | Plots jumps | 1 if jump drive installed |
| Engineer | Engineer (j-drive / m-drive / power) | Drives, power plant, initiates jump, damage control | 1 per 35 tons of drives + power plant |
| Maintenance | Mechanic | Routine upkeep, jury-rig, repairs | 1 per 1,000 tons |
| Gunner | Gunner (turret / ortillery / capital) | Fires a turret/bay; point defence; sand | 1 per turret/barbette/screen |
| Sensor Op (sensop) | Electronics (sensors) | Detection, sensor lock, electronic warfare, missile defence | 1 per 7,500 tons |
| Comms (commo) | Electronics (comms) | Open/close channels, jam, punch through interference, languages | usually computer-run; assigned as needed |
| Steward | Steward | Passengers (1 lvl per 10 High / 100 Middle), cooking, crew morale | by passenger load |
| Medic | Medic | Heals; revives low-berth passengers (Routine 6+) | 1 per 120 crew + passengers |
| Broker | Broker (Captain often doubles) | Buys/sells cargo, finds work | as needed |
| Marine / boarder | Gun Combat, Melee (blade), Vacc Suit, Battle Dress | Repels boarders / storms enemy ships | 0 baseline; carried for raiding |
| Administrator | Admin | Paperwork, customs, fleet logistics | 1 per 2,000 tons |
| Officer | Leadership or Persuade | Supervises crew | 1 per full 20 crew |

(High Guard p.22–23 Crew Requirements; Core p.164 Crew Duties; SOM p.116–119 Crew Roles)

### Notes for small/pirate crews
- A ship <1,000 tons can run on **1–2 multi-skilled people** but is badly disadvantaged in any high-stress event (combat, crisis). Sensop and commo are the "phantom positions" — automated on small ships; sensop earns its keep when the unexpected happens, commo mostly when far-range/jammed signals or alien languages matter (SOM p.119, HG p.22).
- Sensop/EW and gunner duties are what make a corsair effective in a fight; cargo handling, security, and stewarding are "everyone" duties shared in port (SOM p.119).
- **Reassignment:** any crew may switch duty (takes effect next round) instead of acting (Core p.172).

## Minimum vs full crew
- **Minimum (skeleton):** Pilot (also flies/astrogates), Engineer (also power + damage control). Two people can move a <1,000-ton ship between systems.
- **Working corsair crew:** Pilot, Astrogator, Engineer, ≥1 Gunner per turret, Sensop, Medic, Captain/Broker; plus Marines/boarders for raids and a Steward if carrying prize passengers/prisoners.
- **Automated crew:** a ship running the right software can self-fill duties — Fire Control = gunner, Auto-Repair + repair drones = damage control, Intellect + Expert (skill) program = pilot/engineer/sensop (Core p.164). Robots can replace roles; economics favour it on large ships, harder on small (SOM p.116).
- Ships >5,000 tons reduce required crew (engineer/maint/gunner/admin/sensop only) by the Crew Reduction multiplier: 5,001–19,999 ×0.75; 20,000–49,999 ×0.67; 50,000–99,999 ×0.50; 100,000+ ×0.33 (HG p.22).

---

## JUMP procedure
Five phases: **Transit → Plotting → Initiation → Travel → Emergence** (SOM p.83). Plot is normally done during the burn out to the 100-diameter limit.

1. **Transit / reach jump limit.** Can only safely jump >100 diameters from any object larger than the ship (e.g. ~1.27M km from Earth, plus the same rule vs the star and any moon). Gravity inside the limit collapses the bubble. (Core p.157)
2. **Plot the jump (Astrogator).** Easy (4+) **Astrogation** check, 1D×10 min, EDU; **DM = −parsecs** (a 4-pc jump is DM−4). Fail = replot. (Core p.157)
3. **Initiate the jump (Engineer).** Easy (4+) **Engineer (j-drive)** check, 1D×10 min, EDU. Carries the task-chain DM from the Astrogation Effect, plus:
   - Jump drive not maintained: **−1 per month** behind maintenance
   - Using **unrefined fuel: −2**
   - Still inside the 100-diameter limit: **−4**
   - Fail this check = **misjump**. (Core p.157)
   - Needs Power = 10% hull × jump number, and enough Power free (hence "jump dimming" of non-essential systems). Insufficient Power = cannot jump. (Core p.152, 157)
4. **Fuel cost (confirmed):** **10% of hull tonnage per parsec.** 200-ton ship, jump-2 = 20 × 2 = **40 tons**. Jumps <1 pc still count as jump-1 for plot DM and fuel. (Core p.157)
5. **Travel:** always ~1 week in jumpspace regardless of distance = **148 + 6D hours**. Completely cut off — no comms, not even psionic. Distance = jump number in parsecs (1 pc = 1 hex ≈ 3 ly). (Core p.157)
6. **Emergence:** accurate jump exits near the target world but at/near the 100-diameter limit; inaccurate jumps dump the ship somewhere in the inner system (long sublight flight). (Core p.157)

**Combat jump:** raise both Astrogation and Engineer (j-drive) difficulty by one level to compress time to 1D minutes (one combat round) (Core p.171).
**Jump masking / hiding:** a star or world between origin and target collapses the bubble early — you fall out of jump on reaching that body's 100-diameter limit (Core p.157). Ships hide from sensors behind asteroids/planets, not in jump.

### Misjump (Core p.157)
Causes: usually **lack of maintenance** or **unrefined fuel** (= the failed Engineer (j-drive) check). Effects by Effect of the failed check:
| Effect of fail | Result |
|---|---|
| −1 | Arrives in target system **1D days late**; optionally +1D extra days of subjective crew time (relativity error). |
| −2 | Arrives **1D × 100-diameters** away from the target world (long flight in). |
| Worse | Merciful referee: ship ends up **1D × 1D parsecs** in a random direction, possibly deep empty space. Many real misjumps are lethal (bubble collapses early; or trillions of subjective years pass and only hard radiation emerges). |

---

## Fuel
Fusion power plant **and** jump drive both burn hydrogen. (Core p.156)

| Type | Cost / ton | Risk |
|---|---|---|
| Refined | **Cr500** | none |
| Unrefined | **Cr100** | **DM−2 to the Engineer (j-drive) jump check** (misjump risk). Also feeds power plant fine but contaminants can clog drives. |

### Refuelling options
- **Starport / facility:** buy refined or unrefined; ~**1D hours** to refuel a typical ship (Core p.156). Refined needs a Class A/B (sometimes C) port with a refinery (SOM p.23).
- **Gas-giant skimming:** ship with **fuel scoops** (partial streamlining or better) skims hydrogen — **Difficult (10+) Pilot** check, 1D hours, DEX. Yields **unrefined** fuel. (Core p.156)
- **Ocean / water (wilderness):** scoops gather water via hoses and electrolyse it; yields unrefined. (Core p.156) Some systems ban ocean refuelling or mine oceans/gas giants with CAPTOR mines (SOM p.24).
- **Comet ice / star skimming:** ice-type scoops carve cometary ice; atmosphere scoops can skim a star's hydrogen at gas-giant rates but needs heavy heat/radiation shielding — "desperate or foolhardy"; result is unrefined (SOM p.23–24).
- **Fuel scoops + fuel processors:** scoops mine the environment; **fuel processors refine** wild/unrefined fuel into refined. Typical timing: **2–4 hours to scoop, ~24 hours to process** a full jump's worth (some ships do 12h). Process one tank/wing at a time en route to the jump limit. (Core p.156; SOM p.23, 159)
- **Caution:** always run purchased "refined" fuel through purifiers or test it — backwater ports (and pirate-extorted crews) have been known to top tanks with cement/slurry/waste, clogging drives for hours to weeks (SOM p.23–24). Salvage can also yield **2D×10 tons** of fuel from a derelict (Core p.156).

---

## Power management (Core p.152–153)
Power requirements:
- **Basic ship systems** (life support, computer, grav, heat/light): **20% of hull tonnage**. Shutting non-essentials halves this.
- **Manoeuvre drive:** 10% hull × max Thrust.
- **Jump drive:** 10% hull × max jump number — **only when actually jumping** (inert otherwise).
- **Weapons:** per Weapons & Power — Beam Laser 4, Pulse Laser 4, Particle Beam 8, Sandcaster 0, Missile Rack 0, Turret 1 (Core p.152).

If Power drops below need, shut systems down. In a crisis (e.g. damaged plant but want to jump), engineers shut weapons/m-drive/non-essentials to free Power. Engineer combat actions: **Offline System** (Engineer (power), 1 rd, free Power); **Overload Plant** (Difficult 10+ Engineer (power): +10% Power next round; cumulative −2 each retry; −6 fail = Severity 1 crit); **Overload Drive** (Difficult 10+ Engineer (m-drive): +1 Thrust next round; same penalty/crit) (Core p.171). **No Power = no jump, no life support failure cascade.**

---

## Sensors & detection
All ships have **Basic** sensors unless upgraded; the suite's DM applies to **all** Electronics (sensors) and Electronics (comms) checks (HG p.21).

| Suite | TL | Sensors | DM | Power | Tons | Cost |
|---|---|---|---|---|---|---|
| Basic | 8 | Lidar, Radar | **−4** | 0 | — | — |
| Civilian | 9 | Lidar, Radar | −2 | 1 | 1 | MCr3 |
| Military | 10 | +Jammers | +0 | 2 | 2 | MCr4.1 |
| Improved | 12 | +Densitometer | +1 | 4 | 3 | MCr4.3 |
| Advanced | 15 | +NAS | +2 | 6 | 5 | MCr5.3 |

### Range bands (space) (Core p.160, 165)
Adjacent ≤1 km · Close 1–10 km · Short 11–1,250 km · Medium 1,251–10,000 km · Long 10,001–25,000 km · Very Long 25,001–50,000 km · Distant >50,000 km. Most hostile encounters first detect at Very Long/Distant. Detail degrades with range and sensor type (Visual: Full to Short, Limited to Long; passive radar weakest). Active radar/lidar gives the target **DM+2 to detect you back**. NAS (intelligence/neural) and densitometers (internal structure) need close range.

### Initial Detection DMs (HG p.76) — applied to the Electronics (sensors) check
| Factor | DM |
|---|---|
| TL difference | +1 per TL the detector is higher |
| Target running **active** sensors | +2 |
| Target passive sensors only | +0 |
| Target operating **manoeuvre drive** | **+1 per Thrust** |
| Target operating power plant (basic systems+) | +1 |
| Target running **transponder / radio comms** | **+6** |
| Extended array deployed | +2 |
| Target has **stealth** | −2 / −4 / −6 |

Routine post-jump/in-transit detection is automatic; an **Average (8+) Electronics (sensors)** check (1D min, EDU) gets precise data needed to approach/board/fight. Civilian/military ships broadcast an IFF beacon → **DM+4** to detect them (Core p.155). Surprise in space is rare but possible vs damaged sensors or an inattentive sensop (Core p.165).

### Sensor lock & electronic warfare (Core p.171–172)
- **Sensor Lock (sensop):** Electronics (sensors) check → **DM+2** to your ship's attacks vs that target until broken.
- **Electronic Warfare (sensop):** opposed Electronics (sensors)/(comms) to **break an enemy lock** or **jam comms**; vs missiles, Difficult (10+) Electronics (sensors) destroys/diverts that many missiles from a salvo (once/round, cumulative over rounds).

### Stealth & jamming (HG p.14, 54–55, 77)
- **Stealth coating** DM to be detected: Basic/Improved −2, Enhanced −4, Advanced −6. Sensor contact with a stealth ship **can be lost if range opens by a band**. Stealth bonus is reduced if the stealth ship: fires weapons (+2 to spot it), is damaged (+1/Severity, heat), uses active sensors (+2), runs m-drive (+1/Thrust), or uses transponder/comms (+6).
- **Countermeasures suite** (TL13, 2t, MCr4): +4 to jam/EW. **Military countermeasures** (TL15, 15t, MCr28): +6. Meson transmissions can't be jammed.
- **Signal processing:** Improved +2 to sensor checks (but enemies double their jamming DMs vs you); Enhanced +4 (no jamming vulnerability).
- **Deep-penetration / shallow-penetration / life scanners** = ELINT-style internal scans of another hull (deep penetration: Adjacent range, 20t scanned/hour per ton of suite; shallow at up to Very Long detects unusual heat/EM such as fire-control on a "merchant").

---

## Communications
- **No FTL comms.** Allies/contacts reachable only when in the same system; even then expect **seconds to minutes** of light-lag between planets (Core p.91).
- **Ship-to-ship real-time** comms use the same Range Bands; beyond **Distant (>50,000 km)** real-time data hand-off / connection is lost (HG p.76–77, 4157). Within a system, longer-range traffic still gets through but with light-speed delay.
- **In jumpspace = total comms blackout** (Core p.157).
- **Commo duty:** clears weak signals and punches through jamming at long range; usually the practical answers are "move closer" or "it's a faked distress call = trap." Useful for **alien languages** beyond Vilani/Galanglic (SOM p.119).
- **Distress:** standard time-stamped SOS (Mayday / Signal GK). Any ship detecting it is legally required to assist or alert authorities; failure is a crime. Some SOS calls are pirate bait (Core p.156).
- **Improvised signal:** with no comms gear, rig a spark-gap radio (wire, power source, tape, gloves) for unmodulated bursts toward a viewport (SOM p.35).
- **Deep-space relay** (HG p.66) handles x-boat-scale data; mail still crosses systems only by physical jump.

---

## Common spacecraft tasks (non-combat) (Core p.151–152, 156, 172)
- **Land at starport:** Routine (6+) Pilot, 1D×10 sec (take 1D min for DM+2). Wilderness landing: Average/Difficult/Very Difficult Pilot by terrain.
- **Atmospheric flight:** streamlined = fine; partial streamlining skims gas giants & Atmo ≤3; unstreamlined entering atmosphere = DM−4 Pilot and 1D damage (ignores armour) per minute of flight.
- **Docking:** Routine (6+) Pilot, 1D min (opposed if resisted; docker at DM−2). Airlock cycles in 10 sec; one airlock per 500 tons.
- **Gas-giant skim:** Difficult (10+) Pilot, 1D hours (see Fuel).
- **Sensor scan / identify:** Electronics (sensors), often automatic; Average (8+) for precise data.
- **Hack/override locks & systems:** Electronics (computers) — airlock override Very Difficult (12+); ship records Average (8+) external/Difficult inside; key systems Formidable (14+).
- **Remote ops:** drones piloted with Electronics (remote ops) out to Medium range; repair/mining/probe drones extend reach (Core p.158–159).

---

## Repairs & damage control (Core p.159, 171–172)
- **Critical hit, quick (in combat):** Repair System action — Average (8+) **Engineer** check (1 rd, INT/EDU), DM **−Severity**, cumulative +1 per round on the same crit. Only restores the crit's *effect*, lasts **1D hours**. Restarting needed if the same location is hit again.
- **Jury-rig:** a crit can be jury-rigged back to function but **fails again after 1D hours** (Core p.159).
- **Proper repair:** **Engineer or Mechanic** check (1D hours) **plus spare parts**. Parts needed = by Effect minus Severity: Effect 1→1 ton, 2→0.8, 3→0.6, 4→0.4, 5→0.2, 6→none. **Spare parts cost Cr100,000/ton**; carry reserves (Core p.159).
- **Hull damage / destroyed gear/weapons** cannot be quick-repaired — the ship must leave combat and go to a yard. Limited-repair starports fix Hull only (Core p.159, world rules).
- **Repair drones + Auto-Repair software:** let Electronics (remote ops) run repairs without a dedicated engineer (Core p.159, 164).

---

## Life support & staterooms (Core p.154; SOM p.34–35)
- Each **stateroom** costs **Cr1,000 per Maintenance Period** (4 weeks) — supplies, air, food, water (spartan meals). Each **person not in a low berth** adds **Cr1,000**. Each occupied **low berth** Cr100. Two basic passengers fit one stateroom; extra basic passengers need 2 tons each (Core p.154, 158).
- A ship literally cannot complete a take-off → jump → land cycle with no functional air circulation — life support is mandatory (SOM p.34).
- **Galley** lets a crew forage/cook on life-bearing worlds; without one, the ship depends on starport food and is vulnerable to spoilage. With galley + wilderness refuelling a ship can stay away from port a long time (still needs spare parts). ~2 kg food/person/day; 1 ton of food ≈ 13.5 m³ (SOM p.35).
- **Crew critical-hit life support:** Severity 2 = life support fails in 1D hours; Severity 4 = fails in 1D rounds; Severity 6 = fails (Core p.170).

---

## Operating costs (per 4-week Maintenance Period) (Core p.153–154, HG p.22)
| Item | Cost |
|---|---|
| **Life support** | Cr1,000 per stateroom · Cr100 per low berth · Cr1,000 per person aboard |
| **Maintenance** | **0.1% of ship purchase price per year ÷ 12** (full maintenance once/year at a shipyard) |
| **Fuel** | Cr500/ton refined · Cr100/ton unrefined |
| **Berthing / landing** | Weekly, varies wildly by world (see starport rules) |
| **Mortgage / debts** | per ship financing |
| **Spare parts** | Cr100,000/ton as needed |

**Crew salaries (skill-1 monthly; +50% per skill level above 1; HG salaries differ slightly):** Captain Cr10,000 · Pilot Cr6,000 · Astrogator Cr5,000 · Engineer Cr4,000 · Sensor Op Cr4,000 · Medic Cr3,000 (Core) / Cr4,000 (HG) · Steward Cr2,000 · Gunner Cr1,000 (Core) / Cr2,000 (HG) · Marine Cr1,000 · Maintenance Cr1,000 · Administrator Cr1,500 · Officer ~Cr5,000.

**Skipping maintenance:** each Maintenance Period skipped, roll 2D with **DM = periods skipped**; on **8+** a critical hit — roll on **Poor Maintenance**: 2–4 Fuel Leak (lose 1D×10% fuel), 5–7 Drive Damaged (1–3 m-drive Thrust −1 & Pilot −1 / 4–6 j-drive disabled), 8–9 Weapon Faulty (DM−1), 10–12 Power Plant (−25% Power, +1D damage ignoring armour, crew 2D×10 rads/week) (Core p.154). Many small/pirate crews pay in **profit shares** rather than salaries (SOM p.116–117).

## Source
Mongoose Traveller 2e **Core Rulebook** (Spacecraft Operations pp.149–164: Power 152–153, Running Costs/Maintenance 153–154, Encounters/Salvage 155–156, Fuel 156, Jump Travel & Misjumps 157, Passengers/Remote Ops/Repairs 158–159, Sensors/Computers/Security 160–162, Travel Times 163, Crew Duties & combat actions 164, 171–172; Comms light-lag p.91). **High Guard 2022** (Crew Requirements & Crew Reduction pp.22–23; Sensors p.21; Stealth p.14; Spacecraft Options — countermeasures/signal processing/penetration scanners pp.54–57; Initial Detection & Stealth tables pp.76–77; Deep-Space Relay p.66). **Starship Operator's Manual** (Crew Roles pp.116–119; Fuel Scooping & Processing pp.23–24; Life Support & galley pp.34–35; Jump phases p.83; Fuel Processor walkthrough p.159).
