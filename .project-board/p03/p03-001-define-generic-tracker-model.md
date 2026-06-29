# P03-001 Define Generic Tracker Model

## Status

Backlog

## Phase

Phase 3 - Generic Trackers

## Goal

Define a reusable tracker model that can support round counters, timers, countdowns, and party gold without one-off implementations.

## Acceptance Criteria

- [ ] Tracker fields and allowed tracker types are documented.
- [ ] Bounded and unbounded tracker modes are documented.
- [ ] Numeric scale tracker behavior is documented.
- [ ] Optional named value mapping is documented.
- [ ] Interval mapping behavior is documented.
- [ ] Player display mode options are documented.
- [ ] Display mode names are documented: number, label, label_color, number_label.
- [ ] Default tracker color scales are documented.
- [ ] Custom per-state tracker colors are documented as stretch unless promoted.
- [ ] Step control behavior is documented.
- [ ] Public/private visibility rules are documented.
- [ ] Update validation rules are documented.
- [ ] Tracker examples from the roadmap can be represented by the model.

## Notes

Depends on P00-002 and P00-003. Trackers are usually numeric, but may be bounded or unbounded and may map numeric ranges to named states. Example: a security tracker with values Green, Yellow, Orange, Red, Black and interval 3 maps 1-3 to Green, 4-6 to Yellow, and so on. GM should be able to hide raw numeric progress from players and show only the mapped text/color value. Default color scales should include green-to-red, red-to-green, black-to-white, and white-to-black. Custom color picker per state is a stretch goal unless promoted into MVP. Controls should always include default -1/+1 buttons and may include larger interval-derived or GM-configured step buttons.
