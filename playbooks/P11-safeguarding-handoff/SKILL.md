---
name: P11-safeguarding-handoff
description: "Swarm deployment: safeguarding concern detected anywhere to verbatim human handoff, sealed record, ops visibility. Agents 01/04/06 (detection), 13, 14. The swarm's entire role is the handoff: no questions, no statements, no visible change in posture - what happens next is the human's alone."
---

# Playbook P11 - Safeguarding Handoff

**Swarm:** DispatcherAgents Enrollment Swarm (Schools & Childcare)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.2 (ratified 2026-07-18; extended & ratified 2026-07-18 - owner sign-off)

## Trigger
`safeguarding.notice` from intake (01), family channel (04), or tours/events (06).

## Preconditions
- The concern is captured verbatim with source, timestamp, and child/family reference - the human receives the words, not a summary.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Handoff (same turn)
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 01/04/06 | Route the concern verbatim; the routine conversation neither references it nor halts conspicuously | `safeguarding.notice` → human, 13, 14 | verbatim record delivered, human alerted |
| 2 | 14 | Ops visibility same turn; nothing about it appears in routine reporting beyond the handoff fact | (ops log) | daily book shows the handoff happened |

### Phase 2 - Sealed record
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 13 | Sealed record entry - verbatim, access itself logged | `interaction.log` (sealed handling) | record complete; reads are audited |

## HITL gates (hard stops)
- No agent asks follow-up questions, makes statements, or visibly changes posture toward the family - investigation, notification, and mandated reporting are human decisions under law.
- The record is sealed: routine reports carry the handoff fact only, never the content.

## Completion criteria
Verbatim handoff delivered same turn, sealed record complete, ops aware of the handoff fact; the human owns everything after.

## Abort paths
- Ambiguity about whether something is a safeguarding concern: hand it off - the conservative read is the only read.
- The concern implicates staff: identical handoff, zero internal routing beyond human and sealed record.
