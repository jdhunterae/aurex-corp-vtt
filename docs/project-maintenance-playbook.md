# Project Maintenance Playbook

## About This Document

This document serves as the operational playbook for maintaining the Aurex Corp VTT repository. It is intended for human developers responsible for the long-term health of the project.

Unlike `AGENTS.md` or the files within `.ai-context/`, this playbook is written for people rather than AI agents. It documents repeatable maintenance procedures, recommended workflows, and reusable prompts that have proven valuable throughout development.

The goal of this document is consistency. Every developer should approach recurring project maintenance in roughly the same way, regardless of who performs the work.

As development continues, procedures that become routine may be promoted into `.ai-context/playbooks/` where AI agents can execute them with little or no prompting.

---

# Automation Levels

Project maintenance procedures gradually mature over time.

| Level | Description |
|--------|-------------|
| **0 – Manual** | Performed entirely by a developer. |
| **1 – Prompt Assisted** | A reusable prompt exists within this playbook. |
| **2 – AI Playbook** | A standardized AI procedure exists in `.ai-context/playbooks/`. |
| **3 – Repository Native** | The workflow is automatically recognized through `AGENTS.md` with minimal prompting. |

Whenever a maintenance procedure becomes repetitive, consider promoting it to the next automation level.

---

# Session Startup

These procedures establish project context before implementation work begins.

---

## Daily Project Review

**Status**

🟢 Stable

**Automation Level**

Level 1 — Prompt Assisted

**Frequency**

At the beginning of every development session.

**Purpose**

Ensure both the developer and Codex understand the current state of the project before making changes.

#### Procedure

1. Open Codex from the project root.
2. Paste the prompt below.
3. Review the generated startup brief.
4. Confirm the proposed work before implementation begins.

#### Prompt

```text
Before beginning today's work:

1. Read AGENTS.md.
2. Review the active phase in .project-board.
3. Determine whether any completed tickets should be closed or archived.
4. Check whether project documentation still matches the current implementation.
5. Suggest improvements to project organization or AI workflow before writing code.
6. Present a short "Today's Project Brief" and wait for approval before making changes.
```

#### Prompt Customization

None.

#### Expected Result

Codex should:

- identify the active development phase
- identify the current ticket
- summarize repository health
- identify documentation drift
- recommend the next logical task

#### Notes

This workflow is a candidate for permanent automation through the Session Startup AI Playbook.

---

# Project Audits

These procedures help ensure the repository remains healthy as both the project and AI tooling evolve.

---

## Project Maintenance Audit

**Status**

🟢 Stable

**Automation Level**

Level 1 — Prompt Assisted

**Frequency**

After updating Codex or after major repository changes.

**Purpose**

Audit the repository for outdated documentation, obsolete AI guidance, stale planning documents, and opportunities to improve the development workflow.

#### Procedure

1. Ensure any in-progress work has been saved.
2. Run the prompt below.
3. Review the generated audit.
4. Approve or reject recommended changes before implementation.

#### Prompt

```text
Perform a project maintenance audit.

Do not modify any files yet.

Review:

- AGENTS.md
- README.md
- docs/
- .project-board/
- .ai-context/
- project structure
- pyproject.toml
- requirements.txt

Determine whether anything should be updated to reflect:

- newer Codex capabilities
- improved project organization
- outdated instructions
- missing documentation
- duplicate or contradictory documentation
- opportunities to simplify the workflow

Also identify:

- stale tickets
- completed work that should be archived
- documentation that no longer matches the implementation
- missing project conventions that would help future AI agents

Produce a report in:

.brainstorming/project-audit-YYYY-MM-DD.md

Do not make changes until I approve them.
```

#### Prompt Customization

Replace `YYYY-MM-DD` with today's date.

#### Expected Result

A maintenance report should be produced without modifying the repository.

---

## AI Workflow Audit

**Status**

🟢 Stable

**Automation Level**

Level 1 — Prompt Assisted

**Frequency**

Approximately once per month.

**Purpose**

Evaluate how effectively future AI assistants can understand and work within the repository.

#### Procedure

Run this audit after several completed features or whenever the project's workflows have evolved significantly.

#### Prompt

```text
Act as the lead software architect performing an AI workflow audit.

Do not review the application code for quality.

Instead review:

- AGENTS.md
- .ai-context/
- docs/
- .project-board/
- repository organization
- planning documents
- developer workflow

Identify:

- outdated guidance
- duplicated documentation
- conflicting instructions
- opportunities to simplify AI prompts
- missing AI context
- missing architectural decisions
- opportunities to improve onboarding for future AI sessions

Categorize each recommendation as:

Critical
Recommended
Optional

Generate a report in:

.brainstorming/project-ai-audit-YYYY-MM-DD.md

Do not modify files.
```

#### Prompt Customization

Replace `YYYY-MM-DD` with today's date.

---

# Phase Maintenance

These procedures should be performed whenever a roadmap phase has been completed.

---

## Phase Closeout Review

**Status**

🔵 Candidate for AI Playbook

**Automation Level**

Level 1 — Prompt Assisted

**Frequency**

Whenever the final ticket in a development phase has been completed.

**Purpose**

Synchronize project documentation, AI context, roadmap progress, and project planning before beginning the next phase.

#### Procedure

Run this review after all work for the current phase has been accepted.

#### Prompt

```text
We have completed Phase X.

Review:

- .ai-context/
- AGENTS.md
- docs/
- README.md
- .project-board/

Determine whether any documentation, AI context, or project conventions should be updated to reflect the completed work.

Do not modify files immediately.

Instead:

1. Summarize recommended changes.
2. Explain why each change is necessary.
3. Identify obsolete guidance.
4. Identify missing guidance.
5. Recommend any new AI playbooks that should be created.

Wait for approval before making changes.
```

#### Prompt Customization

Replace "Phase X" with the completed phase.

#### Expected Result

Documentation updates are proposed before implementation begins.

#### Notes

This procedure is expected to become one of the project's first AI Playbooks.

---

# Documentation Maintenance

These procedures ensure documentation remains synchronized with implementation.

---

## Documentation Synchronization Review

**Status**

🟢 Stable

**Automation Level**

Level 1 — Prompt Assisted

**Frequency**

After major refactoring or architecture changes.

**Purpose**

Identify documentation that no longer accurately reflects the implementation.

#### Prompt

```text
Review the repository and determine whether the current documentation still matches the implementation.

Focus on:

- architecture
- terminology
- coding conventions
- testing guidance
- UI conventions
- project organization

Produce a report describing:

- outdated documentation
- missing documentation
- documentation that should be merged
- documentation that should be split
- documentation that should be archived

Do not modify files until approval is given.
```

---

# Prompt Development

These procedures help improve the project's AI workflow over time.

---

## Promoting a Prompt to an AI Playbook

**Status**

🟢 Stable

**Automation Level**

Level 0 — Manual

**Frequency**

Whenever a prompt has become part of the normal development workflow.

**Purpose**

Reduce repeated prompting by converting mature workflows into permanent AI procedures.

#### Criteria

A prompt should be promoted when it:

- has been used successfully several times
- produces consistent results
- represents a repeatable workflow
- is unlikely to change frequently

#### Result

Instead of copying a prompt, future AI sessions can simply consult the appropriate playbook within `.ai-context/playbooks/`.

Eventually, `AGENTS.md` should reference these playbooks so that common maintenance workflows become repository-native behavior.
