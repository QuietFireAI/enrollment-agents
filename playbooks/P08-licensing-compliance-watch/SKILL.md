---
name: P08-licensing-compliance-watch
description: "Swarm deployment: facility license renewals, mandated inspections, and configured staff-certification clocks tracked at lead-time. Agents 12, 05, 14, 13. Every external filing is a human act."
---

# Playbook P08 - Licensing Compliance Watch

**Swarm:** DispatcherAgents Enrollment Swarm (Schools & Childcare)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (DRAFT - not implemented)

## Trigger
Continuous: renewal and inspection clocks per the ratified jurisdiction table.

## Preconditions
- The jurisdiction rule table is owner-ratified and current.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Continuous - the watch
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 12 | Track license renewals, inspection windows, configured certifications | `deadline.alert` → 14 (lead-times) | windows visible ahead |
| 2 | 05 | Renewal paperwork chased and inventoried | `forms.received` → 03, 13 | artifacts on record |
| 3 | 12 | Holds on actions that would violate a licensing rule | `compliance.hold` → queue | violations held, not discovered |

## HITL gates (hard stops)
- No filing or response to a licensing authority from the swarm - human acts with the packages assembled.
- Certain misses escalate the moment they are certain.

## Completion criteria
Continuous playbook: licensing clocks visible at lead-time; renewal artifacts inventoried; holds enforced.

## Abort paths
- Jurisdiction-table gap: clocks run on the most conservative known rule; the gap escalates for ratification.
