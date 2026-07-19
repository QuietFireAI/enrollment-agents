---
name: P04-records-compliance-cycle
description: "Swarm deployment: statutory records gates (immunization, required documents) tracked from enrollment to closed, with sealed custody throughout. Agents 03, 05, 12, 04, 13. Adequacy is a licensed judgment; the swarm tracks existence."
---

# Playbook P04 - Records Compliance Cycle

**Swarm:** DispatcherAgents Enrollment Swarm (Schools & Childcare)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.2 (ratified 2026-07-18; extended & ratified 2026-07-18 - owner sign-off)

## Trigger
`enroll.record` arms the compliance clocks; `deadline.alert` drives the cycle.

## Preconditions
- The jurisdiction rule table (immunization windows, required documents) is owner-ratified.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Track to closed
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 12 | Clocks per enrollment; alerts at lead-times | `deadline.alert` → 02, 03 | statutory windows visible |
| 2 | 05 | Chase and inventory records - sealed custody | `forms.received` → 03, 13 | existence facts, content sealed |
| 3 | 03 | Status against the checklist; adequacy questions to the licensed human | `records.verify.result` → 02, 08, 13 | present-unreviewed routes, never self-cleared |
| 4 | 04 | Family deadline notices on approved templates | `family.message.send` | notices logged |

## HITL gates (hard stops)
- Medical content is never read by the swarm - existence, date, source only; adequacy is licensed.
- A certain statutory miss escalates before it lands.

## Completion criteria
Records gates closed by human/licensed review with the trail on record, or open gates named with clocks visible.

## Abort paths
- Exemption request arrives: route verbatim; the clock stays visible while the human decides.
