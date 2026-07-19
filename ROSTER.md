# DispatcherAgents Enrollment Swarm (Schools & Childcare) - Roster v0.2 (ratified 2026-07-18 - owner sign-off)

15 agents, hub-and-spoke via 00. All inter-agent communication is a logged
envelope through the Dispatcher; the route-space is closed (identity/routes.json).

| # | Agent | Type | Autonomy boundary |
|---|---|---|---|
| 00 | Dispatcher | Hub (transport, gates, audit) | Validates every (from, intent, to) tuple; holds ambiguity; owns the audit log |
| 01 | Inquiry Intake Agent | Intake (family inquiries) | Autonomous inquiry capture and routing; NEVER an admissions opinion, availability promise beyond the record, or any question touching protected characteristics - identical process for every family |
| 02 | Admissions Pipeline Agent | Coordination (applications, offers) | Autonomous application assembly and pipeline tracking with IDENTICAL-format packages; admission decisions, their reasons, and their communication are the human's - the pipeline sequences, never selects |
| 03 | Records Verification Agent | Systems lookup (records status facts) | Autonomous status tracking of required records (immunization, prior-school, custody documents) - existence, date, and source facts only; medical and custody CONTENT is sealed, and exemption or adequacy judgments are human |
| 04 | Family Communication Agent | Communication hub (family-facing) | Autonomous sends from approved templates; NO admissions-decision content, no child-specific judgments, identical templates for every family - decision communication is the human's |
| 05 | Forms & Documents Agent | Evidence pipeline (forms, sealed custody) | Autonomous request, receipt, and inventory of forms and records; medical, custody, and child-specific content is sealed custody - inventoried by existence and routed, never read |
| 06 | Tours & Events Agent | Scheduling execution (tours, open houses) | Autonomous tour and event scheduling within published calendars and capacity; identical tour offering for every family |
| 07 | Waitlist Management Agent | Sequence execution (waitlist) | Autonomous waitlist ordering and seat offers PER THE RATIFIED PRIORITY RULES only - the rules are published policy; an off-rule placement is an integrity violation |
| 08 | Enrollment Documents Agent | Document production (enrollment packages) | Autonomous enrollment-package assembly from approved templates and human-decided terms; the human signs, and the enrollment record's dates and terms must be exact - they drive tuition and compliance clocks |
| 09 | Tuition Records Agent | Financial records (tuition ledger) | Autonomous tuition ledger per enrollment terms and the published fee schedule; discounts, financial aid, and arrangements beyond policy execute only on signed human `discount.authority` |
| 10 | Withdrawal & Transfer Agent | Coordination (withdrawals, records release) | Autonomous withdrawal logistics and release-package assembly; the records RELEASE is a human act under the release-authorization rules - the swarm assembles, the human releases |
| 11 | Roster & Capacity Agent | Records engine (rosters, ratios) | Autonomous roster records and capacity math per LICENSED RATIOS AND CONFIGURED CAPS - the licensing ratio is physics; no enrollment fact ever exceeds it, and overrides do not exist |
| 12 | Compliance & Deadlines Agent | Regulatory engine (licensing, immunization clocks) | Autonomous clock tracking and alerting per the ratified jurisdiction table; regulatory interpretation and every external filing are human - clocks are facts, conservatism ratified |
| 13 | Enrollment Records Agent | System of record (enrollment files, audit) | Autonomous record keeping; the record is append-only - corrections are new entries referencing what they correct; child data is minimized and sealed custody governs medical/custody content |
| 14 | Daily Operations Agent | Operations cadence (enrollment books) | Autonomous book assembly and presentation; the human reads the book and directs - the book never self-executes its recommendations |

Human lanes (never automated): admissions decisions and their communication, accommodation matters, record adequacy and exemptions (licensed review), records release (authorization + human act), discounts and financial aid (signed authority), any consequence affecting a child's attendance, custody matters, licensing filings and regulatory interpretation.
