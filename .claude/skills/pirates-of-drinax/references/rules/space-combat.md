# Space Combat (Ship-to-Ship)

> Use this when: two or more spacecraft fight in PoD. Optimised for a **pirate** whose goal is to *disable and capture* a prize, not vaporise it. Personal combat after boarding hands off to `personal-combat.md`.

## Contents
- Pirate doctrine (disable, don't destroy)
- Reading a ship stat block
- Setup: range bands, initiative, surprise, crew duties
- The combat round: Manoeuvre → Attack → Actions
- Movement, closing/opening range, evasion
- Attacking: gunnery, weapon stats, damage, armour, scale
- Point defence, sandcasters, screens, shooting down missiles
- Missiles & torpedoes
- Critical hits (location + severity)
- Crew actions & reactions
- Disabling, surrender, pursuit, breaking off, jumping under fire
- Dogfighting (Close/Adjacent)
- Boarding & capturing a vessel
- Quick reference cheat sheet

---

## Pirate doctrine — disable, don't destroy
A dead prize is worthless. To take a ship intact:
1. **Force surrender first.** Open at Long/Medium, sensor-lock, hail, and demand surrender. A merchant facing armed raiders with no escape often yields before a shot lands (roll morale — see Surrender).
2. **Use disabling weapons, not hull-killers.** Best tools: **ion cannon/ion barbette** (drains Power, no permanent damage), **called shots** to M-Drive or Power Plant (cripple mobility), **sandcasters vs boarders**, light laser fire to wear Hull just past surrender threshold. Avoid missiles/torpedoes/particle/railgun on a prize you want whole — they cause Hull damage, criticals to Cargo, and risk wrecking it.
3. **Knock out the drives, board, take it.** Cripple M-Drive (target can't flee) or Power (target goes dark), close to Adjacent, dock, board with marines.
4. **Stop before zero Hull.** A ship at 0 Hull is wrecked (salvage only). Aim to disable, then capture.
- Ion weapons and called shots to M-Drive/Power are the pirate's signature; reserve heavy ordnance for warships that won't yield.

---

## Reading a ship stat block for combat
Pull these numbers before rolling (Core p.168; HG):
| Field | Meaning in combat |
|---|---|
| **Tonnage** | DM to be hit (attacker +1 per full 1,000 tons of target, max +6); dogfight size penalty; bay/spinal size limits |
| **Hull** | Damage track. 0 Hull = wrecked. Each 10% lost = a Severity-1 critical (Sustained Damage) |
| **Armour** | Subtracted from each hit's damage after Effect (meson/ion ignore it) |
| **M-Drive (Thrust)** | Movement & combat manoeuvre budget per round; adds to Initiative |
| **J-Drive (Jump)** | Max jump; needed to escape system |
| **Power** | Powers drives/weapons/systems; ion drains it; engineers reroute it |
| **Weapons** | Type, mount (turret/barbette/bay/fixed), damage, traits, range band |
| **Computer / software** | Evade/n (DM to all incoming attacks), Fire Control/n (auto-gunners or +DM), Auto-Repair |
| **Crew** | Who can fill pilot/gunner/engineer/sensors duties |
- If a number is garbled in a printed block, mark `(verify)`; do not invent.

---

## Setup

### Range bands (Core p.165) — distances are huge vs personal combat
| Band | Distance | Thrust to change one band |
|---|---|---|
| Adjacent | <1 km (docked / boarding) | 1 |
| Close | 1–10 km (dogfight range) | 1 |
| Short | 11–1,250 km | 2 |
| Medium | 1,251–10,000 km | 5 |
| Long | 10,001–25,000 km | 10 |
| Very Long | 25,001–50,000 km | 25 |
| Distant | >50,000 km | 50 |

Most encounters **start at Very Long/Distant** (first detection). Shooting usually begins at Long/Medium. A pirate posing as a harmless merchant may close to **Close** before revealing intent (see Surprise).

### Initiative (Core p.165)
- Roll **once per ship**: `2D + Pilot skill + ship Thrust`.
- Before rolling, the commander (captain) may make a **Tactics (naval)** check; add its Effect to that ship's (or fleet's) Initiative.
- Acting order is highest Initiative first, each round; ships keep their Initiative unless changed by the captain's Improve Initiative action.

### Surprise (Core p.165)
- Hard in space (nowhere to hide), but possible via damaged/inattentive enemy sensors, hiding behind asteroids/moons, or feigning innocence then revealing intent.
- A surprised ship **takes no actions in the first round**. Huge pirate advantage for closing to boarding range or crippling drives unopposed.

### Crew duties (Core p.164) — assign before the fight
One **Pilot** and one **Captain** only; others may have multiples and may swap mid-fight (Reassignment).
- **Pilot** — movement, combat manoeuvre, Evasive Action.
- **Captain** — Leadership & Tactics; Improve Initiative.
- **Engineer** — power plant / m-drive / j-drive / damage control; overloads, repairs, jump.
- **Sensor Operator** — sensor lock, electronic warfare, detect/jam missiles.
- **Turret Gunner** — one per turret (choose turret at start).
- **Bay Gunner** — one per bay.
- **Marine** — repel boarders / board.
- **Passenger** — anyone unassigned, waiting in staterooms.
- **Automated duties:** Fire Control software can gun; Intellect + Expert software can fill pilot/engineer/sensors; Auto-Repair + repair drones can do damage control.

---

## The combat round (Core p.164)
Each round = **6 minutes**. Resolve all ships through each step in Initiative order, then loop:
1. **Manoeuvre Step** — each ship allocates Thrust to movement and/or combat manoeuvring.
2. **Attack Step** — each ship fires weapons / launches boarding.
3. **Actions Step** — misc. actions (repair, jump, sensor lock, EW, reassign, launch craft, captain's Leadership).

> If ships are at **Close or Adjacent**, switch to **Dogfighting** rules (6-second rounds) — see below.

---

## Movement, range change, evasion (Core p.166)

### Closing / opening
- Spend Thrust per the Range-band table to shift one band up/down. Thrust can be banked across rounds.
- **Both closing:** add both ships' movement-Thrust for the band change.
- **One fleeing:** subtract slower Thrust from faster — the faster ship gains/pulls away. *A pirate needs higher effective Thrust than the prize to force or prevent escape.*
- At Long+ it costs huge Thrust to change band — ships rarely manoeuvre at long range except to board or flee.

### Combat manoeuvring — spend leftover Thrust (1 point each, once per type except Evasive):
- **Aid Gunners** — Pilot check starts a task chain giving the ship's gunners a bonus.
- **Docking** — Pilot check; if target resists, opposed Pilot checks, docker at DM-2. Success → boarding possible.
- **Evasive Action** — see below.

### Evasive Action / dodging (Core p.171, reaction)
- Pilot may dodge with **unspent Thrust** after movement/manoeuvre.
- Each unspent Thrust point dodges **one** incoming attack, imposing **−(Pilot skill)** DM on that attack.
- **Evade/n** software instead applies a flat −n DM to *all* incoming attacks automatically (no Thrust cost).

---

## Attacking (Core p.166–168)

### The roll
`2D + Gunner (speciality) + DEX DM`, vs target 8+. Pilot may fire one turret or a fixed mount at **DM-2**.

### Common attack modifiers (Core p.167)
| Bonus | DM | Penalty | DM |
|---|---|---|---|
| Short range | +1 | Long range | −2 |
| Using a pulse laser | +2 | Very Long range | −4 |
| Using a beam laser | +4 | Distant range | −6 |
| Per full 1,000 tons of target | +1 (max +6) | Sensor lock held (yours) | +2 (see crew) |

- **Beam laser barbette +4 / pulse laser barbette +2** to attack (HG p.28–30).
- **Bays** suffer DM-2 vs targets ≤2,000 t, DM-4 vs ≤100 t (HG p.31). Bad against small prizes.
- **Spinal mounts** can't even hit <2,000 t unless it's stationary/caught in blast; huge penalties up close (HG p.34). Irrelevant for taking small merchants.

### Damage & armour
1. Roll the weapon's Damage dice, **add the attack's Effect**.
2. For barbettes/bays apply the **Damage Multiple** (Barbette ×3; Small bay ×10; Medium ×20; Large ×100; Spinal ×1,000) (HG p.29, 31).
3. Subtract target **Armour** (meson and ion ignore Armour). Min damage on a hit is whatever's left; if armour absorbs it all, no Hull loss and **no critical**.
4. Remaining damage comes off **Hull**. At 0 Hull the ship is wrecked (no power/life support).

### Scale (Core p.167) — ship vs person/vehicle
- Spacecraft weapon vs Ground target: **×10 damage**, but **DM-2** to hit small things (use this when sandblasting boarders / shooting a vehicle).
- Ground weapon vs spacecraft: **÷10 damage**, **+2** to hit (a big target).
- Scale multiply/divide is applied **after** Effect and Destructive.

### Pirate-relevant weapon stats
**Turret weapons** (HG p.28): each turret = 1 hardpoint per 100 t of hull; 1/2/3 weapons (single/double/triple). Same-type weapons in a multi-turret fire as one roll, **+1 per damage die per extra weapon**. Mixed types: only one type per round.

| Turret weapon | TL | Range | Pwr | Damage | Cost | Traits | Pirate use |
|---|---|---|---|---|---|---|---|
| Beam Laser | 10 | Medium | 4 | 1D | MCr0.5 | — | +4 to hit; precise low-damage taps to nudge Hull / point defence |
| Pulse Laser | 9 | Long | 4 | 2D | MCr1 | — | +2 to hit; reach + a bit more punch |
| Missile Rack | 7 | Special | 0 | 4D | MCr0.75 | Smart | 12/turret, Cr250k reload; **Hull damage — avoid on prizes** |
| Sandcaster | 9 | Special | 0 | Special | MCr0.25 | — | Defence vs lasers/energy/particle **and vs boarders** (8D ground-scale) |
| Particle Beam | 12 | Very Long | 8 | 3D | MCr4 | Radiation | irradiates crew; **don't use on a prize you'll board** |
| Railgun | 10 | Short | 2 | 2D | MCr1 | AP 4 | kinetic, armour-piercing; Hull damage |
| Fusion Gun | 14 | Medium | 12 | 4D | MCr2 | Radiation | hull-killer; warships only |

**Barbettes** (HG p.30, ×3 multiple, 5 t, 1 hardpoint): Beam (2D, +4), Pulse (3D, +2), Particle (4D, Radiation), Railgun (3D, AP 5), Missile (4D, fires 5 missiles), Torpedo (6D), Plasma (4D, AP 2), Fusion (5D, AP 3, Radiation), **Ion Cannon** (2D×10, **Ion**).
- Nuclear missiles: 1DD, Radiation; 12/turret, Cr450k legal reload — overkill for piracy and very illegal.

**Ion weapons (HG p.30) — the pirate's friend:** ignore armour; instead of Hull, the hit **drains target Power** (rolled damage, no armour). Power loss lasts until the target finishes its next actions; if attack **Effect 6+**, lasts **D3 rounds**. Hardened systems (/fib) keep pre-allocated Power. Ion *torpedo* (HG p.39): reduces Power by **4D×10 × Effect**, lasting Effect rounds. A Power-starved ship can't run drives/weapons — easy to board or to force surrender. No permanent harm to the prize.

---

## Defences: point defence, sandcasters, screens

### Point Defence (Gunner reaction, Core p.171)
- A turret **beam or pulse laser** can shoot down **missiles** in a salvo as it's about to attack. Make a **Gunner (turret)** check; Effect = missiles removed. Double turret +1, triple turret +2. Once per round; a weapon used for PD can't attack that round.
- **Point-defence laser batteries** (HG p.40): auto-intercept missiles/torpedoes, Intercept **Type I +2D / II +4D / III +6D**, 20 t, 1 hardpoint, no gunner needed.
- **Point-defence gauss batteries** (HG p.40): equal vs missiles/torpedoes Thrust ≤10; DM-2 vs Thrust 12–14, DM-6 vs Thrust 15+; 12 shots per reload.

### Sandcasters — Disperse Sand (Gunner reaction, Core p.171)
- Vs a **laser/energy/particle** attack: Gunner (turret) check; on success add **1D + Effect** to Armour against that one attack. Each use spends 1 canister (20/turret, Cr25k reload). Linked sandcasters: +1 negated per extra caster.
- **Vs boarders:** if the Gunner (turret) check succeeds, each boarder takes **8D Ground-scale** damage (do not ×10).
- Canister types (HG p.38): Sand & Pebble (TL7, anti-laser/energy), Sandcutter (TL8), Chaff (TL8, vs sensors/missiles), Anti-Personnel (TL8, vs boarders).

### Screens — Angle Screens (Gunner reaction, HG p.40)
- **Meson screen** (TL13): reduce a meson attack by **2D×10**, remove its Radiation. **Nuclear damper** (TL12): reduce a fusion/nuclear attack by **2D** (every 5 dampers reduce Destructive by 1DD), remove Radiation.
- Angle Screens: Gunner (screen) check; reduce post-armour damage by (screen dice × Effect). Once per round; each screen once.

---

## Missiles & torpedoes (Core p.172; HG p.36–39)
- Fired in **salvos** (all missiles at one target that round). Salvo has effectively **Thrust 10** (advanced missiles Thrust 15) and takes time to arrive:

| Range fired | Rounds to impact |
|---|---|
| Medium and below | Immediate |
| Long | 1 |
| Very Long | 4 |
| Distant | 10 (then inert if no hit) |

- **Detecting launch:** target sensor op Routine (6+) Electronics (sensors) (Average 8+ if firer undetected), +1 per full 10 missiles (max +6).
- **Missile attack roll:** in Attack Step, **no Gunner skill or range DM**; instead **+1 per missile still in the salvo**. Evasion still applies. Distant-launched salvos: DM-2. At Adjacent/Close missiles lose Smart.
- **Missile damage on hit:** roll one missile's damage, subtract armour, **do not add Effect**; instead **multiply damage by Effect, capped at the number of missiles remaining**.
- **Countermeasures, in order each round:** Flee (thrust away — rarely outruns, but buys time); **Electronic Warfare** (sensor op, Difficult 10+, Effect = missiles destroyed, once/salvo/round, cumulative); finally **Point Defence** just before impact.
- **Torpedoes** (HG p.38–39): bigger (6D standard), **halve point-defence Effect**, DM-2 vs ships <2,000 t. Ion torpedo disables Power (above). For piracy, torpedoes are warship-killers — avoid on prizes.

---

## Critical hits (Core p.168–170)
- **Trigger:** an attack that deals Hull damage (gets past armour) with **Effect 6+**. Also, every time cumulative damage hits another **10% of starting Hull**, take a **Severity-1** critical (Sustained Damage).
- **Severity = attack Effect − 5.** Extra damage from criticals **ignores armour**.
- Repeat hit to same location: use the new Severity or (old +1), whichever is higher. A location at **Severity 6** can take no more crits — instead the ship takes **6D extra damage** each further crit there.
- **Called shots** (range Short or less, direct-fire only, not missiles): DM-2; if it crits, **attacker chooses the location**. *This is how a pirate deliberately kills the M-Drive or Power Plant to stop a prize fleeing.*

### Critical Hit Location (2D)
2 Sensors · 3 Power Plant · 4 Fuel · 5 Weapon · 6 Armour · 7 Hull · 8 M-Drive · 9 Cargo · 10 J-Drive · 11 Crew · 12 Bridge

### Critical Hit Effects (summary by Severity 1→6)
| Location | Effect ramp (Sev 1 … Sev 6) |
|---|---|
| **Sensors** | Sensor checks DM-2 → inoperative beyond Medium/Short/Close/Adjacent → fully disabled |
| **Power Plant** | Power −10% → −10% → −50% → Power 0 → Hull Sev +1, Power 0 → Hull Sev +1D, Power 0 |
| **Fuel** | slow leak → 1D t/round → 1D×10% lost → tank destroyed → +Hull Sev → +Hull Sev 1D |
| **Weapon** | one weapon DM-1 → disabled → destroyed → explodes (Hull Sev+1) → D3 explode → 1D explode |
| **Armour** | −1 → −D3 → −1D → −1D → −2D (+Hull Sev) → −2D (+Hull Sev) |
| **Hull** | 1D → 2D → 3D → 4D → 5D → 6D extra damage |
| **M-Drive** | control DM-1 → DM-1 → DM-1 & Thrust −1 → DM-1 & Thrust −1 → **Thrust 0** → Thrust 0 (+Hull Sev) |
| **Cargo** | 10% lost → 1D×10% → 2D×10% → all → all (+Hull Sev) → all (+Hull Sev) — *bad for loot* |
| **J-Drive** | jump checks DM-2 → disabled → destroyed → destroyed (+Hull Sev) → … → … |
| **Crew** | 1 takes 1D → life support fails 1D hrs → 1D crew 2D dmg → LS fails 1D rounds → all 3D dmg → LS fails |
| **Bridge** | a station disabled → computer reboots (software down this+next round) → bandwidth −50% → station destroyed, occupant 1D×1D → computer destroyed → station destroyed, occupant 1D×1D (+Hull Sev) |

> **Pirate read:** a called-shot crit to **M-Drive** (Sev 5 = Thrust 0) strands the prize; **Power Plant** (Sev 4 = Power 0) makes it go dark; **J-Drive** stops escape by jump. **Crew/Bridge** crits help force surrender. **Avoid Cargo, Fuel-destroyed and Hull crits** if you want the prize intact.

---

## Crew actions & reactions (Core p.171–172)
**Reactions** (anytime, by duty):
- **Evasive Action (Pilot)** — dodge with unspent Thrust (above).
- **Point Defence (Gunner)** — shoot down missiles (above).
- **Disperse Sand (Gunner)** — sandcaster vs lasers / vs boarders (above).
- **Angle Screens (Gunner)** — meson screen / nuclear damper (HG).

**Actions Step actions** (one per crew, Initiative order):
- **Improve Initiative (Captain)** — Leadership check; Effect (even if negative) adjusts the ship's Initiative next round.
- **Jump (Engineer)** — astrogation + Engineer (j-drive) at +1 difficulty to compress to 1D minutes; jump out of the fight.
- **Offline System / Overload Drive / Overload Plant (Engineer)** — power management: shut systems to free Power; Difficult (10+) Engineer (m-drive) for +1 Thrust next round, or Engineer (power) for +10% Power next round (failure by −6 = Severity-1 critical to that drive/plant; cumulative DM-2 each retry until maintenance).
- **Repair System (Engineer)** — Average (8+) Engineer, DM-(critical Severity), +1 per round persisting; fixes *critical effects only*, lasts 1D hours. Hull/destroyed gear needs a yard. Fire Control/Auto-Repair software + repair drones can also repair.
- **Reload Turret (Gunner)** — reload sand/missiles; no attack that round.
- **Sensor Lock (Sensor Operator)** — Electronics (sensors); your attacks on that target get **+2** until the lock is broken.
- **Electronic Warfare (Sensor Operator)** — opposed Electronics (comms) to jam enemy comms, or Electronics (sensors) to break their sensor lock; also destroys incoming missiles (above).
- **Boarding Action (Marine)** — at Adjacent, launch boarders (below).
- **Reassignment (Any)** — switch duty; new duty active next round.
- **Medic** — not a ship-combat station; treats casualties between/after rounds per `personal-combat.md` healing. During a boarding fought at Ground scale, medics act per personal-combat rules.

---

## Disabling, surrender, pursuit, breaking off, jumping out

### Disabling vs destroying
- **Disable:** reduce mobility/power without wrecking. Tools (best→bluntest): **Ion** (drains Power), **called shot to M-Drive** (strand it), **called shot to Power Plant** (dark ship), light laser fire to chip Hull, then board.
- **Destroy:** Hull → 0 = wrecked, salvage only. *Only the last resort vs a warship that won't yield.*

### Forcing surrender (no single RAW table at ship scale — adjudicate)
- A pirate should **hail and demand surrender** at the Attack/Actions step. Resolve the captain/crew's nerve as a **morale check** (use the NPC's reaction/morale; the Boarding modifiers below are a good proxy — superior pirate armament, skills and numbers all push toward yielding).
- Strong triggers to yield: drives/power crippled (can't flee), being out-gunned and out-classed, taking a crippling crit, a clearly-superior boarding party docked.
- On surrender: the prize cuts thrust to zero, allows docking and boarding. Crew may still resist boarders (treat at Ground scale if so) — see `personal-combat.md`.

### Pursuit & breaking off
- Pursuit is a Thrust race: faster effective Thrust gains a band each round (subtract slower from faster). Cripple the target's **M-Drive** to end the chase.
- **Breaking off** yourself: keep banking movement-Thrust to open range; expect to eat attacks/Evasive-Action trade-offs while you run.

### Jumping out under fire (Core p.171)
- Engineer's **Jump action**: Astrogation + Engineer (j-drive) at **+1 difficulty** to compress the jump to **1D minutes** (within ~one round). Needs fuel, a clear jump (beyond the 100-diameter limit) and an intact J-Drive — so enemies target the **J-Drive** to trap you (and you target theirs to stop them escaping with the prize).
- A target under **missile** threat may Flee + jump rather than fight; missiles are long-ranged, so jumping is often the only sure escape.

---

## Dogfighting — Close & Adjacent (Core p.173–174)
- When hostile ships are within **Close/Adjacent (≤10 km)**, switch to **6-second rounds**; the normal combat steps are not used. Automatic — costs no action.
- Each round both pilots make **opposed Pilot checks** with:
  | Modifier | DM |
  |---|---|
  | Ship 50 t+ | −1 |
  | Ship 100 t+ | −2 (−1 per extra 100 t) |
  | Each extra enemy in the dogfight after the first | −1 |
  | Per point of Thrust dedicated to dogfighting | +1 |
- **Draw:** neither hits the other with **fixed** weapons. **Winner:** places its ship in a fire arc of choice (and itself out of the loser's forward arc), and gets **+2 to all attacks** this round; loser **−2**. Carry the win margin as a +DM to next round's opposed check.
- **Escaping a dogfight** needs greater Thrust than the enemy or the enemy's consent; otherwise you must win it.
- Turret weapons fire into any arc, so for a turreted pirate a lost dogfight is a penalty, not a loss of the ability to shoot. **Best pirate play:** win the dogfight, pin the prize in your arc, then disable its drives and board.

---

## Boarding & capturing (Core p.175) → then `personal-combat.md`
1. Get to **Adjacent** and ideally **dock** (Pilot check; opposed if resisted, docker DM-2). A disabled/surrendered prize makes this trivial.
2. In the **Actions Step**, marines launch a **boarding action**: takes **2D rounds** to resolve.
3. **Resolve:** both sides roll 2D + modifiers; defender subtracts their total from attacker's; compare:

| Boarding modifier | DM |
|---|---|
| Superior Armour | +1 |
| Superior Weaponry | +1 |
| Superior Skills & Tactics | +2 |
| Superior Numbers | +1 |
| Vastly Superior Numbers | +3 |
| Defender has no Marines on duty | −2 |

| Total | Result |
|---|---|
| −7 or less | Attackers crushed; if docked, defenders may counter-board at **DM+4** |
| −4 to −6 | Attackers defeated; must retreat or be killed/captured |
| −1 to −3 | Fighting continues (re-roll in 1D rounds), defender **+2**; boarded ship loses 2D Hull |
| 0 | Fighting continues (re-roll in 1D rounds) |
| 1 to 3 | Fighting continues, attacker **+2**; boarded ship loses 2D Hull |
| 4 to 6 | Success; ship takes 1D damage (ignores armour); attackers control it after **2D rounds** of pacification |
| 7+ | Attackers storm and take control **immediately** |

- On any "fighting continues," the Referee may **zoom in to Ground scale** and play the corridor firefight directly → use `personal-combat.md` (crew/marine stat blocks, weapons, cover, grappling, sandcaster blasts at boarders).
- **Capturing the prize:** once controlled, you hold an intact hull, its **cargo** (unless Cargo crits destroyed it), and possibly prisoners/ransom. A wrecked (0 Hull) ship yields **salvage** only.

---

## Quick reference cheat sheet
- **Initiative:** 2D + Pilot + Thrust (+Tactics Effect). **Round:** Manoeuvre → Attack → Actions, 6 min (6 sec in dogfight).
- **Attack:** 2D + Gunner + DEX, 8+. Lasers: beam +4 / pulse +2. Range: Short +1, Long −2, V.Long −4, Distant −6. +1 per 1,000 t target (max +6). Sensor lock +2.
- **Damage:** roll + Effect, ×Damage-Multiple (barb ×3 / bay ×10/20/100 / spinal ×1,000), − Armour (ion/meson ignore). 0 Hull = wrecked.
- **Critical:** Hull damage with **Effect 6+** (or each 10% Hull lost). Severity = Effect − 5. Called shot (Short-, DM-2) picks location.
- **Disable a prize:** ion → Power 0; called shot M-Drive → Thrust 0; then dock + board. Don't push Hull to 0.
- **Missiles:** salvo Thrust 10; +1 per missile to hit; damage ×Effect (capped by missiles left); counter with EW then point defence.
- **Board:** Adjacent → 2D rounds → table; "continues" = zoom to `personal-combat.md`.

## Source
- *Traveller Core Rulebook (2022)* — "Space Combat" pp.164–175 (combat round, range bands, initiative, movement, attacks, Spacecraft scale & weapons pp.167–168, criticals pp.168–170, crew actions/reactions pp.171–172, missiles p.172, dogfighting pp.173–174, boarding p.175); Sensors/Range Bands & ship software pp.160–161.
- *High Guard (2022)* — Weapons & Screens pp.28–41 (turret/barbette/bay weapon tables, Ion trait p.30, Radiation trait, damage multiples, sandcaster & screen mechanics, point-defence batteries); Fleet Battles pp.115–122 (abstracted fleet-scale combat & criticals — use only for large engagements, otherwise default to Core ship-scale rules).
