# Resume Evaluation

Use this after the five general scores (Meaning Fidelity, Korean Naturalness,
Context Fit, Edit Discipline, Practical Usefulness, each 1 to 5) defined in the
k-humanizer skill's `evaluation.md`. A fabricated
fact, metric, causal effect, or ownership claim fails even when the Korean
reads naturally.

## Domain checks

- Resume/profile: Did it preserve evidence, contribution boundaries,
  measurement conditions, completion state, and public wording?
- Application writing: Does a verified experience explain the specific
  organization or role choice and a credible contribution, rather than generic
  company praise?

## Hard fails

For a resume, also cap Meaning Fidelity at 1 when the rewrite:

- Turns a team result into an individual result.
- Turns a plan, proposal, candidate, or unshipped change into completed work.
- Adds an unmeasured performance, cost, stability, or productivity effect.
- Keeps a metric but removes its comparison target, sample, or evaluator when
  that condition was supplied.
- Reveals a private project name or infers personal ownership from a repository.
- Replaces a verified method or domain term with a different one.

## Resume-specific scoring

After the five general scores, check these independently:

- **Evidence boundary**: Every claim stays within the supplied source.
- **Contribution boundary**: Individual, led, shared, and supporting work remain distinct.
- **Measurement integrity**: Numbers keep the conditions that make them interpretable.
- **Decision clarity**: The problem, judgment, action, or result is easier to find.
- **Reader fit**: Specialized or insider wording is explained for a recruiter without erasing exact domain terms.

Any fabricated fact, metric, causal effect, or ownership claim is a hard fail
even when the Korean sounds natural.

For a full resume or career document, also check:

- **Target clarity**: The top section communicates one primary direction rather
  than combining every possible role.
- **Section discipline**: The summary positions, experience proves, skills name
  relevant knowledge, and the portfolio explains contribution and judgment.
- **Evidence distribution**: The strongest direct evidence appears before
  transferable or weakly related experience.
- **Repetition control**: The same achievement is not copied across the summary,
  experience, and skills sections.
- **Output usability**: Paste-ready wording comes before diagnosis, and missing
  information is raised only when it changes a material claim.

Do not penalize structural rewriting when the user explicitly asks to compose
from notes, tailor to a posting, or review a full document. Score edit discipline
against the requested task, while holding every factual boundary constant.

## Role-specific resume checks

When `resume_role` is supplied, also check whether the rewrite answers the
role's actual hiring questions:

- Operations: repeated work, exceptions, handoffs, deadlines, and operating results.
- Planning: problem, requirement, priority, scope decision, and validation state.
- QA: scope, environment, reproduction condition, severity, release decision, and follow-up.
- Design: user task, constraint, design decision, handoff, and usability evidence.
- Marketing/content: audience, channel, hypothesis, message, attribution, and measured response.
- Customer service: customer problem, policy, response, escalation, follow-up, and confirmed outcome.
- Research/data: question, method, sample, limitation, finding, and decision supported.
- People/education: learner or team need, program decision, delivery, participation, and later adoption state.

Do not penalize a role for lacking a percentage when the source has strong
qualitative evidence. Do penalize wording that imports a role keyword without
the action, condition, or decision that would support it.
