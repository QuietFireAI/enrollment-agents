# build config: enrollment-agents
ROOT = "/home/claude/enrollment-agents"
REPO = "enrollment-agents"
BRAND = "DispatcherAgents Enrollment Swarm (Schools & Childcare)"
SWARM_SHORT = "Enrollment"
DOMAIN = "Schools & Childcare"
NOUN = "enrollment"
VERTICAL = "enrollment-agent"
AUTH_INTENT = "discount.authority"
PINGPONG = "(e.g., 02\u219403 records ping-pong on a borderline verification status)"
ESCALATIONS = "`escalation.child_safety` / `escalation.ratio_ceiling`"
INSPECTION_REF = "11's ratio-ceiling discipline"
DATA = "enrollment_data.py"
TUPLES = "enrollment_tuples.py"
PLAYBOOKS = "enrollment_playbooks.py"
ENVELOPE_AGENT = "02-admissions-pipeline"
IDENTITY_MD = "IDENTITY-enrollment-agent.md"
LAST_AGENT = "14-daily-operations"
LIC_NOUN = "enrollment agent"
CLASSES = {"P01": 2, "P02": 2, "P03": 2, "P04": 1, "P05": 2,
           "P06": 2, "P07": 1, "P08": 1, "P09": 2, "P10": 2}
PRIORITY_DOCTRINE = ("JIT run-priority per core doctrine: class 1 = statutory and safety-ceiling "
 "(records/immunization compliance gates, licensed-ratio watch, licensing clocks), "
 "class 2 = pipeline lifecycle and books. Pacing over braking: the siding scheduler "
 "paces class contention; nothing slam-stops, and ratio math never waits.")
HUMAN_LANES = ("Human lanes (never automated): admissions decisions and their communication, "
 "accommodation matters, record adequacy and exemptions (licensed review), records "
 "release (authorization + human act), discounts and financial aid (signed "
 "authority), any consequence affecting a child's attendance, custody matters, "
 "licensing filings and regulatory interpretation.")
DESC = '''DESC = {
 "00": "Enrollment swarm dispatcher. The hub: validates every (from, intent, to) tuple against the closed track, holds ambiguity in clarification, and owns the audit log. Nothing moves without it.",
 "01": "Inquiry intake. Use when family inquiries need complete capture with child-data minimization and identical process - no admissions opinions; sensitive content routes to human verbatim.",
 "02": "Admissions pipeline. Use when applications need IDENTICAL-format package assembly, pipeline tracking, and enrollment handoff - admission decisions and their communication are the human's.",
 "03": "Records verification. Use when immunization, prior-school, and custody records need existence/date/source status facts - content sealed; adequacy and exemptions are licensed-human judgments.",
 "04": "Family communication. Use when families need templated messages or replies need content-routing - decision communication is never templated; child data minimum-necessary in every send.",
 "05": "Forms and documents. Use when forms and records need requesting, chase, and sealed-custody inventory - medical, custody, and child-specific content is inventoried by existence, never read.",
 "06": "Tours and events. Use when tours and open houses need scheduling per published calendars with attendance facts - identical tour access; never impressions or fit commentary.",
 "07": "Waitlist management. Use when waitlists need rule-ordered entries and seat offers per the ratified priority rules - off-rule placements are integrity violations.",
 "08": "Enrollment documents. Use when enrollment packages need assembly from approved templates and human terms with gate checks - the human signs; dates and terms drive ledgers and clocks.",
 "09": "Tuition records. Use when tuition ledgers need charges, payments, and published fees with citations - discounts and aid on SIGNED authority; attendance is never cut off by automation.",
 "10": "Withdrawal and transfer. Use when exits need logistics, final-ledger facts, and sealed release packages - records release is a human act under the authorization rules.",
 "11": "Roster and capacity. Use when rosters and capacity need live math against LICENSED RATIOS - the ratio is the safety ceiling with no override path; margin flags fire before, never after.",
 "12": "Compliance and deadlines. Use when immunization windows, license renewals, and inspection clocks need instantiation and lead-time alerts - clocks are facts, filings are human.",
 "13": "Enrollment records. Use when interactions need the append-only enrollment file, verbatim lookups, and identical-process audit trails - child data minimized, medical/custody content sealed.",
 "14": "Daily operations. Use for the office morning book, end-of-day books with missed-item sweep, and clock reconciliation - ratio flags lead; books inform, the human directs.",
}'''
