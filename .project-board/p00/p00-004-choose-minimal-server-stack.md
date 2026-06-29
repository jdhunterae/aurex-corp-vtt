# P00-004 Choose Minimal Server Stack

## Status

Ready

## Phase

Phase 0 - Project Planning and Architecture

## Goal

Choose the minimal Python server approach for the local server MVP.

## Acceptance Criteria

- [ ] The selected server library or standard-library approach is documented.
- [ ] Any dependency addition is justified before implementation.
- [ ] Startup command and development workflow are documented.
- [ ] The choice supports templates, static assets, JSON routes, and unit tests.
- [ ] The choice does not require handing canonical game state management to a framework ORM or database layer.

## Notes

Current docs say "Python web server" but do not choose a framework or standard-library server. Flask or Django can be considered if they speed up routing/templates, but the project should keep its own backend data model.
