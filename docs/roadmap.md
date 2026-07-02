# Development Roadmap

## Philosophy

Every phase should end with a usable application.

Features should be developed as isolated, testable modules whenever possible.

---

## Phase 0

Repository initialization

Status: Complete

- [x] Repository created
- [x] Documentation started
- [x] Architecture finalized

---

## Phase 1

Application Skeleton

Status: Complete

Goal:

A Python application that starts successfully and serves both the GM and Player pages.

Deliverables

- [x] Python web server
- [x] Basic routing
- [x] Static assets
- [x] Template system
- [x] Shared application state
- [x] Public-state projection endpoint

---

## Phase 2

Scene Display

Status: Complete

Goal:

Display a scene image on the player display while allowing the GM to change it.

Deliverables

- [x] Image display
- [x] Scene title
- [x] Scene description
- [x] GM controls
- [x] App-managed image upload
- [x] Image URL download
- [x] Duplicate image detection
- [x] Scene image validation

---

## Phase 3

Generic Trackers

Status: Next

Goal:

Create reusable tracker widgets.

Examples

- Round Counter
- Torch Timer
- Countdown
- Party Gold

Initial tickets:

- P03-001 Define Generic Tracker Model
- P03-002 Add Tracker State and Projection
- P03-003 Add Tracker GM Controls

---

## Phase 4

Initiative Tracker

Status: Backlog

Goal:

Combat management.

Additional MVP work:

- Initiative model, projection, and GM controls.
- Local save/load persistence after scene, tracker, and initiative state exist.
