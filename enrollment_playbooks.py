# enrollment-agents playbooks P01-P10.
PB = [
 dict(num="P01", slug="inquiry-to-application", name="Inquiry to Application",
  desc="Swarm deployment: family inquiry to a complete, identical-format application package for the human's decision. Agents 01, 02, 06, 03, 04, 13. Identical process for every family - the decision and its communication are the human's.",
  trigger="`inquiry.captured` lands at 02.",
  pre=["Published program facts current; child-data minimization applied at capture (01's rule)."],
  phases=[
   ("Phase 1 - Engage", [
    ("1","06","Schedule the tour per the published calendar","`tour.event` → 02, 13","attendance facts, never impressions"),
    ("2","04","Process communications on identical templates","`family.message.send`","sends logged"),
   ]),
   ("Phase 2 - Package", [
    ("3","03","Required-records status facts (content sealed)","`records.verify.result` → 02, 13","item-level status, adequacy human"),
    ("4","02","Assemble the identical-format application package","`application.package` → human, 13","the human decides; the swarm ranks nothing"),
   ]),
  ],
  gates=["Identical process, identical package format, for every family - deviation is the named fair-process failure.",
         "Protected-characteristic and accommodation content routes to the human verbatim, never processed."],
  completion="Application package delivered in the identical format with records status and tour facts attached.",
  abort=["Sensitive child information surfaces: minimize, seal, route; the process continues identically or pauses on the human."]),

 dict(num="P02", slug="acceptance-to-enrollment", name="Acceptance to Enrollment",
  desc="Swarm deployment: the human's acceptance to an executed, gate-clean enrollment with ledger and clocks armed. Agents 02, 08, 03, 05, 09, 11, 12, 04, 13. Gates hold with names; ratios have no override.",
  trigger="The human's acceptance decision fires `enroll.request` at 08.",
  pre=["Capacity fact from 11 seats the enrollment (the ratio is physics); terms are the human's decision."],
  phases=[
   ("Phase 1 - Package and sign", [
    ("1","08","Assemble the enrollment package: template + terms + forms checklist","`enroll.package` → human, 13","signature-ready; gaps named"),
    ("2","05","Enrollment forms chase and sealed inventory","`forms.received` → 03, 08, 13","gates fact-tracked"),
    ("3","03","Records gates (immunization status) checked","`records.verify.result` → 08, 13","statutory gates visible"),
   ]),
   ("Phase 2 - Record and arm", [
    ("4","08","Record the executed enrollment - terms verbatim, dates exact","`enroll.record` → 09, 11, 12, 13","ledger, roster, and clock basis set"),
    ("5","12","Immunization and paperwork clocks armed","`deadline.alert` (at lead-times)","clocks live"),
    ("6","04","Welcome and start-date communications","`family.message.send`","sends logged"),
   ]),
  ],
  gates=["No enrollment completes over an open statutory gate absent the human's recorded exception.",
         "No enrollment exceeds a licensed ratio - refuse + integrity.violation; no override exists."],
  completion="Enrollment executed and recorded; ledger opened, roster updated, clocks armed.",
  abort=["Immunization gate open at start date: hold + escalate with the compliance clock attached."]),

 dict(num="P03", slug="waitlist-cycle", name="Waitlist Cycle",
  desc="Swarm deployment: capacity opening to a rule-ordered seat offer with the window run per policy. Agents 07, 11, 02, 04, 13. The order is rule arithmetic; off-rule placements are integrity violations.",
  trigger="`capacity.status` from 11 opens a seat, or a new `waitlist.entry` arrives.",
  pre=["The ratified priority rules and offer-window policy are current."],
  phases=[
   ("Order and offer", [
    ("1","07","Order the list per the ratified rules; ties break on the ratified tiebreak","(order state)","rule math on facts"),
    ("2","07","Issue the seat offer with the published window","`seat.offer` → 02, 13","offer + window on record"),
    ("3","04","Offer notification on identical templates","`family.message.send`","sends logged"),
    ("4","07","Expired windows move to the next rule-ordered family, history recorded","(next offer)","no silent skips, no silent holds"),
   ]),
  ],
  gates=["No off-rule ordering or placement - an exception is a human's recorded, authority-attached decision.",
         "Waitlist positions of other families are never disclosed."],
  completion="Seat offered per the rules; acceptance flows to enrollment (P02) or the next offer fires with history intact.",
  abort=["A directed off-rule placement without recorded authority: refuse + integrity.violation."]),

 dict(num="P04", slug="records-compliance-cycle", name="Records Compliance Cycle",
  desc="Swarm deployment: statutory records gates (immunization, required documents) tracked from enrollment to closed, with sealed custody throughout. Agents 03, 05, 12, 04, 13. Adequacy is a licensed judgment; the swarm tracks existence.",
  trigger="`enroll.record` arms the compliance clocks; `deadline.alert` drives the cycle.",
  pre=["The jurisdiction rule table (immunization windows, required documents) is owner-ratified."],
  phases=[
   ("Track to closed", [
    ("1","12","Clocks per enrollment; alerts at lead-times","`deadline.alert` → 02, 03","statutory windows visible"),
    ("2","05","Chase and inventory records - sealed custody","`forms.received` → 03, 13","existence facts, content sealed"),
    ("3","03","Status against the checklist; adequacy questions to the licensed human","`records.verify.result` → 02, 08, 13","present-unreviewed routes, never self-cleared"),
    ("4","04","Family deadline notices on approved templates","`family.message.send`","notices logged"),
   ]),
  ],
  gates=["Medical content is never read by the swarm - existence, date, source only; adequacy is licensed.",
         "A certain statutory miss escalates before it lands."],
  completion="Records gates closed by human/licensed review with the trail on record, or open gates named with clocks visible.",
  abort=["Exemption request arrives: route verbatim; the clock stays visible while the human decides."]),

 dict(num="P05", slug="tuition-cycle", name="Tuition Cycle",
  desc="Swarm deployment: enrollment terms to a clean ledger - charges, payments, statements, published fees, signed-authority exceptions. Agents 09, 04, 12, 13. A child's attendance is never cut off by automation.",
  trigger="`enroll.record` opens the ledger; the published billing cycle drives it.",
  pre=["The published fee schedule and delinquency rules are the ratified versions."],
  phases=[
   ("Run the ledger", [
    ("1","09","Charges per enrollment terms and the published schedule; payments recorded","`tuition.record` → 13","citations per line"),
    ("2","04","Statement cycle on identical templates","`family.message.send`","statements logged"),
    ("3","09","Discounts/aid/arrangements ONLY on signed authority","(record with authority envelope_id)","no unsigned money"),
    ("4","09","Delinquency per published rules; enrollment-affecting consequences route to the human","(facts to human at thresholds)","automation never excludes a child"),
   ]),
  ],
  gates=["No discount, aid, or arrangement beyond published policy without signed `discount.authority`.",
         "Any consequence touching a child's attendance is a human decision."],
  completion="Ledger current with citations; exceptions authority-attached; threshold cases in the human queue.",
  abort=["Ledger dispute: both readings preserved and routed; the ledger never adjudicates."]),

 dict(num="P06", slug="withdrawal-transfer-cycle", name="Withdrawal & Transfer Cycle",
  desc="Swarm deployment: family withdrawal notice to a clean exit - final ledger facts, sealed release package, human-released records. Agents 10, 02, 05, 09, 04, 13. What leaves the building is a human decision with authorization on file.",
  trigger="`withdrawal.open` at 10 from the pipeline's routing of family notice.",
  pre=["Release-authorization rules loaded; the exit checklist is the ratified version."],
  phases=[
   ("Phase 1 - Exit logistics", [
    ("1","10","Run the exit checklist; final-ledger and proration facts assembled per policy","(facts via records + 09)","refund decision facts ready for the human"),
    ("2","05","Exit forms and release authorizations","`forms.received` → 03, 08, 13","authorization status on record"),
   ]),
   ("Phase 2 - Release", [
    ("3","10","Assemble the sealed release package + authorization status","`release.package` → human, 13","the human releases; the swarm assembles"),
    ("4","04","Exit process communications","`family.message.send`","sends logged"),
   ]),
  ],
  gates=["No records release without the authorization on file AND the human's act.",
         "Custody-conflicted instructions freeze the process and route immediately."],
  completion="Exit complete: ledger closed with facts for the refund decision, release package human-released, roster updated.",
  abort=["Ambiguous release scope: both readings route; nothing releases on a guessed scope."]),

 dict(num="P07", slug="capacity-ratio-watch", name="Capacity & Ratio Watch",
  desc="Swarm deployment: continuous roster and licensed-ratio math with lead-margin flags and zero override paths. Agents 11, 07, 02, 14, 13. The licensing ratio is the safety ceiling - capacity above it does not exist in this swarm.",
  trigger="Continuous: every `enroll.record`, withdrawal, and staffing-input change recomputes.",
  pre=["Licensed ratios and configured caps are owner-ratified; staffing inputs current per rule."],
  phases=[
   ("Continuous - the watch", [
    ("1","11","Recompute capacity per class/room on every roster or staffing fact","`capacity.status` → 02, 07, 13","live math, never enrollment-time math"),
    ("2","11","Lead-margin flags before any room approaches its ratio","(flags at configured margin)","before, never after"),
    ("3","07","Openings feed the waitlist cycle (P03)","(via capacity facts)","seats fill by rule"),
    ("4","14","Ratio state into the books; margin flags lead until resolved","(book sections)","ratio state never a footnote"),
   ]),
  ],
  gates=["A directed enrollment exceeding a licensed ratio is refused + integrity.violation - no override path exists.",
         "Mid-day staffing changes recompute immediately and route."],
  completion="Continuous playbook: capacity facts live per licensed ratios; openings flowing to the waitlist by rule.",
  abort=["Roster/enrollment record conflict: both facts route; the roster never silently reconciles."]),

 dict(num="P08", slug="licensing-compliance-watch", name="Licensing Compliance Watch",
  desc="Swarm deployment: facility license renewals, mandated inspections, and configured staff-certification clocks tracked at lead-time. Agents 12, 05, 14, 13. Every external filing is a human act.",
  trigger="Continuous: renewal and inspection clocks per the ratified jurisdiction table.",
  pre=["The jurisdiction rule table is owner-ratified and current."],
  phases=[
   ("Continuous - the watch", [
    ("1","12","Track license renewals, inspection windows, configured certifications","`deadline.alert` → 14 (lead-times)","windows visible ahead"),
    ("2","05","Renewal paperwork chased and inventoried","`forms.received` → 03, 13","artifacts on record"),
    ("3","12","Holds on actions that would violate a licensing rule","`compliance.hold` → queue","violations held, not discovered"),
   ]),
  ],
  gates=["No filing or response to a licensing authority from the swarm - human acts with the packages assembled.",
         "Certain misses escalate the moment they are certain."],
  completion="Continuous playbook: licensing clocks visible at lead-time; renewal artifacts inventoried; holds enforced.",
  abort=["Jurisdiction-table gap: clocks run on the most conservative known rule; the gap escalates for ratification."]),

 dict(num="P09", slug="morning-operations", name="Morning Operations",
  desc="Swarm deployment: the office's morning book. Today's tours, pipeline and waitlist states, open gates on starting students, ratio state, compliance clocks. Agents 14, 13, 12.",
  trigger="Scheduled daily start (owner-configured time) or owner command.",
  pre=["EOD books from the previous day exist (P10 completion on the log); if absent, the book runs with the gap NAMED."],
  phases=[
   ("Assemble (parallel, all to human review)", [
    ("1","14","Pull tours, pipeline/waitlist states, open enrollment gates, ratio state","`record.request` → 13","sections sourced; ratio flags lead"),
    ("2","14","Today's clock alerts: immunization, licensing, billing","(from 12's alert stream)","clock section current with lead-times"),
   ]),
   ("Present", [
    ("3","14","Deliver the morning book; unavailable sources marked absent","`report.package` → human","book delivered; the human directs"),
   ]),
  ],
  gates=["A source unavailable at assembly is a named absence - never yesterday's numbers backfilled."],
  completion="Morning book delivered with every section sourced or marked absent; ratio flags lead.",
  abort=["Record source down: section marked absent; the book still delivers on time."]),

 dict(num="P10", slug="end-of-day-books", name="End-of-Day Books",
  desc="Swarm deployment: the closing books. Applications moved, enrollments executed, offers out, withdrawals, clock reconciliation, the missed-item sweep. Agents 14, 13, 12. Gaps named.",
  trigger="Scheduled day end (owner-configured time) or owner command.",
  pre=["The morning book (P09) exists as the sweep baseline; if absent, the sweep names that first."],
  phases=[
   ("Assemble", [
    ("1","14","Pull the day's activity: applications, enrollments, offers, withdrawals, tuition","`record.request` → 13","activity sections sourced with timestamps"),
    ("2","14","Clock reconciliation: satisfied, at-risk, missed - quantified with owners","(from 12's stream + records)","reconciliation complete"),
    ("3","14","Missed-item sweep against the morning book","(sweep vs. P09 baseline)","sweep complete; no silent reassignment"),
   ]),
   ("Present", [
    ("4","14","Deliver the EOD books","`report.package` → human","books delivered; P10 completion logged for tomorrow's P09"),
   ]),
  ],
  gates=["The sweep never reassigns - it names. Reassignment is the human's morning decision.",
         "Ratio-margin flags lead both books until resolved."],
  completion="EOD books delivered; sweep complete with owners named; completion event logged.",
  abort=["Morning baseline absent: the sweep names that first and proceeds on records alone."]),

 dict(num="P11", slug="safeguarding-handoff", name="Safeguarding Handoff",
  desc="Swarm deployment: safeguarding concern detected anywhere to verbatim human handoff, sealed record, ops visibility. Agents 01/04/06 (detection), 13, 14. The swarm's entire role is the handoff: no questions, no statements, no visible change in posture - what happens next is the human's alone.",
  trigger="`safeguarding.notice` from intake (01), family channel (04), or tours/events (06).",
  pre=["The concern is captured verbatim with source, timestamp, and child/family reference - the human receives the words, not a summary."],
  phases=[
   ("Phase 1 - Handoff (same turn)", [
    ("1","01/04/06","Route the concern verbatim; the routine conversation neither references it nor halts conspicuously","`safeguarding.notice` \u2192 human, 13, 14","verbatim record delivered, human alerted"),
    ("2","14","Ops visibility same turn; nothing about it appears in routine reporting beyond the handoff fact","(ops log)","daily book shows the handoff happened"),
   ]),
   ("Phase 2 - Sealed record", [
    ("3","13","Sealed record entry - verbatim, access itself logged","`interaction.log` (sealed handling)","record complete; reads are audited"),
   ]),
  ],
  gates=["No agent asks follow-up questions, makes statements, or visibly changes posture toward the family - investigation, notification, and mandated reporting are human decisions under law.",
         "The record is sealed: routine reports carry the handoff fact only, never the content."],
  completion="Verbatim handoff delivered same turn, sealed record complete, ops aware of the handoff fact; the human owns everything after.",
  abort=["Ambiguity about whether something is a safeguarding concern: hand it off - the conservative read is the only read.",
         "The concern implicates staff: identical handoff, zero internal routing beyond human and sealed record."]),

 dict(num="P12", slug="custody-change-wave", name="Custody Change Wave",
  desc="Swarm deployment: stated or documented custody/authorization change to a re-anchored record with human-approved effect. Agents 01/04/05 (detection), 02, 10, 13. The swarm never adjudicates custody: statements are noticed, documentation is inventoried, and only human approval moves the record.",
  trigger="`custody.notice` from intake (01), family channel (04), or received documentation (05).",
  pre=["The prior authorization facts (pickup list, records access, financial responsibility) are on record - a change is only a change against a recorded baseline."],
  phases=[
   ("Phase 1 - Notice and freeze the ambiguity", [
    ("1","01/04/05","Notice verbatim with source; documentation inventoried existence/type/date/source","`custody.notice` \u2192 02, 10, 13","notice on record; nothing changed yet"),
    ("2","02","Pending offers, releases, and disclosures re-check against the notice before moving","(hold where affected)","no affected action proceeds on the old facts"),
   ]),
   ("Phase 2 - Human-approved effect", [
    ("3","10","Release/records posture re-anchored only on verified documentation + human approval","`release.package` \u2192 human (where releases pend)","human decision on record"),
    ("4","13","The change, its documentation, and the approval recorded as one auditable unit","`interaction.log`","who changed what, on whose approval, citing what"),
   ]),
  ],
  gates=["The swarm never decides who has custody - a stated change freezes affected ambiguity; only verified documentation plus human approval changes pickup, access, or disclosure.",
         "Both parents/guardians retain their existing recorded rights until the human rules - a notice is not a verdict."],
  completion="Every affected pending action re-checked, the record changed only under human approval with documentation cited, the full unit auditable.",
  abort=["Conflicting custody claims arrive: both recorded verbatim; all affected actions hold; human immediately - conflicts are legal territory.",
         "A pickup situation is live while ambiguity stands: human immediately, same turn - safety over process, always."]),

 dict(num="P13", slug="refund-tuition-reconciliation", name="Refund & Tuition Reconciliation",
  desc="Swarm deployment: withdrawal refund from published schedule to signed execution with books at $0.00. Agents 10, 09, 04, 13. Refunds are money: the schedule computes, the human signs, the books reconcile to the penny.",
  trigger="Withdrawal completes (P06) with a refundable balance per the published tuition schedule, or `reconciliation.exception` surfaces a credit.",
  pre=["The published tuition schedule and the family's payment record are both on file - the refund is arithmetic shown, never judgment applied."],
  phases=[
   ("Phase 1 - Compute and package", [
    ("1","09","Refund computed from the published schedule; every number carries its source","`tuition.record` \u2192 13","computation on record"),
    ("2","09","Package to human: schedule citation, payments, computed refund","`reconciliation.exception` \u2192 human, 13 (as the money package)","package delivered"),
   ]),
   ("Phase 2 - Signed execution", [
    ("3","09","Refund executes only on signed authority","(await `refund.authority` \u2190 human)","signed envelope on the chain first"),
    ("4","04","Family informed from posted facts once executed","`family.message.send` \u2192 external","templated notice, facts only"),
    ("5","09","Books reconcile to $0.00 or the variance escalates","`reconciliation.exception` \u2192 human, 13 (if any variance)","clean books or a named exception"),
   ]),
  ],
  gates=["No refund executes unsigned - refund.authority is money, same doctrine as discount.authority.",
         "The $0.00 rule governs: any variance between schedule, payments, and executed refund is an exception, never absorbed."],
  completion="Refund executed on signed authority per the published schedule, family informed, books at $0.00; or the blocking question named to the human.",
  abort=["Family disputes the schedule computation: the dispute routes verbatim with the arithmetic attached - the swarm shows its work and stops.",
         "Financial responsibility is under a custody conflict (P12): the refund holds until the human rules on payee."]),

 dict(num="P14", slug="records-request-response", name="Records Request Response",
  desc="Swarm deployment: external records request (agency, receiving school, parent) to human-approved disclosure inside the clock. Agents 13, 12, 05, 04. Every item is custody-flagged; release is a human decision - a records request about a child is never routine.",
  trigger="External records request lands via 04 (family channel) or intake (01); agency/compliance requests via 12.",
  pre=["The request is captured verbatim with date, requester, claimed relationship/authority, scope, and the applicable response window."],
  phases=[
   ("Phase 1 - Clock and inventory", [
    ("1","12","Response clock armed (jurisdictional default if none stated)","`deadline.alert` \u2192 14 (at lead-times)","clock live"),
    ("2","13","Disclosure inventory: existence, type, date, source per item - custody flags named per item","`records.disclosure.package` \u2192 human, 12","inventory delivered inside lead-time"),
    ("3","05","Documentation supporting the requester's authority inventoried (never adjudicated)","`forms.received` \u2192 03, 13 (references)","authority-support status per requester"),
   ]),
   ("Phase 2 - Human release", [
    ("4","13","Record the human's release decision and what was disclosed","`record.response` + `interaction.log`","itemized: who, what, when, under whose approval, custody check noted"),
    ("5","04","Transmit per the approved scope","`family.message.send` \u2192 external (or agency channel per direction)","transmission artifact on record"),
   ]),
  ],
  gates=["Nothing beyond the human's itemized approval is disclosed - the approval is the ceiling.",
         "Requester authority is never adjudicated by the swarm - custody flags and supporting documentation go to the human; the decision is theirs (P12 doctrine).",
         "A noticed custody change freezes affected disclosures until the human rules."],
  completion="Human-approved disclosure transmitted inside the clock with a complete itemized, custody-checked record; or refusal/clarification recorded the same way.",
  abort=["Requester's claimed authority conflicts with the record: human immediately with both facts - never split the difference.",
         "Request arrives under legal process (subpoena, court order): counsel's lane - the swarm inventories and waits for direction."]),
]
