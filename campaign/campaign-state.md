# Campaign State — Pirates of Drinax (solo)

> SOURCE OF TRUTH. Overwrite at the end of every scene. Engine = mythic-gm; content = pirates-of-drinax. In-fiction date: **~1105–06** (Phase 2; touring the Reach courting independent worlds — currently at **Paal**).

> ▶ **RESUME HERE (next session):** The crew are aboard the Harrier at Paal, the pitch **WON**. Shake's partnership argument landed (Persuade **12** vs Difficult 10, **Effect +2 — Average Success**): **Magnate Ivo Sarrel commits his centrist swing-bloc** to championing the partnership case, *favourably*. With **Matron Avelline (pro-Drinax) + the centre**, Drinax now has a **council majority in waiting** — **Paal shifted Suspicious → Neutral** (winnable; not yet recruited — that's the Finale). Sarrel is a **conditional** ally ("don't make me a fool for it"); **GeDeCo's bid stalled but is NOT beaten** and will counter harder (its pitch was "protection, not partnership" — it just lost the centre). **Chaos Factor → 1.** Next: it's the **player's move** — consolidate Paal (formal council vote / lock in Avelline+Sarrel / brace for GeDeCo's counter), or break off toward live threads (the **corsair warlord massing on Pourne** = danger + key to winning Pourne; honour the **Clarke defence pact** → Haven; report-in / raiding income; GeDeCo's overdue counter-stroke). Awaiting "What do you do?"

## Engine state (mythic-gm)
- **Chaos Factor:** 1  *(crew controlled the Paal pitch completely; world very predictable — push the advantage or expect the dice to inject tension soon.)*
- **Engine:** mythic-gm **v2** (JSON-backed Lists). **Threads/Characters/Adventure config now live in `threads.json` / `characters.json` / `adventure.json`** — the dice roll *those* (any length, two-stage roll). The Lists below are a human-readable **snapshot**; edit via `state.py thread|char add|weight|remove|show campaign "<name>"`. Roll the loop with `--campaign campaign` (e.g. `dice.py fate <odds> <CF> --campaign campaign`, `oracle.py event --campaign campaign`, `adventure_crafter.py turning-point --campaign campaign --existing`); new NPCs auto-fire `oracle.py character --campaign campaign --bridge .claude/skills/pirates-of-drinax/bridge` (AC Crafter + `npc_role.json`, conjunction).
- **Adventure Source mode:** Prepared Adventure (sandbox) → **Phase 2 (Raiding & Empire-Building) now open.**
- **Discipline:** HARDCORE — honest scripted dice, pre-committed stakes, no softening, Peril Points OFF; Player ≠ PC knowledge (adventures spoiler-gated).
- **Current adventure:** **Phase 2 — Building the Kingdom (sandbox).** Allies: **Torpol (Friendly)**, **Clarke (Friendly, held; owed a defence → Haven)**. **At Paal (0805) — pitch WON, world now Neutral & council winnable.** Won pro-Drinax **Matron Sera Avelline** (free) + **Magnate Ivo Sarrel's centrist swing-bloc** (Persuade roll, Effect +2) = a **majority in waiting**. Open threads: lock in Paal's council (formal vote) vs GeDeCo's coming counter; defend Clarke (pact → Haven); the **corsair warlord massing to sack Pourne** (a danger + the key to winning the Pourne fortress); GeDeCo rivalry (3× beaten, overdue a hard counter).
- **Last scene recap (current):** At **Paal**, Shake delivered his fear-addressing partnership pitch to **Magnate Ivo Sarrel** and **won the roll** (Persuade 1 + SOC + Diplomatic Suite, Boon for Reyna + the argument = 12 vs Difficult 10, Effect +2). Sarrel — a hedging centrist to the marrow — committed to championing the partnership case to his bloc, noting GeDeCo had offered Paal "protection, not partnership" ("like a granary protects its grain — for the harvest"), while Shake at least admitted the war is real. He gave his hand, *conditionally*: "Don't make me a fool for it. GeDeCo won't take the centre slipping quietly." **Paal: Suspicious → Neutral; council majority in waiting (Avelline + the centre). Chaos 2 → 1.**
- **Last scene recap (prior):** Worked Paal's power players. Allied freely with **Matron Sera Avelline** (pro-Drinax old-blood). Mapped the council as a quarrelsome oligarchy; identified **Magnate Ivo Sarrel** as the centrist swing-bloc leader and hosted him aboard. A social read (10 vs 8) opened him up; oracle gave his wants as **Waste · Prison** (fears Paal reduced to a vassal *prison*, or *wasted*/bombed to slag in an empire's war as under Oleb XIV's tax-war). Shake answered both: war is coming regardless; can't promise no war, but promises to meet it **together, as equal partners, back-to-back, not as sacrifices.**
- **Last scene recap:** Saved Clarke from GeDeCo's poison (protector pact). Scouted **Pourne** — a paranoid Imperial-leaning fortress, no diplomatic angle, but bar-gossip revealed it's bracing against a **gathering corsair warlord's fleet** that means to sack it (irony: Pourne fears pirates, and the crew fly privateer colours). Refueled, then jumped clean to **Paal** to court a warmer, old-Drinax-tied world.
- **Last scene recap:** Stun-capture of Miria went sideways (weak stun 4 < END 8) but the team subdued her by force (10 vs 10); disarmed her cyberarm's hidden suicide-bomb (a near-miss that vindicated the no-shooting capture). Pulled the *Mercifuge* nav logs on her codes (Sal 10) → Ferrik on Palindrome's 4th moon. Interrogated her (Reyna+Shake 15, Effect +5): she broke completely and offered to **bait Ferrik** into a trap for "the right consideration."
- **Last scene recap:** Shake ordered the launch for Clarke. Refined fuel, but the still-wayward J-drive (DM−1) threw the jump — Astrogation check failed (Effect −3) → **misjump**: flung 5 parsecs coreward into Sindal subsector, pulled out at **Borite (0609)**. Costs: hull 51→42/88 (cracked frames), **all jump fuel spent**, drive held but unverified, ~1 week gone, badly off-mission in lawless space near Theev. Chaos Factor 4→5.

### Threads List & Characters List → see generated `campaign/LISTS.md`
> **JSON-backed (v2):** `threads.json` / `characters.json` are the machine source the dice roll; the live, annotated
> view is **`campaign/LISTS.md`** (generated by `state.py render`, auto-updated on every mutation — do NOT hand-maintain
> a second copy here). Manage via `state.py thread|char add|weight|note|remove campaign "<name>"`.
> Current: **13 active Threads** (resolved *Win Tashan's wager* & *Run down Ferrik* dropped) · **19 Characters**
> (Ferrik removed — dead). Theme priority Action · Social · Tension · Mystery · Personal · scene #12.

### Adventure-Features List
- Merchant convoys & lone traders (prey) · Imperial patrols / customs / Q-ships (law/traps) · Gas-giant & wilderness refuelling · Theev (lawless pirate port) · Derelicts & salvage · Sindalian-era ruins & lost tech · Aslan war-fleets & ihatei craft · Ion storms / deep-space hazards · Rival pirate crews · A rumoured "treasure ship."

## Crew
- **PC:** Abhishek "Shake" Rao — **Captain & ship's surgeon** — unharmed — Medic 3, Leadership 1, Tactics(naval) 1; ~Cr22,500, 0 Ship Shares (spent). (Full sheet: `character-sheet-shake.md`.)
- **NPC crew (morale/loyalty all steady at start):**
  - Reyna Voss — First Officer / pilot / Face / court liaison
  - Dak Surrow — Pilot / Astrogator / Sensors
  - Mira Kell — Chief Engineer
  - Brakk — Lead Gunner / boarding leader
  - Sal Quist — Boarder / Quartermaster / 2nd gunner / fence
  - Doc Hadrian — Medic / Steward
  - **Krrsh** (NEW — rescued at Borite) — Vargr Pilot/Gunner/comms; Pilot 2, Gunner 2, Electronics(comms) 1, Astrogation 1, Engineer(j-drive) 1, Streetwise 2. Not bright, broken, fiercely devoted to Shake who saved him. Knows the Theev routes.
- **Letter of marque:** granted (good standing). Tithe to Oleb: **10% of all takings.**

## The Harrier (full log: harrier-ship-log.md)
- **Fully restored & upgraded** — hull **88/88**, **all defects cleared** (running costs normal; M-drive & J-drive sound, no misjump; ventral **triple pulse-laser turret, ALL-ARC** = point-defence; cosmetics restored → **Diplomacy DM+1/+2**). Added **Mission Pod: Diplomatic Suite** (Diplomacy DM+1; −10t cargo). The gifted wreck is now a proper warship + a courting platform.
- At **Drinax (Royal Docks)**, fueled, jump-true. **Ship Shares: 0.**
- **CARGO: salvaged exotic Sindalian alloy (~5–6 SRU-equivalent)** — enough to **properly restore the hull to 88** at a yard (the fix TL11 couldn't do) + surplus (rebuild the ventral turret and/or sell — exotic alloy is near-priceless). Theev's Kallos Shipyards (TL15) could do the work.

## Finances & plunder
- Cash: **~Cr1.0M** (~Cr2.44M − ~Cr1.4M full refit at the Royal Docks). Still a solid war chest. **Monthly maintenance now normal (~Cr2,657/mo)** + 10% tithe on takings.
- **Monthly costs:** Harrier maintenance ~Cr5,314/mo (doubled until repaired) + tithe on takings.
- Cargo/loot: none.

## Empire / Reputation (full table: reputation-tracker.md)
- Worlds recruited: 0 (Finale mechanic) · Fighting Strength pledged: Torpol FS 3 (uncommitted).
- Drinax = Haven (home). Theev = Friendly (Darokyn's goodwill kept — his wish honored). **Torpol = Friendly (↑+3, first true ally)**, **Clarke = Friendly (held; pact → Haven)**, **Paal = Neutral (↑+1, council majority in waiting — Avelline + Sarrel's bloc)**. Borite = Suspicious (goodwill seed). Pourne = Suspicious (no angle yet; corsair-warlord saviour hook).
- Drinax court: Oleb favourable; Rao's scheme on trial; Lord Wrax opposed (his client Tashan publicly bested by Shake at dinner — minor face won for the privateer scheme, fresh grudge from the Wrax faction).

## Heat & sandbox clocks
> Reconciled at **scene #12** after restoring the world-tick discipline (these had silently stalled; `tick.py --bridge … --campaign campaign` now fires every bookkeeping). Values reflect established Phase-2 fiction, not new rolled events — fresh advances roll in play from here.
- **Imperial Heat:** ▢▢▢▢▢ (0/5 — pure diplomacy in Phase 2; no big raid/atrocity/exposure → trigger never fired) (→ 06 Game of Sun & Shadow / naval hunt)
- **Aslan ihatei pressure:** ▣▣▢▢▢ (2/5 — the tide keeps rising offscreen; every-4-scene cadence)
- **Drinax decay / succession:** ▣▢▢▢▢ (1/5 — court strife simmers: Wrax faction, the foreshadowed Harrick/Rao rift) (→ 09 Blood of the Star Dragon)
- **Rival pirates:** ▣▣▢▢▢ (2/5 — the corsair warlord uniting raider bands to sack Pourne IS this clock advancing)

## Adventures
- **In play:** 01 Honour Among Thieves — **RESOLVED in the field** (Ferrik dead, bounty collected, Torpol/Clarke won). **Final step: report to King Oleb at Drinax** → fully closes the opener.
- **Permanent bonus earned:** completing the opener → **DM+1 to ALL Finale recruitment rolls** (empire game).
- **Completed:** (01 pending the Drinax report).
- **Open threads/seeds:** Darokyn's secret (Imperial Intelligence — known to the crew, proof still on his flagship; dormant blackmail/heist hook); the lost Sindalian crown jewels (Borite painting); the Theev safe-code + fuel-dump (recurring access). **Phase 2 (raiding & empire-building sandbox) opens after the report.**

## Open canon questions answered in play
- **Borite system has a skimmable gas giant** (Fate Q, Likely → Yes) — usable wilderness refuelling point in-system.
- The Star Ray raider that worked Borite's granary run had **no clean transponder / unknown backer**; Korr (local) doesn't know who sent it. (Likely a freelance Sindal raider, not the opener's Ferrik — unconfirmed.)
