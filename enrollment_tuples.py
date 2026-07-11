# enrollment-agents tuple layer.
D = {
"00": [
 ("route valid but ambiguous", "hold in clarification queue; never route on 'most likely'"),
 ("signature invalid on authority intent", "reject + integrity.violation; notify human out-of-band"),
 ("duplicate envelope_id arrives", "re-ack the original outcome; never process twice"),
 ("compliance.hold received mid-run", "suspend the named family's traffic; only 12's release or human direction resumes it"),
 ("a spoke reports done without its artifact", "treat as not-done; the artifact is the proof"),
],
"01": [
 ("family volunteers sensitive child information", "capture only the operational need, route the rest to human; minimization is the rule"),
 ("same family inquires through two channels", "one deduplicated record; identical process either way"),
 ("family asks about accommodations", "route to human immediately; accommodation conversations are never automated"),
 ("inquiry references another family's situation", "the other family's data never enters this record; cross-family references route to human"),
],
"02": [
 ("two applications compete for one seat", "both packages in receipt order with timestamps; the swarm ranks nothing"),
 ("family asks why they were not admitted", "route verbatim; decision communication is the human's, never templated"),
 ("application complete except a document in transit", "package goes with the gap named; no silent holds"),
 ("a referral source asks about an application's status", "nothing discloses; family-authorized channels only"),
],
"03": [
 ("immunization record present but adequacy unclear", "present-unreviewed, route to the licensed human; the swarm never reads the shots"),
 ("custody order arrives", "presence recorded, content sealed, human notified; its terms apply only by human reading"),
 ("prior school claims records were sent, nothing arrived", "both facts recorded; absence with the claim attached is the status"),
 ("an exemption request arrives", "route verbatim; grant/deny is a human decision"),
],
"04": [
 ("reply contains a child wellbeing or safety concern", "route to human immediately and verbatim; safety content never waits in a queue"),
 ("template merge would reveal another family's information", "hold; cross-family data in a send is the named failure"),
 ("family requests another language", "route to human for the approved-translation decision"),
 ("family requests contact stop", "honor per rule; only human-directed required notices may still send"),
],
"05": [
 ("document type unidentifiable without reading", "type-unknown, route to human; identification never excuses reading"),
 ("document arrives for the wrong child", "misdirect protocol: human immediately, incident logged"),
 ("required form missing at an enrollment gate", "the gate holds with the gap named; readiness is a fact"),
 ("a form arrives partially completed", "received-defective, re-request once with the defect named"),
],
"06": [
 ("family requests a private tour outside the calendar", "route to human; calendar exceptions are human decisions applied identically"),
 ("tour no-show asks to rebook repeatedly", "the published rebooking rule governs; the rule is the boundary"),
 ("staff share impressions after a tour", "not recorded here; the tour record carries attendance facts only"),
 ("a tour request names a specific classroom to observe", "the published tour format governs; format exceptions are human decisions"),
],
"07": [
 ("two entries tie under priority rules", "the ratified tiebreak (application timestamp) decides; never ad-hoc"),
 ("family claims a different position than the record", "the record's order stands; the claim routes with the rule math attached"),
 ("human asks to move a family up", "record and route as a policy exception; if directed, recorded with its authority - never silent"),
 ("an offer window expires during a family emergency", "the expiry fact routes to human before the next offer fires; the rule pauses on a human decision only"),
],
"08": [
 ("human terms differ from the published tuition schedule", "route back named; a nonstandard rate is a signed exception, never a quiet merge"),
 ("executed agreement returns with a handwritten change", "record as-executed, flag the delta; the record carries what was signed"),
 ("immunization gate open at the start date", "hold and escalate with the compliance clock; the gate is statutory in most jurisdictions"),
 ("an enrollment is requested that 11's capacity facts cannot seat", "the capacity fact governs; the conflict routes - the ratio has no override"),
],
"09": [
 ("family disputes a charge", "both readings preserved; the ledger reports, the human resolves"),
 ("payment arrives for a withdrawn student", "record unapplied and route; a closed ledger never silently reopens"),
 ("delinquency reaches the published exclusion threshold", "facts route to human; a child's attendance is never cut off by automation"),
 ("a signed discount references terms that changed since signing", "hold and re-confirm naming both states"),
],
"10": [
 ("receiving school requests records directly", "recorded and routed; nothing releases without authorization on file and the human's act"),
 ("withdrawal mid-billing-cycle", "proration facts per published policy; the refund decision is the human's"),
 ("custody-conflicted instructions arrive", "freeze and route to human immediately; custody conflicts are legal territory"),
 ("a release authorization is ambiguous in scope", "both readings route; a records release never proceeds on a guessed scope"),
],
"11": [
 ("a directed enrollment would exceed the licensed ratio", "refuse + integrity.violation; the ratio has no override - the safety ceiling in a classroom"),
 ("a staffing change alters the effective ratio mid-day", "capacity recomputes immediately; the change routes to human - ratios are live math"),
 ("roster and enrollment records disagree", "both facts to human; the roster never silently reconciles"),
 ("a capacity fact would open a seat for under the offer-window duration", "the fact routes with the window math; a seat that cannot survive the published window is a human call"),
],
"12": [
 ("state and local rules differ on an immunization window", "the shorter protection governs; the conflict escalates for the table"),
 ("an enrollment date is disputed", "the earlier date runs the clocks; conservatism ratified"),
 ("a certain miss emerges", "escalate immediately, quantified; early certainty is compliance"),
 ("a rule change is announced but not ratified into the table", "alert with the delta; the table changes only by ratification"),
],
"13": [
 ("two entries conflict on a material fact", "both stand; conflict flagged to the requester"),
 ("a request would unseal medical or custody content", "refuse with the seal named"),
 ("retention conflicts with an open dispute or licensing matter", "the hold wins; escalate"),
 ("storage write unconfirmed", "not done until re-verified; unconfirmed is reported failed"),
],
"14": [
 ("book source unavailable at assembly", "section marked absent; never backfilled"),
 ("EOD sweep finds an untouched morning item", "miss named with its owner; the sweep never reassigns"),
 ("human unreachable at book time", "publish to the queue and hold"),
 ("a ratio-margin flag spans the book boundary", "it leads both books until resolved; ratio state never ages into a footnote"),
],
}
