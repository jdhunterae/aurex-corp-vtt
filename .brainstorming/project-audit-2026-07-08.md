# Project Maintenance Audit - 2026-07-08

## Scope

Reviewed:

- `AGENTS.md`
- `README.md`
- `docs/`
- `.project-board/`
- Project structure
- `pyproject.toml`
- `requirements.txt`
- Current implementation under `app/`
- Current tests under `tests/`

No project files were modified except this requested audit report.

Verification run:

```text
.venv/bin/python -m pytest
41 passed
```

## Executive Summary

The project is in good shape for a small local-first Flask app. The implementation has advanced beyond several top-level status documents: tracker model, tracker projection, tracker GM controls, and tracker player rendering are implemented and tested, but `README.md`, `docs/architecture.md`, `docs/roadmap.md`, and `.project-board/mvp-dependencies.md` still describe Phase 3 generic trackers as the next major phase.

The main maintenance need is a documentation and board status refresh, not code churn. The next practical implementation ticket appears to be `P03-005 Add Player Auto Refresh`. After that, `P03-006 Redesign GM Control Layout` and `P02-006 Add Prepared Scene Library` are workflow improvements before Phase 4 initiative/persistence work.

## Current Implementation Snapshot

Implemented and covered by tests:

- Flask app factory and route skeleton.
- GM home, GM session, player display, health, redirects, and 404 handling.
- In-memory session state with project-local session folder bootstrap.
- Public-state projection boundary.
- Scene title, description, image asset selection, and validation.
- App-managed image upload and URL download.
- Duplicate asset preview/reuse/copy behavior.
- App-managed asset serving from `data/sessions/<session_id>/assets/`.
- Generic tracker state, validation, projection, GM controls, adjustment controls, and player rendering.
- Initiative projection helper behavior exists in `app/projection.py`, but initiative state validation, GM controls, and UI are not implemented.

Not implemented:

- Player auto-refresh loop.
- Prepared scene library.
- GM control layout redesign.
- Initiative GM workflow/UI.
- Local save/load persistence and autosave.
- Session listing/creation UI beyond direct session URLs.
- Full GM session JSON endpoint.

## Documentation Drift

### Phase Status Is Outdated

These files still imply Phase 3 generic trackers are next or not yet implemented:

- `README.md`
  - Says "Phase 2 - Scene Display Complete".
  - Says development is ready to begin Phase 3.
  - Lists generic counters and trackers as "next phase".
  - Lists generic tracker GM controls and player rendering as not implemented.
- `docs/architecture.md`
  - Says Phase 3 generic trackers are next.
- `docs/roadmap.md`
  - Says Phase 3 status is "Next".
  - Lists all Phase 3 tickets as initial tickets rather than partly complete.
- `.project-board/mvp-dependencies.md`
  - Says Phase 3 generic tracker tickets are next.

Recommended update:

- Mark Phase 3 as "In Progress" or "Partially Complete".
- Make `P03-005 Add Player Auto Refresh` the current next implementation ticket.
- Mention that tracker model, projection, GM controls, and player display are complete.
- Keep Phase 3 open until player auto-refresh is done, matching the roadmap statement that Phase 3 is not usable until the player display updates automatically.

### Changelog Is Missing Phase 3 Work

`docs/changelog.md` stops at Phase 2. The code and board show substantial Phase 3 work is already done.

Recommended update:

- Add a Phase 3 section for generic tracker model/projection, GM controls, player display, validation, and tests.
- Leave auto-refresh and GM layout redesign out until completed.

### API Documentation Is Mostly Current, But Should Be Rechecked

`docs/api.md` is more current than the README and architecture docs. It correctly says tracker APIs are implemented for Phase 3 and that autosave remains false until persistence exists.

Potential cleanup:

- Ensure the documented tracker route names and response shapes exactly match `app/server.py`.
- Add the currently implemented tracker form routes if the API doc wants to cover page/form behavior, not just JSON endpoints.
- Preserve the distinction between implemented tracker APIs and planned full GM session APIs.

