# Session Startup Playbook

## Purpose

Use this playbook at the beginning of a new AI-assisted development session.

The goal is to establish enough project context to begin work safely without rereading the entire repository or performing unnecessary maintenance.

## When to Use

Use this playbook when:

- Starting a new Codex session
- Returning to the project after a break
- Beginning work on a new ticket
- Switching phases or branches
- The user asks for a project brief before development

Do not use this playbook as a substitute for focused task analysis. It prepares the session; it does not perform the work.

## Procedure

### 1. Read Core Instructions

Read `AGENTS.md` first.

Follow its safety, documentation, command, and repository-boundary rules throughout the session.

### 2. Identify Current Working Context

Determine, when possible:

- Current branch
- Current phase
- Current ticket or task
- Whether the working tree already has changes
- Whether the user's request belongs to the active phase

If the active phase or ticket is unclear, infer it from the branch name, `.project-board/`, and the user's request. If it remains unclear, say so in the startup brief.

### 3. Review Relevant Planning Documents

Review only the planning files needed for the task.

Likely locations:

- `.project-board/pNN/`
- `docs/roadmap.md`
- Any ticket or document directly named by the user

Do not scan every ticket unless the user asks for a phase audit, ticket cleanup, or project-board review.

### 4. Review Relevant AI Context

Read only the `.ai-context/` files relevant to the task.

Examples:

- Code changes: read `coding-style.md`
- Test changes: read `testing.md`
- UI changes: read `ui-conventions.md`
- Domain model or state changes: read `architecture.md` and `terminology.md`
- Repeated workflow: read the relevant file under `.ai-context/playbooks/`

If a relevant `.ai-context/` file is missing or incomplete, mention that in the startup brief.

### 5. Check for Obvious Maintenance Signals

Look for obvious signs that documentation or planning may need attention, such as:

- A completed ticket still marked `In Progress`
- Documentation that clearly contradicts the requested work
- Missing AI context that would help future sessions
- A phase that appears complete but has not had closeout review

Do not perform broad maintenance automatically. Report observations and ask before making maintenance changes unless the user specifically requested them.

### 6. Produce a Startup Brief

Before editing files, provide a short brief containing:

- Current branch, if known
- Active phase or ticket, if known
- Relevant files or documents reviewed
- Any immediate risks, blockers, or mismatches
- Suggested next action

Keep the brief concise. The goal is to align before changing the repository.

### 7. Wait for Approval When Needed

Wait for user approval before:

- Making broad documentation updates
- Creating or closing tickets
- Changing phase status
- Installing dependencies
- Running destructive commands
- Making changes outside the requested task

For small, clearly requested edits, proceed according to `AGENTS.md`.

## Output Format

Use a concise format similar to:

```text
Startup brief:

- Branch: p03-generic-trackers
- Active phase: Phase 3 — Generic trackers
- Relevant context reviewed: AGENTS.md, .project-board/p03/..., .ai-context/coding-style.md
- Notes: No obvious documentation blockers found.
- Suggested next action: Implement the requested tracker update.
```

## Non-Goals

This playbook should not:

- Audit the entire project
- Rewrite documentation
- Create tickets
- Close tickets
- Modify code
- Run tests
- Commit changes

Those actions may happen later in the session, but they are not part of startup.
