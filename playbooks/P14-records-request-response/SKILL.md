---
name: P14-records-request-response
description: "Swarm deployment: external records request (agency, receiving school, parent) to human-approved disclosure inside the clock. Agents 13, 12, 05, 04. Every item is custody-flagged; release is a human decision - a records request about a child is never routine."
---

# Playbook P14 - Records Request Response

**Swarm:** DispatcherAgents Enrollment Swarm (Schools & Childcare)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.2 (ratified 2026-07-18; extended & ratified 2026-07-18 - owner sign-off)

## Trigger
External records request lands via 04 (family channel) or intake (01); agency/compliance requests via 12.

## Preconditions
- The request is captured verbatim with date, requester, claimed relationship/authority, scope, and the applicable response window.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Clock and inventory
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 12 | Response clock armed (jurisdictional default if none stated) | `deadline.alert` → 14 (at lead-times) | clock live |
| 2 | 13 | Disclosure inventory: existence, type, date, source per item - custody flags named per item | `records.disclosure.package` → human, 12 | inventory delivered inside lead-time |
| 3 | 05 | Documentation supporting the requester's authority inventoried (never adjudicated) | `forms.received` → 03, 13 (references) | authority-support status per requester |

### Phase 2 - Human release
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 4 | 13 | Record the human's release decision and what was disclosed | `record.response` + `interaction.log` | itemized: who, what, when, under whose approval, custody check noted |
| 5 | 04 | Transmit per the approved scope | `family.message.send` → external (or agency channel per direction) | transmission artifact on record |

## HITL gates (hard stops)
- Nothing beyond the human's itemized approval is disclosed - the approval is the ceiling.
- Requester authority is never adjudicated by the swarm - custody flags and supporting documentation go to the human; the decision is theirs (P12 doctrine).
- A noticed custody change freezes affected disclosures until the human rules.

## Completion criteria
Human-approved disclosure transmitted inside the clock with a complete itemized, custody-checked record; or refusal/clarification recorded the same way.

## Abort paths
- Requester's claimed authority conflicts with the record: human immediately with both facts - never split the difference.
- Request arrives under legal process (subpoena, court order): counsel's lane - the swarm inventories and waits for direction.
