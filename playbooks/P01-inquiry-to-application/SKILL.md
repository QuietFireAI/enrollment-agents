---
name: P01-inquiry-to-application
description: "Swarm deployment: family inquiry to a complete, identical-format application package for the human's decision. Agents 01, 02, 06, 03, 04, 13. Identical process for every family - the decision and its communication are the human's."
---

# Playbook P01 - Inquiry to Application

**Swarm:** DispatcherAgents Enrollment Swarm (Schools & Childcare)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off; not runtime-hardened)

## Trigger
`inquiry.captured` lands at 02.

## Preconditions
- Published program facts current; child-data minimization applied at capture (01's rule).
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Engage
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 06 | Schedule the tour per the published calendar | `tour.event` → 02, 13 | attendance facts, never impressions |
| 2 | 04 | Process communications on identical templates | `family.message.send` | sends logged |

### Phase 2 - Package
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 03 | Required-records status facts (content sealed) | `records.verify.result` → 02, 13 | item-level status, adequacy human |
| 4 | 02 | Assemble the identical-format application package | `application.package` → human, 13 | the human decides; the swarm ranks nothing |

## HITL gates (hard stops)
- Identical process, identical package format, for every family - deviation is the named fair-process failure.
- Protected-characteristic and accommodation content routes to the human verbatim, never processed.

## Completion criteria
Application package delivered in the identical format with records status and tour facts attached.

## Abort paths
- Sensitive child information surfaces: minimize, seal, route; the process continues identically or pauses on the human.
