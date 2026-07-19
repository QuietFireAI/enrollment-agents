---
name: P13-refund-tuition-reconciliation
description: "Swarm deployment: withdrawal refund from published schedule to signed execution with books at $0.00. Agents 10, 09, 04, 13. Refunds are money: the schedule computes, the human signs, the books reconcile to the penny."
---

# Playbook P13 - Refund & Tuition Reconciliation

**Swarm:** DispatcherAgents Enrollment Swarm (Schools & Childcare)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off; not runtime-hardened)

## Trigger
Withdrawal completes (P06) with a refundable balance per the published tuition schedule, or `reconciliation.exception` surfaces a credit.

## Preconditions
- The published tuition schedule and the family's payment record are both on file - the refund is arithmetic shown, never judgment applied.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Compute and package
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 09 | Refund computed from the published schedule; every number carries its source | `tuition.record` → 13 | computation on record |
| 2 | 09 | Package to human: schedule citation, payments, computed refund | `reconciliation.exception` → human, 13 (as the money package) | package delivered |

### Phase 2 - Signed execution
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 09 | Refund executes only on signed authority | (await `refund.authority` ← human) | signed envelope on the chain first |
| 4 | 04 | Family informed from posted facts once executed | `family.message.send` → external | templated notice, facts only |
| 5 | 09 | Books reconcile to $0.00 or the variance escalates | `reconciliation.exception` → human, 13 (if any variance) | clean books or a named exception |

## HITL gates (hard stops)
- No refund executes unsigned - refund.authority is money, same doctrine as discount.authority.
- The $0.00 rule governs: any variance between schedule, payments, and executed refund is an exception, never absorbed.

## Completion criteria
Refund executed on signed authority per the published schedule, family informed, books at $0.00; or the blocking question named to the human.

## Abort paths
- Family disputes the schedule computation: the dispute routes verbatim with the arithmetic attached - the swarm shows its work and stops.
- Financial responsibility is under a custody conflict (P12): the refund holds until the human rules on payee.
