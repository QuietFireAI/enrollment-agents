---
name: P07-capacity-ratio-watch
description: "Swarm deployment: continuous roster and licensed-ratio math with lead-margin flags and zero override paths. Agents 11, 07, 02, 14, 13. The licensing ratio is the safety ceiling - capacity above it does not exist in this swarm."
---

# Playbook P07 - Capacity & Ratio Watch

**Swarm:** DispatcherAgents Enrollment Swarm (Schools & Childcare)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (DRAFT - not implemented)

## Trigger
Continuous: every `enroll.record`, withdrawal, and staffing-input change recomputes.

## Preconditions
- Licensed ratios and configured caps are owner-ratified; staffing inputs current per rule.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Continuous - the watch
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 11 | Recompute capacity per class/room on every roster or staffing fact | `capacity.status` → 02, 07, 13 | live math, never enrollment-time math |
| 2 | 11 | Lead-margin flags before any room approaches its ratio | (flags at configured margin) | before, never after |
| 3 | 07 | Openings feed the waitlist cycle (P03) | (via capacity facts) | seats fill by rule |
| 4 | 14 | Ratio state into the books; margin flags lead until resolved | (book sections) | ratio state never a footnote |

## HITL gates (hard stops)
- A directed enrollment exceeding a licensed ratio is refused + integrity.violation - no override path exists.
- Mid-day staffing changes recompute immediately and route.

## Completion criteria
Continuous playbook: capacity facts live per licensed ratios; openings flowing to the waitlist by rule.

## Abort paths
- Roster/enrollment record conflict: both facts route; the roster never silently reconciles.
