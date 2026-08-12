# Resume Workflow

Use this reference with `resume.md` for every resume, career description,
portfolio summary, LinkedIn profile, or application-writing task. It converts
source material into a usable document without filling evidence gaps with
plausible claims.

## Choose the task before editing

| Input | Task | Default response |
|---|---|---|
| One or more finished bullets | Polish wording while preserving scope and strength | Return paste-ready bullets. Explain only a material claim issue. |
| Raw notes, meeting notes, or a task list | Extract evidence and compose bullets | Return the safest usable wording, then list only evidence gaps that affect it. |
| A job posting and existing experience | Tailor verified evidence to the role | Choose one primary role and at most one supporting role, then reorder and rewrite the relevant sections. |
| A complete resume or career document | Review structure and rewrite weak sections | Organize the result by document section. Separate ready wording, evidence gaps, and content to remove or move. |
| A request to make text sound natural | Humanize only | Follow the normal change budget. Do not reorganize the document unless requested. |

If the user requests composition, restructuring, or a role-targeted rewrite, a
change over 50% can be appropriate. The evidence boundary still applies even
when the wording and order change substantially.

## Build an evidence record

For each experience, extract only what the source supports:

| Field | Question | Safe handling when missing |
|---|---|---|
| Problem or scope | What work, user problem, repeated task, or decision was involved? | Keep the known task. Do not invent urgency or business importance. |
| Judgment | What priority, policy, option, standard, or design choice did the person make? | State the action only. Do not imply strategic ownership. |
| Action | What did the person actually do? | Ask for the action if the source contains only a trait or result. |
| Ownership | Was the work individual, led, shared, or supporting? | Use neutral wording or flag the boundary. Never default to sole ownership. |
| State | Was it proposed, approved, piloted, implemented, released, or verified later? | Keep the latest confirmed state. |
| Result | What changed or was learned? | A clear action or decision can stand without a result. |
| Measurement | Compared with what, over which period, sample, environment, or evaluator? | Keep the number attached to known conditions or omit the unsupported interpretation. |
| Disclosure | Which names, customers, figures, or internal methods may be public? | Generalize the name while preserving the functional scope. |

Do not show this table automatically. It is an internal writing aid unless the
user asks to inspect the evidence.

## Give each section one job

### Summary

Use two or three compact sentences when enough evidence exists. Establish the
target work, the closest verified scope, and one differentiating way of working
or result. Do not open with a tool inventory, a personality claim, or an
aspiration such as `성장하고 싶은 인재입니다`.

For people moving between fields, lead with transferable work already done. Do
not rename the previous job or imply experience in a new field that the source
does not support.

### Experience

- Give each bullet one main point.
- Lead with a responsibility, decision, action, or confirmed result that matters
  to the target role.
- Keep background only when the action is hard to understand without it.
- Use a second sentence when ownership, conditions, or follow-up would make one
  sentence overloaded.
- Vary bullet length by evidence. Do not force every bullet into the same mold.

### Projects and portfolio

State the project context, personal contribution, important judgment, output,
and confirmed response. For design, planning, research, or QA work, the reason
for a decision may be more useful than a tool list or a raw output count.

Images, links, screens, reports, prototypes, test records, policies, and
operating documents are evidence only when the source connects them to the
person's contribution. A repository or file does not prove sole ownership.

### Skills and tools

Keep exact names that help search or establish domain familiarity. Group them
by how they were used when the source supports that distinction. Do not assign
unverified proficiency levels or repeat tools in every experience bullet.

### Education, certificates, and activities

Keep names, dates, status, and scope factual. Move an activity into experience
or projects only when the work itself is supported. Attendance alone is not a
project result.

### Application writing

Use complete sentences and the applicant's actual motivation. Connect a real
experience to the organization's stated work and the contribution the applicant
can credibly make. Do not turn admiration for the company or a job-posting
phrase into personal evidence.

## Prioritize for the target role

Read `resume-roles.md` when a target role or job description is available.

1. Extract the posting's actual responsibilities, expected decisions, and
   evidence requirements.
2. Mark each supplied experience as direct evidence, transferable evidence, or
   unsupported.
3. Put direct evidence first. Use transferable evidence only when the connection
   can be explained without changing the facts.
4. Keep a genuine gap visible. Do not cover it with a keyword or a stronger job
   title.
5. Remove details that consume space without helping the target reader judge the
   work.

For mixed roles, choose one primary role and one supporting role. For example,
an operations applicant may use planning experience to show policy decisions,
but the document should still read as an operations resume rather than eight
different resumes combined.

## Common resume failures

| Failure | Better handling |
|---|---|
| Every bullet starts with a tool or task | Lead with the work, judgment, or result the tool supported. |
| Every bullet needs a percentage | Keep qualitative evidence when the method, decision, or verified state is meaningful. |
| A job-posting keyword is repeated as a trait | Use it once beside an experience that proves it. |
| `협업`, `소통`, or `문제 해결` stands alone | Name the handoff, disagreement, customer request, decision, or follow-up already in the source. |
| One achievement appears in the summary, skills, and experience | Keep positioning in the summary, names in skills, and evidence in experience. |
| Technical detail dominates a non-technical role | Explain the operating, planning, QA, design, customer, or research decision first. Keep only technical detail that proves it. |
| All bullets are noun phrases | Use complete predicates for experience and judgment. Reserve noun phrases for compact lists. |
| The candidate is changing fields | Show transferable responsibilities without relabeling past experience. |

## Output patterns

### Finished bullets

Return the revised bullets first. Add a short note only if a claim was weakened,
removed, or left unresolved for evidence safety.

### Raw notes with a safe draft

```markdown
수정본:
[paste-ready wording]

확인 필요:
- [one missing fact that would materially change the claim]
```

Do not add `확인 필요` when the current wording is already accurate and usable.

### Full resume review

```markdown
[section name]

바로 사용:
[paste-ready wording]

근거 보완:
- [experience and the exact missing boundary]

삭제 또는 이동:
- [repetition, unsupported claim, or misplaced content]
```

Use only the headings needed for the document. Keep the rewritten document
ahead of the review notes.

## Final document check

- The first screen or top third communicates one clear target direction.
- The first two experience bullets answer the target role's main hiring questions.
- Every claim maps to supplied evidence.
- Ownership and completion state stay visible.
- Numbers retain their comparison and measurement conditions.
- Each section adds new information.
- The document does not depend on personality claims or job-posting keywords.
- Non-technical roles are not forced into engineering language or a metric-only
  achievement formula.
- The result is concise enough to scan and specific enough to discuss in an
  interview.
