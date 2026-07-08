# AI Context

This directory contains long-lived guidance intended for AI assistants working within this repository.

Unlike `docs/`, which is primarily human-facing project documentation, `.ai-context/` is optimized to preserve stable project knowledge across AI sessions and reduce repeated prompting.

The information here should be concise, practical, and grounded in the current project. Do not use this directory for speculative notes, temporary analysis, or broad brainstorming. Use `.brainstorming/` for that.

## Contents

### `architecture.md`

Stable notes about the application's architecture, major components, state ownership, and important design boundaries.

### `terminology.md`

Shared vocabulary for the project, including domain terms, UI names, tracker concepts, and any project-specific language that should be used consistently.

### `ui-conventions.md`

Guidance for GM-facing and player-facing UI behavior, layout priorities, readability expectations, and interaction patterns.

### `coding-style.md`

Project coding conventions, preferred patterns, module organization, naming, dependency expectations, and implementation style.

### `testing.md`

Testing expectations, known test commands, fixture conventions, manual verification steps, and areas that need additional test coverage.

### `prompt-library.md`

Reusable prompt text that is still primarily managed by the human maintainer. Prompts that become routine candidates for automation may later be promoted into `.ai-context/playbooks/`.

### `playbooks/`

Standard operating procedures for recurring AI-assisted workflows. Playbooks are written for Codex and other AI agents to follow directly.

## Maintenance Guidelines

Update `.ai-context/` when the project materially changes in a way that affects future AI work.

Examples:

- Architecture changes
- New terminology
- New coding conventions
- New UI conventions
- New testing strategy
- A repeated workflow becomes stable enough to document as a playbook

Do not invent details that are not supported by the repository. When something is unclear, add a `TODO:` note or ask the user.
