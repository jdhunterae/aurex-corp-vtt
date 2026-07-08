# AI Playbooks

This directory contains standard operating procedures for recurring AI-assisted project workflows.

Playbooks are written for Codex and other AI agents. They are not general human documentation, brainstorming notes, tickets, or copy/paste prompt collections.

## Purpose

Use playbooks to make repeated project workflows more reliable.

A playbook should explain:

- When the workflow applies
- What the agent should inspect
- What the agent should produce
- What the agent should avoid
- When the agent should ask for approval

## Current Playbooks

### `session-start.md`

Use at the beginning of a new work session to establish context, identify the current phase or ticket, and produce a brief before making changes.

## Relationship to Other Project Areas

- `AGENTS.md` defines global agent rules and safety expectations.
- `.ai-context/` contains stable AI guidance and project knowledge.
- `.project-board/` contains phase-based tickets.
- `.brainstorming/` contains temporary analysis, audits, and rough planning notes.
- `docs/` contains stable human-facing project documentation.

## Adding New Playbooks

Create a new playbook only when a workflow has become repeated and stable.

Good candidates:

- Phase closeout
- Release preparation
- Bug investigation
- Documentation review
- Feature planning
- Project-board cleanup

Avoid creating a playbook for one-off tasks or speculative workflows.
