#!/usr/bin/env python3
"""Generate the meta pre-decision layer: per-agent DECISIONS.md (tuple layer)
and SWARM.md (framework manifest + swarm-level tuples).
Tuples are (crossing, answer): the deliberation happened before the run."""
import os
from generate_skills import ROUTES, AGENTS

PKG = os.path.dirname(os.path.abspath(__file__))

SWARM_TUPLES = [
 ("two playbooks match one trigger", "run neither; clarification.request naming both"),
 ("a playbook step conflicts with an agent's legal line", "halt playbook; integrity.violation - spec defect, never a judgment call"),
 ("workload exceeds capacity", "priority order: escalations > active-transaction deadlines > client-facing requests > internal/marketing > discovery; ties go to the older item"),
 ("signed human instruction conflicts with a playbook", "signed human wins; deviation logged in the after-action report"),
 ("required data is stale beyond threshold", "regenerate; never present stale as current"),
 ("one parallel step fails mid-phase", "complete independent siblings; hold dependents; flag - never abandon the phase silently"),
 ("identical envelope arrives twice", "process once; envelope_id is the idempotency key"),
 ("uncertainty about whether a legal line is crossed", "treat as crossed; escalate"),
 ("no suitable tuple exists for the task at hand", "STOP; clarification.request to the human and wait - a missing tuple is a design omission to fix, never a license to improvise"),
 ("context fade suspected or long run", "re-read MANNERS.md and own SKILL.md before the next action"),
 ("visibility limited but the path seems clear", "proceed only within stopping distance: reversible increments; irreversible or client-visible actions wait for full verified authority"),
 ("two runs contend for the same agent", "higher priority class proceeds; the lower takes the siding - held live on route, resumes when the segment clears; contention never aborts a run"),
 ("task requires a path outside declared edges", "refuse; clarification.request - an undeclared path is ambiguity, not opportunity"),
 ("an unlisted crossing is reached", "ambiguity protocol; propose the missing tuple in the after-action report for human ratification"),
]

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

def decisions_md(num, name):
    rows = "\n".join(f"- ({c}, {a})" for c, a in D[num])
    rows += "\n\n(Root rule, restated: no suitable tuple - or an uncertain match - means STOP and ask the human.)"
    return f"""# Agent {num} - Predeliberated Decisions (Tuple Layer) v0.1 DRAFT

PRE-TEXT - ROOT OF THE TUPLE DECISION TREE (owner rule, binding):
before ANY task or decision, consult this layer. If NO suitable tuple covers
the task: STOP. Contact the human via clarification.request and wait. Do not
improvise, do not pick the nearest tuple, do not proceed on judgment - a
missing tuple is a design omission to be fixed, never a license to act. A
PARTIAL OR UNCERTAIN MATCH IS NOT-FOUND: if it takes judgment to decide the
tuple fits, it does not fit - STOP applies. The after-action proposes the
missing tuple so the omission is closed.

Meta pre-decision layer, above playbooks: crossings this agent may reach,
already deliberated. Format: (crossing, answer) - a location with its answer,
stored before the run. Swarm-wide tuples in /SWARM.md apply first; MANNERS.md
constrains everything.

{rows}
"""

def swarm_md():
    agents_list = "\n".join(f"- {a['num']} {a['name']}" for a in AGENTS)
    intents = sorted({i for i, *_ in ROUTES})
    tuples = "\n".join(f"- ({c}, {a})" for c, a in SWARM_TUPLES)
    return f"""# SWARM.md - Framework Manifest + Swarm-Level Decisions (v0.1 DRAFT)

Framework context for the dispatcher and every agent: as much predefined
structure as exists, until learning (after-action dataset) takes over.
MANIFEST SECTION IS MACHINE-GENERATED from ROUTES/AGENTS in generate_skills.py
 -  regenerate via gen_meta.py; hand-edits here will be overwritten and are a
defect, not a change.

## Manifest (generated)
- Agents: {len(AGENTS)+1} (00-dispatcher + {len(AGENTS)} spokes)
- Routes: {len(ROUTES)} entries, {len(intents)} distinct intents
- Playbooks: P01-P10 (playbooks/)
- Layer stack: MANNERS.md → DISPATCHER_CORE.md → identity/ → DECISIONS.md
  (per agent) → playbooks/ → agent SKILL.md files
- Track principle: the ROUTE-SPACE IS CLOSED. Agents run on predetermined
  track; an option absent from the routing table, playbooks, and tuples does
  not exist. Trains request routes; only the hub lines switches. Content-space
  is BOUNDED (manners, compliance verdicts) but not closed - generative freight
  is why inspection exists (11's ratio-ceiling discipline, verify_swarm, after-action).
- Routes never originate on the train: a run = a FIXED route + VARIABLE events
  (scheduled work at the stations along the line, or unforeseen events that
  trigger the restricted-speed doctrine). Agents never create routes or work
  assignments; on arrival they produce documents and evaluations from
  predetermined possibilities, autonomously, under dispatcher permission.
- Crew principle: the track cannot disobey and the train cannot disobey - the
  CREW can, and derailments are crew decisions on compliant hardware. In this
  swarm the model is the crew, not the train. Rulebooks alone never stopped
  crew-caused derailments; automated enforcement did. Every rule therefore
  ships with its enforcement twin: instruction < detection (verify_swarm,
  after-action, audit log) < structural impossibility (acks, signatures,
  closed routes). Constraint reduces variance, not bias - a wrong tuple makes
  the swarm consistently wrong, which is why spec ratification outranks spec
  volume.
- Shared-segment principle: spokes are shared track segments - concurrent runs
  (trains) traverse the same agents. The dispatcher's value concentrates where
  track is shared: sequencing, priority class, and context isolation are block
  protection for segments used by other trains.
- Spokes:
{agents_list}
- Intents: {", ".join(f"`{i}`" for i in intents)}

## Swarm-level decision tuples (predictable scenarios, pre-deliberated)
{tuples}

Status: v0.1 DRAFT - manifest verified against generator data at generation
time; not runtime-tested.
"""

def main():
    # dispatcher decisions live in its folder like every spoke's
    names = {a["num"]: a["name"] for a in AGENTS}
    names["00"] = "Dispatcher"
    slugs = {a["num"]: f'{a["num"]}-{a["slug"]}' for a in AGENTS}
    slugs["00"] = "00-dispatcher"
    for num in sorted(D):
        path = os.path.join(PKG, slugs[num], "DECISIONS.md")
        open(path, "w").write(decisions_md(num, names[num]))
    open(os.path.join(PKG, "SWARM.md"), "w").write(swarm_md())
    print(f"wrote {len(D)} DECISIONS.md + SWARM.md")

if __name__ == "__main__":
    main()
