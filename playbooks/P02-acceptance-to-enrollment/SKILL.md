---
name: P02-acceptance-to-enrollment
description: "Swarm deployment: the human's acceptance to an executed, gate-clean enrollment with ledger and clocks armed. Agents 02, 08, 03, 05, 09, 11, 12, 04, 13. Gates hold with names; ratios have no override."
---

# Playbook P02 - Acceptance to Enrollment

**Swarm:** DispatcherAgents Enrollment Swarm (Schools & Childcare)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off; not runtime-hardened)

## Trigger
The human's acceptance decision fires `enroll.request` at 08.

## Preconditions
- Capacity fact from 11 seats the enrollment (the ratio is physics); terms are the human's decision.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Package and sign
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 08 | Assemble the enrollment package: template + terms + forms checklist | `enroll.package` → human, 13 | signature-ready; gaps named |
| 2 | 05 | Enrollment forms chase and sealed inventory | `forms.received` → 03, 08, 13 | gates fact-tracked |
| 3 | 03 | Records gates (immunization status) checked | `records.verify.result` → 08, 13 | statutory gates visible |

### Phase 2 - Record and arm
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 4 | 08 | Record the executed enrollment - terms verbatim, dates exact | `enroll.record` → 09, 11, 12, 13 | ledger, roster, and clock basis set |
| 5 | 12 | Immunization and paperwork clocks armed | `deadline.alert` (at lead-times) | clocks live |
| 6 | 04 | Welcome and start-date communications | `family.message.send` | sends logged |

## HITL gates (hard stops)
- No enrollment completes over an open statutory gate absent the human's recorded exception.
- No enrollment exceeds a licensed ratio - refuse + integrity.violation; no override exists.

## Completion criteria
Enrollment executed and recorded; ledger opened, roster updated, clocks armed.

## Abort paths
- Immunization gate open at start date: hold + escalate with the compliance clock attached.
