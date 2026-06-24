# Theme Weights — Pirates of Drinax   (hook: themes; FIXED for the whole campaign)
> **Operative digest:** PoD is an Action+Social engine (raid/board/chase + court/diplomacy/empire) — those two
> dominate Turning Points, with Tension, Mystery, Personal underneath. Roll an adventure's 5 Theme priorities with
> `adventure_crafter.py themes --style action --campaign <dir>` (the closest built-in to these weights), or set them
> explicitly: `state.py adventure set-themes <dir> Action,Social,Tension,Mystery,Personal`.
> (NB: the `themes` command does not yet read these bridge weights directly — use --style or set-themes.)
# Every adventure rolls its 5 Theme priorities from these weights
# (python3 ../../mythic-gm/scripts/adventure_crafter.py themes, weighted by these).
# PoD blends two engines in roughly equal measure: ACTION (raiding, boarding, ship combat, the chase) and
# SOCIAL (court intrigue at Drinax, diplomacy, recruiting worlds, the empire game). Tension (Heat, the ihatei
# clock, being hunted) and Mystery (Sindal ruins, GeDeCo conspiracies, lost tech) ride underneath; Personal
# (crew loyalty, the crown, an outsider earning a place) gives it heart.
Action: 2
Tension: 1
Mystery: 1
Social: 2
Personal: 1
# Optional fixed First-Priority theme:
first_priority: none
