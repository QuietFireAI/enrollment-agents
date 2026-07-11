---
name: P06-withdrawal-transfer-cycle
description: "Swarm deployment: family withdrawal notice to a clean exit - final ledger facts, sealed release package, human-released records. Agents 10, 02, 05, 09, 04, 13. What leaves the building is a human decision with authorization on file."
---

# Playbook P06 - Withdrawal & Transfer Cycle

**Swarm:** DispatcherAgents Enrollment Swarm (Schools & Childcare)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off; not runtime-hardened)

## Trigger
`withdrawal.open` at 10 from the pipeline's routing of family notice.

## Preconditions
- Release-authorization rules loaded; the exit checklist is the ratified version.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Exit logistics
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 10 | Run the exit checklist; final-ledger and proration facts assembled per policy | (facts via records + 09) | refund decision facts ready for the human |
| 2 | 05 | Exit forms and release authorizations | `forms.received` → 03, 08, 13 | authorization status on record |

### Phase 2 - Release
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 10 | Assemble the sealed release package + authorization status | `release.package` → human, 13 | the human releases; the swarm assembles |
| 4 | 04 | Exit process communications | `family.message.send` | sends logged |

## HITL gates (hard stops)
- No records release without the authorization on file AND the human's act.
- Custody-conflicted instructions freeze the process and route immediately.

## Completion criteria
Exit complete: ledger closed with facts for the refund decision, release package human-released, roster updated.

## Abort paths
- Ambiguous release scope: both readings route; nothing releases on a guessed scope.
