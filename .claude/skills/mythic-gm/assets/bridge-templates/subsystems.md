# World Subsystems — <Setting>   (hook: world-tick; fired by tick.py at bookkeeping)
> **Operative digest:** <RUN `tick.py --bridge <b> --campaign <c>` EVERY bookkeeping; advance each DUE clock by
> rolling its table and record it to state. These run whether or not the PC acts — skipping silently stalls the sandbox.>
| subsystem        | cadence          | advance by |
|------------------|------------------|-----------|
| <War Front clock>| every scene      | tick +1; at full → roll <table> |
| <Salvage economy>| every scene      | draw 1 on <table> |
| <Faction move>   | every 3 scenes   | roll <faction.json> + a Move Toward/Away a Thread |
