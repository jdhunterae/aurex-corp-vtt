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

Follow-up tickets:

- P02-005 Fix Player Asset Rendering - Done
- P02-006 Add Prepared Scene Library

---

## Phase 3

Generic Trackers

Status: In Progress

Goal:

Create reusable tracker widgets.

Examples

- Round Counter
- Torch Timer
- Countdown
- Party Gold

Tickets:

- [x] P03-001 Define Generic Tracker Model
- [x] P03-002 Add Tracker State and Projection
- [x] P03-003 Add Tracker GM Controls
- [x] P03-004 Add Tracker Player Display
- [x] P03-005 Add Player Auto Refresh
- [ ] P03-006 Redesign GM Control Layout
- [ ] P03-007 Add GM Action Feedback
- [x] P03-008 Retain Scroll Position After Updates

Phase 3 has a usable player display: public scene and tracker changes now refresh automatically from the public projection endpoint. GM form submissions now return to the relevant page area after scene, asset, and tracker updates.

Current active ticket:

- P03-006 Redesign GM Control Layout

---

## Phase 4

Initiative Tracker

Status: Backlog

Goal:

Combat management.

Additional MVP work:

- Initiative model, projection, and GM controls.
- Local save/load persistence after scene, tracker, and initiative state exist.
