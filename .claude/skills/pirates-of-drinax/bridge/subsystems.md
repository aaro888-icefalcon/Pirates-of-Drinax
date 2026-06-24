# World Subsystems — Trojan Reach   (hook: world-tick; fired by tick.py at bookkeeping)

> `python3 ../../mythic-gm/scripts/tick.py <campaign-or-bridge-dir> <scene#>` reports which rows are DUE (and which
> need a trigger check); the engine then advances each by rolling its named table / ticking its clock and records the
> result to campaign state. These are the Reach's living pressures — they run whether or not the crew act.
> Mechanics live in the cited references; this registry only schedules them.

> **Operative digest:** RUN `tick.py --bridge <bridge> --campaign <campaign>` AT EVERY BOOKKEEPING STEP — it reads the
> scene # from adventure.json and reports DUE rows; advance each by rolling its table / ticking its clock and WRITE the
> result to campaign-state. These clocks (Imperial Heat, ihatei, Drinax decay, rival pirates, PRI, Standing, tithe) run
> whether or not the crew act — skip the tick and the whole sandbox silently stalls. It prints "(nothing due)" when idle, so its absence is conspicuous.

| subsystem | cadence | advance by |
|---|---|---|
| Imperial Heat | on trigger: a big or near-Drinax raid, an atrocity, or exposure | +1 box; at 5 boxes → **06 Game of Sun & Shadow** goes live (Navy sweep). Check monthly with `dice.py keyed 1d10 <target>`. (`../references/rules/piracy-raiding.md`) |
| Aslan ihatei pressure | every 4 scenes | +1 box (raids/noise on the Aslan border add more); at full → **03 Ihatei!** invasion window opens (hard 25-week clock). (`../references/setting/factions.md`) |
| Drinax decay & succession | every 6 scenes | +1 box (court strife adds more); at full → **09 Blood of the Star Dragon** (Harrick/Rao rift detonates). (`../references/setting/drinax.md`) |
| Rival pirates | every 3 scenes | a rival band advances its plan — roll `generators/rumour_of_the_reach.json` or `generators/reach_hazard.json`, or a Mythic Move Toward a Thread; a uniting corsair warlord is a standing threat. |
| PRI — regional piracy response | every scene | no raid in-region this scene → decay −1; each raid → +1D and feeds watch lists; spikes summon Q-ships / 2D×500t task forces. (`../references/rules/piracy-raiding.md`) |
| Offscreen / patron clocks | every scene | advance any active timed adventures: Treasure Ship (12-week), Ihatei! (25-week), Game of Sun & Shadow (months), and patron deadlines — regardless of detours. |
| World Attitude review | on trigger: arrive at or act at a world | apply earned step-shifts toward/away Haven for what the crew actually did; recompute recruitment Final DMs. (`../references/campaign/empire-reputation.md` · live tracker in `campaign/reputation-tracker.md`) |
| Great-power Standing | on trigger: a raid or heroic deed resolves | adjust Imperium / Hierate Standing; hitting the *other* power's ships is a Heroic Deed (+1D with the pleased power); crossings at 20+ / −40+ re-rate that power's ports. (`../references/rules/piracy-raiding.md`) |
| Drinax tithe | on trigger: takings banked | Oleb takes **10% of all takings**; refusing/forgetting risks forfeiting the letter of marque and making an enemy of Drinax. |

## Notes
- "every scene" / "every N scenes" rows fire automatically; "on trigger" rows surface for the GM to judge against the
  scene's fiction. Advance honestly — never skip a tick because it's inconvenient for the crew.
- Three of these (Imperial Heat, ihatei pressure, Drinax decay) are the campaign's **doom clocks**; surface their state
  in `campaign/campaign-state.md` every scene (the ▢▢▢▢▢ tracks).
