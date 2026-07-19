# enrollment-agents - school & childcare enrollment vertical for the DispatcherAgents runtime

An **identity side-load**: everything vertical-specific for a 15-agent
school/childcare enrollment swarm, loadable into the content-neutral
[dispatcher-agents](https://github.com/QuietFireAI/dispatcher-agents) runtime.
The runtime never contains vertical text; this repo never contains transport
code. That split is the architecture.

**Status: v0.2 ratified 2026-07-18 (extended from v0.1 2026-07-11) - owner sign-off. Blueprint, not runtime-hardened. No licensed regulatory, or education/childcare-practice review has been performed.**

## What this is for

Enrollment operations support for a private school, preschool, or childcare
center: minimized-data inquiry intake, identical-format application packages,
sealed records-status tracking, published-calendar tours, rule-ordered
waitlists and seat offers, gate-checked enrollment packages, citation-clean
tuition ledgers, human-released records on withdrawal, live licensed-ratio
capacity math, the compliance clock engine, an append-only enrollment file,
and the daily books.

What it never does - the five absolute lines (identity/IDENTITY-enrollment-agent.md):

1. Identical process is the fairness guarantee - the swarm ranks nothing;
   decisions and their communication are the human's.
2. Child data is minimized and sealed - medical/custody content inventoried
   by existence, never read.
3. The licensed ratio is the safety ceiling - no override path exists.
4. No unsigned money, and automation never excludes a child.
5. Records release is a human act - authorization on file, human releases.

## Layout

| Path | What it is |
|---|---|
| `identity/routes.json` | The closed track: 31 (intent, senders, receivers) routes - single source of truth |
| `identity/priority.json` | JIT playbook priority classes (ratified 2026-07-11; extended & ratified 2026-07-18) |
| `identity/IDENTITY-enrollment-agent.md` | The identity declaration |
| `00-dispatcher/ ... 14-daily-operations/` | 15 agent SKILL.md + DECISIONS.md (tuple layer) |
| `playbooks/P01 ... P10` | Deployment playbooks: inquiry-to-application through EOD books |
| `SWARM.md` | Framework manifest + swarm-level tuples |
| `MANNERS.md` | Conduct constants, hash-registered at boot attestation |
| `TUPLE_INDEX.md` | Generated drill-down: tuple → agent → playbooks |
| `generate_skills.py` / `gen_meta.py` / `gen_playbooks.py` / `gen_tuple_index.py` | Generators - data tables are the spec; files are build artifacts |
| `verify_swarm.py` | Enforcement: tuple legality, edge completeness, regression - exit 0 = clean |

## Verify

```bash
python3 verify_swarm.py    # 0 failures, 0 warnings expected
```

## Load into the runtime

```bash
git clone https://github.com/QuietFireAI/dispatcher-agents.git
git clone https://github.com/QuietFireAI/enrollment-agents.git
cd dispatcher-agents && pip install -e ".[pillars,crypto,dev]"
```

```python
from dispatcher.loader import load_identity
ident = load_identity("/path/to/enrollment-agents")
```

The loader is fail-closed: no routes.json, no track, no load. It audits the
priority table's status on every load - never silently.

## Sibling identities

- [listing-agents](https://github.com/QuietFireAI/listing-agents) - real-estate listing vertical (ratified)
- [claim-agents](https://github.com/QuietFireAI/claim-agents) - insurance claims vertical (ratified)
- [reservation-agents](https://github.com/QuietFireAI/reservation-agents) - park/resort reservations vertical (ratified)
- medbilling-agents, mortgage-agents, property-mgmt-agents, practice-agents - prior drop
- freight-agents, hr-agents - this drop's siblings

## License

Dual-licensed under the **QuietFire Identity License** (see `LICENSE`) over
an **AGPL-3.0** floor (see `LICENSE-AGPL`). Evaluation, development, and
internal testing — including cloning, running the suite, and any demo — are
free. **Production and commercial use require a paid license from
QuietFireAI or full AGPL-3.0 compliance.** Building derivative identities
for third parties is not permitted without a commercial license. The
supported commercial operating environment is TelsonBase. The open chassis
this runs on (dispatcher-agents) is Apache-2.0 and separate.

*License text is a placeholder pending counsel review.*
