# Prompt Library Context

Purpose: provide concise reusable prompts for future AI-agent sessions without making them binding project requirements.

## Before Implementing A Ticket

```text
Read AGENTS.md, .ai-context/, docs/roadmap.md, .project-board/active.md, and the target ticket. Identify the roadmap phase, summarize the safety boundary, then implement only the requested ticket scope.
```

## Player-Safety Review

```text
Review this change for player-state leaks. Check player routes, public JSON, player templates, static JavaScript, and tests. Confirm hidden GM notes, local paths, original asset URLs, hidden trackers, hidden combatants, hidden AC/HP, keys, tokens, and private save metadata are not exposed.
```

## Documentation Sync

```text
Compare the implementation against README.md, docs/roadmap.md, docs/changelog.md, docs/api.md, docs/state-model.md, docs/ui-concepts.md, and .project-board/active.md. Update only stale or contradictory project materials.
```

## New Feature Test Checklist

```text
Before finishing, identify focused tests for projection safety, route/API behavior, validation errors, and user-visible rendering. Run .venv/bin/python -m pytest and summarize results.
```

## Phase 3 Auto-Refresh Guardrails

```text
Implement player auto-refresh using only public projection payloads. Player JavaScript must fetch /api/s/<session_id>/public or another explicit public projection endpoint only. Do not call GM APIs or expose full session state.
```

## Maintenance Audit

```text
Audit AGENTS.md, README.md, docs/, .project-board/, pyproject.toml, requirements.txt, app/, and tests/. Save findings to .brainstorming/project-audit-YYYY-MM-DD.md. Separate findings from proposed changes and do not modify project files unless approved.
```

TODO: Add project-specific prompts as recurring workflows become clearer.
