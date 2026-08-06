# Resume and Career Documents

Use this reference for resumes, career descriptions, portfolio summaries,
LinkedIn profiles, and application essays. The goal is a credible document a
recruiter and a technical interviewer can scan quickly.

Natural wording cannot repair missing evidence. Protect the claim before
polishing the sentence. Never turn a plan into completed work, a team result
into an individual result, or an unmeasured effect into a metric.

## Start with the evidence boundary

Before rewriting, identify:

1. What fact, action, result, number, and time range the source supports.
2. Whether the work was individual, led, shared, or supporting.
3. Whether a result was measured, observed without measurement, planned, or
   still unverified.
4. Which terms and project names may be disclosed.

If any boundary is missing and the rewrite would change the strength of the
claim, keep the source strength or flag the missing evidence. Do not fill the
gap with a plausible achievement.

## Conditional rewrite table

| If the source has X | Use Y | Do not |
|---|---|---|
| `저는`, `제가`, `저의` at the start of a resume bullet | Start with the problem, responsibility, action, or result | Drop the subject when that would make individual and team ownership ambiguous |
| A broad self-description such as `탁월한`, `책임감 있는`, `성장하는 개발자` | Replace it with a verified example that demonstrates the trait | Invent an example or keep unsupported self-rating as an achievement |
| `기여했다`, `고도화했다`, `강화했다`, `의미 있는 성과` | Name what changed and the confirmed result. If no result is supplied, state the action only | Add a metric, causal effect, or praise not present in the source |
| `만들었다`, `바꿨다`, `고쳤다`, `옮겼다` hides the actual action | Use the supported verb such as `설계했다`, `구현했다`, `분리했다`, `통합했다`, `이전했다`, or `제거했다` | Choose a stronger ownership verb than the evidence supports |
| `성능 개선`, `비용 절감`, `안정성 향상`, `생산성 향상` without a measurement | State the concrete change or observed behavior and mark the effect as unmeasured when necessary | Turn direction-only evidence into a percentage or firm causal claim |
| A number or score | Keep the comparison target, sample size, evaluation condition, time range, and evaluator when supplied | Detach a number from the conditions that make it interpretable |
| A team or company result | Match the verb to the person's contribution: led, shared, supported, proposed, implemented, or verified | Make the whole result sound individually owned |
| A plan, proposal, experiment candidate, or unshipped change | Use `제안했다`, `검증했다`, `후보로 확인했다`, or the exact known state | Write `구축했다`, `출시했다`, `도입했다`, or `개선했다` before completion is verified |
| Tool names or implementation units listed as the main point | Lead with the problem, judgment, or responsibility, then name the relevant technology | Use a technology inventory as proof of impact |
| Long background before the action | Move the problem and action forward; split after a complete thought if needed | Force problem, action, and result into one overloaded sentence |
| `전 과정`, `전반`, `모든 영역` | List only the stages or scope the source verifies | Use total-ownership wording as a shortcut |
| Internal AI or English terms for a general recruiter | Use plain Korean from `patterns.md` and explain what was checked or decided | Replace an exact job-posting keyword or technical name that matters for search and precision |
| A target job description is supplied | Use it to rank and phrase verified evidence by relevance | Copy a requirement into the resume as if it were the applicant's experience |
| The introduction opens with years and a tool list | Lead with the closest verified problem, design decision, or operating responsibility; keep duration and tools as support | Turn the introduction into a keyword inventory |
| Several unrelated project areas compete for space | Choose one primary axis and one supporting axis for the target role | Give every project equal weight or hide a real experience gap |
| The same sentence appears in the introduction, skills, and experience | Give each section a job: introduction for positioning, skills for tools, experience for evidence | Repeat one polished sentence across sections |
| A private or unverified project name | Use a public product name or a functional description while preserving scope | Reveal an internal code name or infer that a repository proves personal ownership |
| A future-looking `~하고자 합니다` in an achievement bullet | Use an existing action or result. Move genuine motivation to the application essay | Present intention as experience |
| Every bullet follows the same three-part mold | Keep only supported parts and vary length by meaning | Manufacture symmetry, a third item, or a result for visual consistency |

## Sentence order

Prefer this reading order when the source supports it:

1. Problem or owned scope
2. Judgment and action
3. Confirmed result

This is a reading order, not a sentence template. One bullet may contain only
an action because the result was not measured. Another may need two sentences
because the decision and its conditions matter.

## Examples

### Measured result

Before:

> 저는 캐시 전략 고도화를 통해 자체 부하 테스트 500건에서 API 응답 중앙값을 1.8초에서 1.1초로 크게 개선했습니다.

After:

> 캐시 정책을 조정해 자체 부하 테스트 500건의 API 응답 중앙값을 1.8초에서 1.1초로 줄였다.

The rewrite keeps the sample, metric, and comparison while removing first
person, abstract wording, and unsupported praise.

### Unmeasured effect

Before:

> 장애 유형별 로그를 추가해 서비스 안정성을 강화했습니다.

After:

> 장애 유형별 로그를 추가했다.

Without before-and-after evidence, keep the implemented change and remove the
unmeasured effect.

### Contribution boundary

Evidence says the person led the architecture and SDK integration while the
team shared screen implementation.

Before:

> 채팅 기능 전체를 단독으로 구현했습니다.

After:

> 채팅 구조와 SDK 연동을 주도하고 화면 구현은 팀원과 나눠 맡았다.

### Internal wording

Before:

> 모델 승격 게이트와 롤백 파이프라인을 구축했습니다.

After:

> 운영 모델의 채택 기준과 이전 버전 복구 절차를 만들었다.

If the source specifies the actual checks and automation, use those details
instead of the general nouns in either sentence.

### Missing evidence

Before:

> 다양한 프로젝트를 통해 탁월한 문제 해결 능력을 발휘해 의미 있는 성과를 만들었습니다.

Do not manufacture a polished achievement. Ask for or flag the missing problem,
action, ownership, and result. If no evidence is available, omit the claim.

## Final resume check

- Every claim stays inside the source evidence and contribution boundary.
- Team results remain team results.
- Plans, proposals, implementation, merge, release, and observed outcome remain
  distinct states.
- Metrics keep their comparison and measurement conditions.
- Unmeasured effects are not presented as facts.
- A non-specialist can explain each sentence without internal vocabulary.
- Exact job-posting terms and established technical names remain where useful.
- No private name or unsupported service classification was added.
- No U+2014 em dash or U+00B7 middle dot appears.
