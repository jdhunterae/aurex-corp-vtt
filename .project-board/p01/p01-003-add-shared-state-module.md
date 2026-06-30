# P01-003 Add Shared State Module

## Status

Backlog

## Phase

Phase 1 - Application Skeleton

## Goal

Implement an in-memory shared state module for the MVP.

## Acceptance Criteria

- [ ] Initial state shape follows `docs/state-model.md`.
- [ ] A default local session can be created or loaded for skeleton use.
- [ ] Project-local `data/sessions/<session_id>/` layout is bootstrapped for MVP development.
- [ ] Backend code owns canonical state.
- [ ] State access is explicit and testable.
- [ ] State is associated with an active foldered session.
- [ ] State module exposes clear functions for create/load/get/update active session state.
- [ ] No private state is passed directly to player routes.
- [ ] Persistence beyond basic session bootstrap is deferred to Phase 4 save/load tickets.

## Notes

Depends on P00-002 and P01-001.

Keep this module boring and in-memory first. Phase 1 only needs enough state to support page routes, public projection, and tests.
