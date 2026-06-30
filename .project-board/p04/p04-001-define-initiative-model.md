# P04-001 Define Initiative Model

## Status

Backlog

## Phase

Phase 4 - Initiative Tracker

## Goal

Define the initiative data model and visibility rules for combat management.

## Acceptance Criteria

- [ ] Combatant fields are documented.
- [ ] Visible versus hidden combatants are defined.
- [ ] Overall initiative visibility behavior is documented.
- [ ] Hidden overall initiative display removes the player-facing panel entirely.
- [ ] Per-combatant visibility behavior is documented.
- [ ] Per-combatant hidden, visible, and known states are documented.
- [ ] AC visibility behavior is documented.
- [ ] AC reveal is documented as per-combatant, not global enemy type state.
- [ ] HP visibility modes are documented.
- [ ] Global discovered HP number display configuration is documented.
- [ ] Vibe health thresholds are documented.
- [ ] Current turn and ordering behavior are documented.
- [ ] Non-creature initiative row behavior is documented.
- [ ] Public non-creature rows expose only title/name and initiative slot number plus technical rendering fields.
- [ ] Unrevealed monsters and GM-only combat notes are excluded from public payloads.

## Notes

Depends on P00-002 and P00-003. Initiative needs an overall hidden toggle and per-combatant player visibility states. When overall initiative is hidden, the player UI should show no initiative panel, blank space, or placeholder. `hidden` means no row is shown. `visible` means the row is shown with `???` replacing hidden data except initiative slot/speed. `known` means name and discovered information are shown. AC is hidden by default with per-combatant reveal support. MVP does not need global enemy-type AC reveal behavior. HP visibility modes are none, vibe, and numbers. Vibe bands are healthy at 70% or higher, injured from 50% to 70%, and seriously injured/bloodied below 50%. HP number display style should be a global GM configuration defaulting to current/max, such as `20/56`. Initiative should support non-creature rows such as lair actions, environmental effects, pets, companions, vehicles, and similar turn-order entries. Public non-creature rows expose only title/name and initiative slot number plus technical rendering fields such as ID, kind, and current-turn status.
