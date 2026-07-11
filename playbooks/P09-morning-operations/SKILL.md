---
name: P09-morning-operations
description: "Swarm deployment: the office's morning book. Today's tours, pipeline and waitlist states, open gates on starting students, ratio state, compliance clocks. Agents 14, 13, 12."
---

# Playbook P09 - Morning Operations

**Swarm:** DispatcherAgents Enrollment Swarm (Schools & Childcare)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off; not runtime-hardened)

## Trigger
Scheduled daily start (owner-configured time) or owner command.

## Preconditions
- EOD books from the previous day exist (P10 completion on the log); if absent, the book runs with the gap NAMED.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Assemble (parallel, all to human review)
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 14 | Pull tours, pipeline/waitlist states, open enrollment gates, ratio state | `record.request` → 13 | sections sourced; ratio flags lead |
| 2 | 14 | Today's clock alerts: immunization, licensing, billing | (from 12's alert stream) | clock section current with lead-times |

### Present
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 14 | Deliver the morning book; unavailable sources marked absent | `report.package` → human | book delivered; the human directs |

## HITL gates (hard stops)
- A source unavailable at assembly is a named absence - never yesterday's numbers backfilled.

## Completion criteria
Morning book delivered with every section sourced or marked absent; ratio flags lead.

## Abort paths
- Record source down: section marked absent; the book still delivers on time.
