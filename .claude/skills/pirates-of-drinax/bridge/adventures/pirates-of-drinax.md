# Ingested Adventure — Pirates of Drinax (the set campaign)   (hook: adventure-ingest; pure sandbox)
fidelity: light

> The Reach is **available content the oracle plays through honestly, never a fixed order.** Each cluster below points
> at its full, **spoiler-gated** file in `../../references/campaign/adventures/` — read only Setup + Player-facing up
> front; pull GM-only/Truth one beat at a time as the crew earn it. **Player ≠ PC knowledge.** Only the start (01) and
> the *Finale* (10) are effectively fixed; everything else is a menu surfaced by trigger, then chosen by the crew.
> Content bias: **medium** — prefer a relevant authored cluster/fragment, else roll a random Plot Point. Keep a usage
> ledger; lean toward un-used fragments. When a Turning Point draws one fragment from a cluster, prefer its siblings.

## Campaign spine (the through-line — frame these as Expected Scenes when their trigger fires, then Scene-Test)
### cluster: spine-01 — "The King's offer"   (source: 01 Honour Among Thieves)
scene: Session start — Oleb's marque + the Harrier; Princess Rao's "test" mission (hunt the raider Ferrik Redthane). **Must happen first; not Scene-Tested.**
threads: [Keep Oleb's favour & the marque]   characters: [King Oleb XVI, Princess Rao]   elements: [Floating Palace, the Harrier]   themes: [Social, Action]
gate: none (the opener)
fragments:
  - plot_point: "Oleb tests the crew before trusting them with the marque"   themes: [Social]   weight: 1
  - plot_point: "Follow Ferrik's trail through Clarke/Torpol to Theev"   themes: [Mystery, Action]   weight: 1
  - plot_point: "Completing the opener banks a permanent DM+1 to all Finale recruitment"   themes: [Social]   weight: 1

### cluster: spine-heat — "The Imperium notices"   (source: 06 The Game of Sun & Shadow)
scene: When **Imperial Heat fills** (several big raids / a notorious atrocity near Drinax), a punitive flotilla parks near Drinax and hunts the pirate world. Months-long parallel clock.
threads: [Stay ahead of the Navy's attention]   characters: [Vice-Admiral Krond]   elements: [the flagship Eurisko, Drinax]   themes: [Tension, Action]
gate: Imperial Heat clock full (subsystems.md)
fragments:
  - plot_point: "Keep Drinax's patronage of the raids secret"   themes: [Tension, Social]   weight: 1
  - plot_point: "Drive the fleet out by stealth/intrigue/sabotage, never a fleet battle"   themes: [Action]   weight: 1

### cluster: spine-succession — "The triple disappearance"   (source: 09 Blood of the Star Dragon)
scene: Once the crew are deep in Drinaxian politics (sworn to Rao or Harrick) and Drinax-decay pressure ripens, Oleb crashes and all three royals vanish at once — rescue, coup, and choose who rules Drinax into the endgame.
threads: [Restore or seize the Kingdom]   characters: [King Oleb XVI, Princess Rao, Prince Harrick]   elements: [Pillars of Night, Dragon Fortress]   themes: [Social, Personal, Tension]
gate: Drinax decay/succession clock full (subsystems.md); crew entangled in court politics
fragments:
  - plot_point: "A palace coup; rescue the dying king"   themes: [Action, Social]   weight: 1
  - plot_point: "Who rules Drinax (and whether the Zhodani back it) sets the Finale's starting conditions"   themes: [Personal, Social]   weight: 1

### cluster: spine-finale — "The reborn Kingdom"   (source: 10 Finale)
scene: At the late empire milestones (power base + allies in place), the Declaration: recruit allies, throttle the trade route with a blockade, negotiate recognition from two empires, then hold the Floating Palace against the Aslan invasion fleet. **Fixed, lethal climax.**
threads: [Restore or seize the Kingdom]   characters: [the Reach's recruited worlds, an Aslan invasion fleet]   elements: [the trade route, the Floating Palace]   themes: [Action, Social, Tension]
gate: late empire milestones reached (../../references/campaign/empire-reputation.md "Milestones"); hinges off spine-succession
fragments:
  - plot_point: "Recruitment rolls bring worlds into the Kingdom (Attitude + Policy + Other DMs)"   themes: [Social]   weight: 1
  - plot_point: "The blockade, the negotiations, the final battle — win all or lose all"   themes: [Action, Tension]   weight: 1

## Cluster registry — the full menu (each = one episode; open its file for scenes & secrets)
> Surface by the listed trigger, then let the crew choose. Apply each file's `## Empire / Reputation effects` and push its
> `## Threads & hooks onward` onto the Lists when it resolves. Threads/Characters here seed the Lists (below).

| cluster | episode (file) | typical trigger | location | core threads | key characters | themes | clock |
|---|---|---|---|---|---|---|---|
| pod-01 | 01 Honour Among Thieves | **campaign start** | Tlaiowaha/Sindal → Theev | win the marque; hunt Ferrik | Oleb, Rao, Ferrik | Social, Mystery, Action | — |
| pod-02 | 02 Treasure Ship | treasure-ship rumour near Arunisiir | Borderland | the big score | rival pirate band, Star Marines | Action, Tension | hard 12-week |
| pod-03 | 03 Ihatei! | ihatei pressure sighted near Drinax | Hierate (Kteiroa) | stop/redirect the invasion | a uniting warlord, Kasiyl | Tension, Social | hard 25-week |
| pod-04 | 04 The Demon's Eye | Tech-World overture / patron | Tech-World → Tobia | the nanotech chase | Dr. Jali Astor, the god-king | Mystery, Tension | — |
| pod-05 | 05 The Treasure of Sindal | Prof. haut-Belzoni's message to Oleb | Noricum/Sindal Main | the lost hoard (=WMDs) | three rival gangs, haut-Belzoni | Mystery, Action | — |
| pod-06 | 06 Game of Sun & Shadow | **Imperial Heat fills** (spine-heat) | sector-wide; Drinax | keep Drinax secret; drive the fleet out | Vice-Admiral Krond | Tension, Action | months (parallel) |
| pod-07 | 07 The Vorito Gambit | capture the courier *Exalted Spirit* | Drinax → Vorito | unmask GeDeCo's doomsday plan | Rachando, GeDeCo | Mystery, Social | — |
| pod-08 | 08 The Prodigal Outcast | Kasiyl calls in his debt | Drinax → deep Hierate | clear Kasiyl's name (a clan war) | Kasiyl, a war-judge | Action, Social | — |
| pod-09 | 09 Blood of the Star Dragon | **court intrigue ripens** (spine-succession) | Drinax → Asim | the coup; who rules Drinax | Oleb, Rao, Harrick | Social, Personal, Tension | — |
| pod-10 | 10 Finale | **late empire milestones** (spine-finale) | Drinax / route | declare & defend the Kingdom | recruited worlds, Aslan fleet | Action, Social, Tension | endgame |
| pod-11 | 11 Patrons & Opportunities | **a port/court/Random-Event job** (the most frequent) | all subsectors | ~40 mission seeds → Attitude shifts | varies per seed | varies | varies |
| pod-12 | 12 Gods of Marduk | Maris Enar hires at/near Marduk | Marduk | prove the "sea gods" real | Maris Enar | Mystery, Personal | — |
| pod-13 | 13 Revolution on Acrid | Gera Hollis seeks a forward base | Acrid (Borderland) | arm a revolution → a Haven | Gera Hollis, PRQ | Action, Social | — |
| pod-14 | 14 Friends in Dry Places | Utea's "lordly summons" | Kteiroa | supply a failing ihatei camp | Lord Utea | Social, Tension | — |
| pod-15 | 15 The Cordan Conflict | a Lux rep offers a trivial cargo run | Cordan (Borderland) | a deniable proxy civil war | Baroness Lux | Social, Action | — |
| pod-16 | 16 Lions of Thebus | Lord Ftahkaiw's summons near Thebus | Thebus (Sindal) | rescue a proud, doomed ihatei son | Lord Ftahkaiw | Personal, Tension | — |
| pod-17 | 17 Liberty Port | Free Sperle Society reps approach | Sperle | build a smuggling port vs GeDeCo | Armandie Kern, GeDeCo | Social, Tension | — |
| pod-18 | 18 Shadows of Sindal *(optional)* | drop-in rival-claimant arc | Sindal region | a sinister rival to Oleb's plan | the rival claimant | Mystery, Personal | mini-campaign |

## Travel & sandbox triggers (check during bookkeeping / per jump / per visit)
- **Each jump through patrolled or Amber space** → patrol/Navy detection (`../../references/rules/piracy-raiding.md`, else a Fate Question); or roll `generators/reach_hazard.json`.
- **Crew pick a hunting ground and go raiding** → the commerce-raiding procedure (`../../references/rules/piracy-raiding.md`); roll `generators/prey_ship.json`.
- **Arrive at any world** → its **Attitude** colours reception (`../../references/campaign/empire-reputation.md`); a patron hook (pod-11) may surface (Fate Question / Random Event / `generators/rumour_of_the_reach.json`).
- **Arrive at Theev or another haven** → fencing & black market open (`../../references/rules/piracy-raiding.md`).
- **A Fate-Question doubles ≤ CF with focus on an Adventure Feature** → pull a Reach hazard/opportunity from the Features List.
- **Refuel at a gas giant / wilderness** → skimming + processing risk (`../../references/rules/starship-operations.md`).

## Place → adventure becomes available (not forced)
- Sindalian-treasure hook (from pod-01) → **pod-05**; Sindal ruins → **pod-18** (optional).
- Rumour of a fat, slow prize → **pod-02**. · Aslan ihatei pressure rises → **pod-03** / **pod-14** (Kteiroa/Utea).
- Vorito system → **pod-07**. · An exiled Aslan noble seeks aid → **pod-08**. · Marduk → **pod-12**. · Acrid → **pod-13**.
- Cordan → **pod-15**. · Thebus → **pod-16**. · Sperle/Exe (GeDeCo space) → **pod-17**. · Tech-World → **pod-04**.

## Seed the Lists from all clusters
- **Threads** (objectives): keep Oleb's favour & the marque · make the Harrier pay (raid/trade/survive) · restore or seize the Kingdom · stay ahead of Imperial Heat · read the ihatei tide · + 1–2 personal threads per PC. (`../../references/campaign/seed-lists.md`)
- **Characters**: King Oleb XVI · Princess Rao · the Pirate Lords of Theev · an Imperial naval officer (the law) · an Aslan clan leader / ihatei captain · the crew's char-gen contacts.
- **Adventure Features**: merchant convoys & lone traders · Imperial patrols/customs/Q-ships · gas-giant & wilderness refuelling · Theev · derelicts & salvage · Sindalian ruins & lost tech · Aslan war-fleets & ihatei craft · ion storms/deep-space hazards · rival pirate crews · a rumoured "treasure ship".

## Diminisher (solo scaling): 1/2
> A small pirate crew, not a fleet — scale opposed forces and "the whole sector reacts" beats down by half; the powers
> are vast but rarely bring their full weight against one ship at once. The doom clocks, not raw firepower, are the threat.
