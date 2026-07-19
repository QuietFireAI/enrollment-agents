# TUNING_MANUAL - enrollment-agents

Every configurable parameter, placeholder, and ratification in this identity.
Rule (inherited doctrine): any commit introducing a tunable updates this
manual in the same commit.

---

## TOP OF LIST - Deliberate placeholders & unratified content (read before deployment)

Full sweep 2026-07-18. If it's not in this table it's ratified content or
real spec.

| Item | Where | Status | What blocks / what to do |
|---|---|---|---|
| Signer identity | `config/authority_signers.json` | **RATIFIED FOR TEST 2026-07-18** — "Dr. Jeff Phillips" is a fictional test persona | Demo/test only. Production MUST replace `signer_login` with a real IdP login; the IdP seam (INTEGRATIONS.md) is a go-live prerequisite for any authority intent. |
| Ratio caps | `config/ratio_caps.json` | **DOCTRINE RATIFIED / entries jurisdictional** | The-cap-is-law doctrine binding; load your licensed ratios and capacities before any offer arms. |
| Tuition schedule | `config/tuition_schedule.json` | **DOCTRINE RATIFIED / entries deployment content** | Zero-threshold doctrine binding; empty schedule = every money move = signed. |
| Jurisdiction table | `config/jurisdiction_table.json` | **DEPLOYMENT CONTENT** | Your state/locality's requirements; the conservatism rule (stricter/earlier wins) governs derivations. |
| Offer window / priority rules | `config/offer_window_rules.json`, `config/priority_rules.json` | **DEPLOYMENT CONTENT** | Owner-ratified versions required before P03 runs. |
| Message templates | `config/message_templates.json` | **UNRATIFIED — awaiting owner sign-off per template** | Fill `approved_by` per template (includes new `opt_out_confirmed`). |
| Runtime | whole repo | **BLUEPRINT, not runtime-hardened** | Side-loads into dispatcher-agents; no working build yet (owner decision 2026-07-18, Option A). medbilling-agents is the working-build reference for this catalog. |

---

## Ratified (owner: Jeff Phillips, 2026-07-18)

| Parameter | Value | Consumer |
|---|---|---|
| Books reconciliation tolerance | **$0.00** — permeates all blueprints | 09 → `reconciliation.exception` |
| Zero-threshold money doctrine | schedule-matching auto with citation; discounts/waivers/refunds signed, any amount | 09 |
| Safeguarding handoff | same-turn, verbatim, sealed record, zero swarm follow-up | P11 (class 1) |
| Custody doctrine | the swarm never adjudicates; notice freezes affected ambiguity; documentation + human approval moves the record | P12 (class 1) |
| The cap is law | ratios/capacity are physics; over-line goes to human same turn | 11 |

### The $0.00 rule (permeates ALL identity blueprints - owner decision 2026-07-18)

Any variance between posted money and reconciled books, any amount, is a
`reconciliation.exception` routed to the human and the books. No "close
enough" lane. The HITL is notified on every variance.

---

## PROPOSED thresholds — pending owner ratification

Conservative defaults until ratified or amended. Jurisdictional law always
governs where stricter.

| Parameter | Proposed | Consumer |
|---|---|---|
| Inquiry response SLA | 4 business hours | 01/04 (P01) |
| Seat-offer window | 48 hours to accept | 07 (P03, offer_window_rules) |
| Records chase cadence | every 7 days until complete | 03/05 (P04) |
| Verification staleness | per jurisdiction table (regulatory) | 03 |
| Tuition past-due sequence | 0 / 15 / 30 days, then human decision | 09 (P05) |
| Records-response lead alert / escalation | 10 / 3 days | 12 (P14) |
| Wait-state visibility threshold | 3 business days | any → 14 |
