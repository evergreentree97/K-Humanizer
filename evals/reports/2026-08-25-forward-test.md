# Accumulated-Knowledge Forward Test

Date: 2026-08-25

Status: Passed

Reviewer: independent Codex subagent without access to the implementation diff
or audit conclusions

## Scope

This focused test covers the five behaviors added or clarified in the current
change:

1. Public-post verbs and evidence strength
2. Application motivation without invented company facts
3. Compact Korean resume bullet endings
4. First-use explanation for mixed audiences
5. Evidence boundaries in a public validation update

This is a focused forward test, not the full 220-case scored baseline.

## Results

### 1. Public post

Input:

> 고객 답변 8만 건을 훑으며 4,200개 표현을 고쳐 얻은 노하우가 어색한 문장의 본질을 가립니다. 한국어 AI 글쓰기의 판도를 바꿀 결과에 공감하시나요?

Output:

> 고객 답변 8만 건을 검토하며 4,200개 표현을 고쳤습니다. 그 과정에서 한국어 AI 글쓰기의 어색한 표현을 가려내는 기준을 익혔습니다.

Scores: meaning fidelity 4, Korean naturalness 5, context fit 5, edit discipline
5, practical usefulness 5.

The output removed the unsupported market-changing claim and engagement prompt.
It kept `가려내다` because identifying awkward expressions is a natural
subject-action pairing here. This confirms that the guidance behaves as a
context check rather than a word blacklist.

### 2. Application motivation

Input:

> 귀사의 혁신적인 비전에 매료되어 지원했습니다. 대학 축제에서 참가자 문의를 분류한 경험을 바탕으로 고객지원 직무에서 회사의 성장에 크게 기여하겠습니다.

Output:

> 대학 축제에서 참가자 문의를 분류한 경험을 고객지원 업무에 이어가고자 귀사에 지원했습니다. 입사 후에는 이 경험을 고객 문의를 유형별로 정리하는 데 활용하겠습니다.

Scores: meaning fidelity 4, Korean naturalness 5, context fit 4, edit discipline
5, practical usefulness 4.

The source did not contain organization-specific information. The output kept
the verified experience and role connection instead of inventing a company
fact. A stronger organization-specific paragraph still requires an official
source or user-provided detail.

### 3. Resume bullet style

Input:

> 소개: Android 기능을 설계하고 운영 문제를 해결해 온 개발자입니다.
>
> 경력:
> - 결제 오류 재현 조건 정리 및 수정 후 실기기 검증했습니다
> - API 오류 응답을 화면 상태로 연동하고 재시도 동작 구현

Output:

> 소개: Android 기능을 설계하고 운영 중 발생한 문제를 해결해 온 개발자입니다.
>
> 경력:
> - 결제 오류 재현 조건 정리 및 수정 후 실기기 검증
> - API 오류 응답과 화면 상태 연동 및 재시도 동작 구현

Scores: meaning fidelity 5, Korean naturalness 5, context fit 5, edit discipline
5, practical usefulness 5.

The introduction kept a complete predicate while both compact career bullets
used consistent action-noun endings.

### 4. Mixed-audience terminology

Input:

> TTFT(Time To First Token)는 첫 응답 대기 시간을 의미합니다. 이번 측정에서는 TTFT(Time To First Token)가 1.8초였고 `TTFT_P95`는 2.4초였습니다.

Output:

> TTFT(Time To First Token)는 첫 응답이 시작될 때까지 걸리는 시간입니다. 이번 측정에서 TTFT는 1.8초였고 `TTFT_P95`는 2.4초였습니다.

Scores: meaning fidelity 5, Korean naturalness 5, context fit 5, edit discipline
5, practical usefulness 5.

The exact identifier survived, and the English expansion appeared only at first
use.

### 5. Public evidence boundaries

Input:

> 합성 예시 220개로 파일 구조와 항목 수를 검증했습니다. 실제 사용자 만족도 조사는 아직 하지 않았지만 이 결과로 자연스러움까지 완전히 입증했습니다.

Output:

> 합성 예시 220개로 파일 구조와 항목 수를 검증했습니다. 실제 사용자 만족도 조사는 아직 진행하지 않아 이번 결과만으로 자연스러움까지 입증했다고 보기는 어렵습니다.

Scores: meaning fidelity 5, Korean naturalness 5, context fit 5, edit discipline
5, practical usefulness 5.

The output separated structural validation from unmeasured naturalness and user
satisfaction.

## Verdict

No blocking behavior failure appeared in the five focused cases. Two outputs
scored 4 on at least one dimension because the source lacked a supportable
market claim or organization-specific reason. The skill narrowed those claims
instead of inventing missing evidence.
