---
name: P05-tuition-cycle
description: "Swarm deployment: enrollment terms to a clean ledger - charges, payments, statements, published fees, signed-authority exceptions. Agents 09, 04, 12, 13. A child's attendance is never cut off by automation."
---

# Playbook P05 - Tuition Cycle

**Swarm:** DispatcherAgents Enrollment Swarm (Schools & Childcare)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (DRAFT - not implemented)

## Trigger
`enroll.record` opens the ledger; the published billing cycle drives it.

## Preconditions
- The published fee schedule and delinquency rules are the ratified versions.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Run the ledger
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 09 | Charges per enrollment terms and the published schedule; payments recorded | `tuition.record` → 13 | citations per line |
| 2 | 04 | Statement cycle on identical templates | `family.message.send` | statements logged |
| 3 | 09 | Discounts/aid/arrangements ONLY on signed authority | (record with authority envelope_id) | no unsigned money |
| 4 | 09 | Delinquency per published rules; enrollment-affecting consequences route to the human | (facts to human at thresholds) | automation never excludes a child |

## HITL gates (hard stops)
- No discount, aid, or arrangement beyond published policy without signed `discount.authority`.
- Any consequence touching a child's attendance is a human decision.

## Completion criteria
Ledger current with citations; exceptions authority-attached; threshold cases in the human queue.

## Abort paths
- Ledger dispute: both readings preserved and routed; the ledger never adjudicates.
