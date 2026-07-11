---
name: P03-waitlist-cycle
description: "Swarm deployment: capacity opening to a rule-ordered seat offer with the window run per policy. Agents 07, 11, 02, 04, 13. The order is rule arithmetic; off-rule placements are integrity violations."
---

# Playbook P03 - Waitlist Cycle

**Swarm:** DispatcherAgents Enrollment Swarm (Schools & Childcare)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (DRAFT - not implemented)

## Trigger
`capacity.status` from 11 opens a seat, or a new `waitlist.entry` arrives.

## Preconditions
- The ratified priority rules and offer-window policy are current.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Order and offer
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 07 | Order the list per the ratified rules; ties break on the ratified tiebreak | (order state) | rule math on facts |
| 2 | 07 | Issue the seat offer with the published window | `seat.offer` → 02, 13 | offer + window on record |
| 3 | 04 | Offer notification on identical templates | `family.message.send` | sends logged |
| 4 | 07 | Expired windows move to the next rule-ordered family, history recorded | (next offer) | no silent skips, no silent holds |

## HITL gates (hard stops)
- No off-rule ordering or placement - an exception is a human's recorded, authority-attached decision.
- Waitlist positions of other families are never disclosed.

## Completion criteria
Seat offered per the rules; acceptance flows to enrollment (P02) or the next offer fires with history intact.

## Abort paths
- A directed off-rule placement without recorded authority: refuse + integrity.violation.
