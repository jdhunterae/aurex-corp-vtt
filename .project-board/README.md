# Project Board

This folder stores local markdown tickets organized by development phase.

Use `active.md` as the quick entry point for current work. Phase folders remain the source of truth for full ticket details and acceptance criteria.

Phase folders use `pNN` names:

- `p00` — Phase 0, project planning and architecture
- `p01` — Phase 1, application skeleton
- `p02` — Phase 2, scene display
- `p03` — Phase 3, generic trackers
- `p04` — Phase 4, initiative tracker

Suggested ticket filename style:

```text
p01-001-short-title.md
```

## Status Values

- `Backlog`: planned but not ready to work immediately.
- `Ready`: ready to implement when the current active work is complete.
- `In Progress`: currently being worked.
- `Blocked`: cannot proceed until a stated dependency or decision is resolved.
- `Done`: completed and retained for history.

## Maintenance Conventions

- Keep tickets in their phase folders unless the user explicitly approves an archive move.
- Do not move completed tickets to an archive by default.
- Update `active.md` when the current ticket changes, when a ticket moves to `Done`, or when phase priorities change.
- Keep `active.md` concise. Put detailed scope, acceptance criteria, and notes in the ticket files.
- Use `docs/roadmap.md` as the phase source of truth when adding new phase folders or changing phase names.
