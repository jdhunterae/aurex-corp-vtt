# P03-001 Define Generic Tracker Model

## Status

Backlog

## Phase

Phase 3 - Generic Trackers

## Goal

Review and finalize the reusable tracker model draft so it can support round counters, timers, countdowns, and party gold without one-off implementations.

## Acceptance Criteria

- [ ] Tracker fields and supported use cases are documented without introducing one-off tracker types.
- [ ] Bounded and unbounded tracker modes are documented.
- [ ] Numeric scale tracker behavior is documented.
- [ ] Optional named value mapping is documented.
- [ ] Interval mapping behavior is documented.
- [ ] Player display mode options are documented.
- [ ] Display mode names are documented: number, label, label_color, number_label.
- [ ] Default tracker color scales are documented with concrete display colors or a clear derivation rule.
- [ ] Custom per-state tracker colors are documented as stretch.
- [ ] Step control behavior is documented.
- [ ] Public/private visibility rules are documented.
- [ ] Update validation rules are documented.
- [ ] Planned Phase 3 route/UI surface is documented or confirmed against `docs/api.md` and `docs/ui-concepts.md`.
- [ ] Tracker examples from the roadmap can be represented by the model.

## Notes

Depends on P00-002 and P00-003.

`docs/state-model.md` already contains a tracker model draft. This ticket should confirm, tighten, and fill gaps in that draft rather than create a competing model.

Trackers are numeric at the canonical state level, but may be bounded or unbounded and may map numeric ranges to named public states. Example: a security tracker with values Green, Yellow, Orange, Red, Black and interval 3 maps 1-3 to Green, 4-6 to Yellow, and so on. GM should be able to hide raw numeric progress from players and show only the mapped text/color value. Default color scales should include green-to-red, red-to-green, black-to-white, and white-to-black. Custom color picker per state is a stretch goal. Controls should always include default -1/+1 buttons and may include larger interval-derived or GM-configured step buttons.
