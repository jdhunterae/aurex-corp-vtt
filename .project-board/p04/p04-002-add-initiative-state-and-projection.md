# P04-002 Add Initiative State and Projection

## Status

Backlog

## Phase

Phase 4 - Initiative Tracker

## Goal

Add initiative state and public projection behavior.

## Acceptance Criteria

- [ ] Initiative state matches the documented model.
- [ ] Public projection respects the overall initiative hidden toggle.
- [ ] Public projection omits the initiative panel entirely when overall initiative is hidden.
- [ ] Public projection includes only visible initiative entries.
- [ ] Public projection omits `hidden` combatants.
- [ ] Public projection shows `visible` combatants with `???` for hidden data except initiative slot/speed.
- [ ] Public projection shows `known` combatants with discovered information.
- [ ] Public projection hides AC unless revealed.
- [ ] Public projection applies HP visibility mode.
- [ ] Public projection applies global discovered HP number display configuration.
- [ ] Public projection defaults discovered HP number display to current/max.
- [ ] Public projection derives vibe health bands without exposing hidden HP numbers.
- [ ] Public projection supports non-creature initiative rows.
- [ ] Hidden or unrevealed combatants are excluded from player-facing payloads.
- [ ] Projection behavior is covered by unit tests.

## Notes

Depends on P04-001 and P01-004.
