---
name: P12-custody-change-wave
description: "Swarm deployment: stated or documented custody/authorization change to a re-anchored record with human-approved effect. Agents 01/04/05 (detection), 02, 10, 13. The swarm never adjudicates custody: statements are noticed, documentation is inventoried, and only human approval moves the record."
---

# Playbook P12 - Custody Change Wave

**Swarm:** DispatcherAgents Enrollment Swarm (Schools & Childcare)
**Type:** Deployment playbook (consumed by Agent 00 - Dispatcher)
**Version:** 0.1 (ratified 2026-07-11 - owner sign-off; not runtime-hardened)

## Trigger
`custody.notice` from intake (01), family channel (04), or received documentation (05).

## Preconditions
- The prior authorization facts (pickup list, records access, financial responsibility) are on record - a change is only a change against a recorded baseline.
Precondition unmet = playbook does not start; `clarification.request` to human.

## Deployment sequence

### Phase 1 - Notice and freeze the ambiguity
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 1 | 01/04/05 | Notice verbatim with source; documentation inventoried existence/type/date/source | `custody.notice` → 02, 10, 13 | notice on record; nothing changed yet |
| 2 | 02 | Pending offers, releases, and disclosures re-check against the notice before moving | (hold where affected) | no affected action proceeds on the old facts |

### Phase 2 - Human-approved effect
| Step | Agent | Action | Intent | Proof of done |
|---|---|---|---|---|
| 3 | 10 | Release/records posture re-anchored only on verified documentation + human approval | `release.package` → human (where releases pend) | human decision on record |
| 4 | 13 | The change, its documentation, and the approval recorded as one auditable unit | `interaction.log` | who changed what, on whose approval, citing what |

## HITL gates (hard stops)
- The swarm never decides who has custody - a stated change freezes affected ambiguity; only verified documentation plus human approval changes pickup, access, or disclosure.
- Both parents/guardians retain their existing recorded rights until the human rules - a notice is not a verdict.

## Completion criteria
Every affected pending action re-checked, the record changed only under human approval with documentation cited, the full unit auditable.

## Abort paths
- Conflicting custody claims arrive: both recorded verbatim; all affected actions hold; human immediately - conflicts are legal territory.
- A pickup situation is live while ambiguity stands: human immediately, same turn - safety over process, always.
