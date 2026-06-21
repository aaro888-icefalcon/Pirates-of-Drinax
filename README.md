# Pirates of Drinax — solo / GM-less campaign

A self-contained setup for playing **Pirates of Drinax** (Mongoose Traveller
2e, in the Trojan Reach) **solo or GM-less**, with Claude Code acting as the
Game Master.

> You're a pirate crew with a royal letter of marque and an ancient warship, the
> *Harrier*. Raid the shipping lanes of the Reach, build alliances, and — maybe —
> win back the crown of Drinax.

## How it works

Two [Claude Code skills](https://code.claude.com/docs) (installed under
`.claude/skills/`) do the work:

- **`mythic-gm`** — the **engine**. Runs the play loop, rolls every die honestly
  through Python scripts, asks the Mythic oracle, fires Random Events, and
  enforces a strict no-softening discipline.
- **`pirates-of-drinax`** — the **content pack**. The Traveller 2e ruleset, the
  Trojan Reach setting and worlds, the Harrier, the piracy & empire-building
  subsystems, and spoiler-gated breakdowns of every set adventure. It layers
  onto the engine.

[`CLAUDE.md`](CLAUDE.md) tells Claude how to drive both.

## Play

Open this repo in Claude Code and say, e.g.:

> *"Let's play Pirates of Drinax solo."*

Claude runs **Session Zero** — builds your crew, assigns the Harrier, seeds the
sandbox, and opens with *Honour Among Thieves*. Already started? It reads
`campaign/campaign-state.md` and picks up where you left off.

Your live game lives in [`campaign/`](campaign/). The container is ephemeral, so
**commit and push `campaign/` to keep your progress** between sessions.

## Requirements

- Claude Code (the two skills are bundled in this repo)
- Python 3 (for the engine's dice/oracle scripts — already available in the
  cloud environment)

## Attribution / personal use

Traveller © Mongoose Publishing / Far Future Enterprises. *Pirates of Drinax* and
the *Drinaxian Companion* © Mongoose Publishing. *Mythic Game Master Emulator 2e*
and *The Adventure Crafter* © Tana Pigeon / Word Mill Games. Bundled source text
consists of the user's own converted copies, included for personal use.