### UI Concepts Are Current Enough, With One Wording Issue

`docs/ui-concepts.md` correctly says player scene and public trackers are implemented and auto-refresh is planned. It also says "Tracker controls: implemented for Phase 3" and then "Phase 3 tracker controls should support", which reads partly historical and partly future-looking.

Recommended update:

- Convert the tracker controls section to "Current tracker controls support..." plus "Remaining workflow gaps..."
- Point remaining workflow gaps at `P03-005`, `P03-006`, and `P02-006`.

## Project Board Audit

### Stale Or Completed Tickets

Done tickets now form the bulk of the board:

- All `p00` tickets are Done.
- All `p01` tickets are Done.
- `p02-001` through `p02-005` are Done.
- `p03-001` through `p03-004` are Done.

These are not wrong, but the board is becoming noisy. Consider an archive convention before the next phase grows.

Recommended archival convention:

- Keep active board tickets under `.project-board/pNN/`.
- Move completed phase folders or completed tickets to `.project-board/archive/pNN/` only when the user explicitly approves.
- Alternatively keep files in place and add `.project-board/active.md` as a concise index of current actionable tickets.

Do not archive yet without approval because `AGENTS.md` currently defines the expected phase folder layout.

### Current Active Tickets

Current actionable tickets appear to be:

- `P03-005 Add Player Auto Refresh` - Ready, highest leverage for table usability.
- `P03-006 Redesign GM Control Layout` - Backlog, depends on auto-refresh.
- `P02-006 Add Prepared Scene Library` - Backlog, still valuable because the current scene workflow is live-entry oriented.
- `P04-001` through `P04-004` - Backlog, phase 4 initiative and persistence.

### Ticket Text Drift

Some Done ticket notes still describe pre-implementation observations:

- `P03-002` says helper coverage is partial and needs Phase 3 work, then also says completed.
- `P03-004` says the current Phase 2 player template renders scene content only, then also says completed.

These are acceptable historical notes but can confuse future agents. Recommended cleanup:

- Move stale "before implementation" observations into a "Historical context" line, or replace them with concise completion notes.

## Project Structure Audit

Current structure is consistent with `AGENTS.md`:

```text
app/
docs/
.brainstorming/
.project-board/
tests/
AGENTS.md
README.md
requirements.txt
pyproject.toml
```

Observed local-only/generated paths:

- `data/`
- `.venv/`
- `.pytest_cache/`
- `__pycache__/`

`.gitignore` covers these adequately:

```text
__pycache__/
*.py[cod]
.venv/
venv/
data/
```

No structural change is required right now.

## Configuration Audit

### `pyproject.toml`

`pyproject.toml` exists but is empty. Pytest still detects it as `configfile: pyproject.toml`.

Options:

1. Remove `pyproject.toml` if no tooling is configured there.
2. Add minimal real configuration, such as:
   - `[tool.pytest.ini_options]`
   - `testpaths = ["tests"]`
   - optionally `pythonpath = ["."]` if needed by future tooling.
3. Move dependency metadata into `pyproject.toml` only if the project deliberately adopts package metadata later.

Recommended now:

- Either delete the empty file or add minimal pytest config. Keeping an empty config file is mildly confusing because tools report it as authoritative even though it contains no settings.

### `requirements.txt`

Current dependencies are minimal:

```text
Flask>=3.0,<4.0
pytest>=8.0,<9.0
```

This matches project constraints. No dependency change is recommended.

## AGENTS.md Audit

`AGENTS.md` is strong and still mostly current. It correctly emphasizes:

- Player projection safety.
- Small phase-based changes.
- Documentation boundaries.
- No frameworks/databases/build tools without approval.
- Boring Python and simple frontend code.
- Test and permission expectations.

Potential updates for newer Codex capabilities:

