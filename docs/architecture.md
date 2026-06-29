# Architecture

## Purpose

The application consists of a single backend responsible for maintaining game state.

The GM interacts with the backend through a control interface.

Players receive a filtered, read-only view of the same state.

---

## System Overview

GM Browser

↓

Python Server

↓

Shared State

↓

Player Browser

---

## Core Principles

The backend owns all state.

The player interface never modifies state.

The GM interface edits state exclusively through API endpoints.

The player interface only receives public information.

---

## Future Considerations

Eventually multiple sessions should be supported.

Each session should have:

- Session ID
- GM Key
- Independent state