- Add a short instruction that broad audits should be saved under `.brainstorming/project-audit-YYYY-MM-DD.md` when the user asks for a maintenance audit. This matches the current request and avoids filename ambiguity.
- Add guidance for using current Codex tool strengths without changing project scope:
  - Prefer `rg` for repo searches.
  - Run focused tests after implementation.
  - Use local planning/checklist tools when the task is multi-step.
  - Do not use web access unless the task needs current external facts.
- Add a convention for generated audit reports:
  - Include verification commands run.
  - Separate recommended changes from changes actually made.
  - Include "no files modified except report" when applicable.

Do not overfit `AGENTS.md` to a specific Codex UI or tool name. Keep it agent-agnostic where practical.

## Missing Documentation Or Conventions

Recommended additions:

- `docs/developer-setup.md` or a README section for:
  - Python version expectations.
  - Virtualenv setup.
  - Test command.
  - Run command.
  - Runtime data behavior under `data/sessions/`.
  - How to clear local runtime data safely.
- A board maintenance convention:
  - What "Ready" means.
  - Whether Done tickets remain in phase folders or move to archive.
  - How to identify the current active ticket.
- A lightweight route/API convention:
  - Page/form routes use `/s/<session_id>/gm/...`.
  - JSON GM routes use `/api/gm/session/<session_id>/...`.
  - Player JSON routes must use `/api/s/<session_id>/public`.
- A frontend convention:
  - Player JavaScript may consume only the public projection endpoint.
  - GM JavaScript may call GM endpoints but must not be loaded on player pages.
- A persistence convention before P04-004:
  - How autosave responses should transition from `autosaved: false` to real autosave metadata.

## Duplicate Or Contradictory Documentation

The docs intentionally overlap in places. The overlap is manageable, but status duplication is causing drift.

Duplicated status appears in:

- `README.md`
- `docs/architecture.md`
- `docs/roadmap.md`
- `docs/ui-concepts.md`
- `.project-board/mvp-dependencies.md`
- individual tickets

Recommended simplification:

- Make `docs/roadmap.md` the only phase-status source of truth.
- Let `README.md` summarize current status in one short paragraph and link to `docs/roadmap.md`.
- Let `.project-board/mvp-dependencies.md` describe dependency order, not current completion status.
- Keep detailed implementation status inside tickets and `docs/changelog.md`.

## Workflow Simplification Opportunities

- Add a concise "Current Work" section to `docs/roadmap.md` pointing to exactly one or two active tickets.
- Add `.project-board/active.md` instead of scanning all phase folders.
- Decide whether `pyproject.toml` should be removed or made useful.
- Update README "Current Status" after each completed phase or substantial phase milestone.
- Use `docs/changelog.md` as the durable completion log instead of repeating completion details across README and ticket notes.

## Safety Boundary Notes

No obvious player-state safety documentation regressions were found.

Current implementation appears aligned with the core rule:

- Player route renders `public_state`.
- Public JSON route returns `project_public_state`.
- Scene asset projection exposes app-managed asset URL only.
- Tracker projection omits hidden trackers and does not expose `gm_notes`.
- Asset upload/download responses use a public asset response helper rather than returning full private asset source metadata.

One future concern:

- The player template currently renders initial state server-side and has `data-public-state-url`, but no player JS loop. `P03-005` must preserve the projection boundary by fetching only `/api/s/<session_id>/public`.

## Recommended Next Maintenance Patch

If approved, make a documentation-only maintenance update:

1. Update README current status to Phase 3 in progress.
2. Update `docs/architecture.md` current implementation status.
3. Update `docs/roadmap.md` Phase 3 status and checked deliverables.
4. Add Phase 3 completed tracker work to `docs/changelog.md`.
5. Update `.project-board/mvp-dependencies.md` current development position.
6. Clarify stale wording in `P03-002` and `P03-004`.
7. Decide and apply either removal of empty `pyproject.toml` or minimal pytest config.

Recommended after that:

1. Implement `P03-005 Add Player Auto Refresh`.
2. Then revisit `P03-006` and `P02-006` for GM workflow quality.
3. Then begin Phase 4 initiative with `P04-001`.

