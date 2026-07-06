# Dataset Research

Last checked: 2026-07-04.

This project should not redistribute third-party text unless the license and attribution path are clear. Prefer using public datasets for evaluation prompts, style analysis, and benchmark inspiration.

## Strong Candidates

### coastral/korean-writing-style-instruct

URL: https://huggingface.co/datasets/coastral/korean-writing-style-instruct

Use for:
- Korean style categories
- Prompt patterns for style and register transfer
- Synthetic examples for non-private validation

Notes:
- Hugging Face API reports `license:apache-2.0`.
- Synthetic dataset; useful for breadth, not a gold standard for human naturalness.

### jojo0217/korean_safe_conversation

URL: https://huggingface.co/datasets/jojo0217/korean_safe_conversation

Use for:
- Casual conversation and messenger-like wording reference
- Natural daily dialogue examples

Notes:
- Hugging Face API reports `license:apache-2.0`.
- The dataset card says parts are based on public Korean corpora and AI Hub-derived sources; verify provenance before redistributing derived samples.

### KatFish / KatFishNet

Paper: https://arxiv.org/abs/2503.00032

GitHub: https://github.com/Shinwoo-Park/katfishnet

Use for:
- Korean AI-tell feature categories
- Punctuation, spacing, and POS diversity references
- Benchmark framing for human vs LLM-generated Korean

Notes:
- This is directly relevant to Korean AI-text detection research.
- Use as research grounding. Do not copy dataset content until license is confirmed from the repo.

## Secondary Candidates

### devngho/korean-instruction-mix

URL: https://huggingface.co/datasets/devngho/korean-instruction-mix

Use for:
- Instruction-style Korean outputs
- Broad prompt coverage

Notes:
- Hugging Face API reports `license:cc-by-sa-4.0`.
- Mixed source dataset; attribution and share-alike implications need care.

### heegyu/open-korean-instructions

URL: https://huggingface.co/datasets/heegyu/open-korean-instructions

Use for:
- General Korean instruction patterns

Notes:
- Hugging Face API reports `license:mit`.
- It is broad instruction data, not specifically natural Korean writing.

## Existing Projects To Acknowledge

### DaleSeo/korean-skills

URL: https://github.com/DaleSeo/korean-skills

Includes a Korean `humanizer`, grammar checker, and style guide. Good reference for ecosystem positioning.

### epoko77-ai/im-not-ai

URL: https://github.com/epoko77-ai/im-not-ai

Large Korean AI-tell rewriting harness. Strong existing project; K-Humanizer should avoid competing only on "AI smell removal" and instead emphasize practical Korean writing polish by genre.

### dotoricode/korean-humanizer

URL: https://github.com/dotoricode/korean-humanizer

Portable Korean humanizer prompt/skill. Useful comparable project for packaging and README clarity.

## Dataset Decision

For v0.1:
- Do not download or vendor datasets.
- Use the hand-authored anonymized v0 golden set in `evals/fixtures/golden_set.v0.jsonl`.
- Link to public datasets only as research references.

For v0.2:
- Add a script that can optionally sample public datasets locally.
- Keep downloaded data under `evals/datasets/`, which is gitignored.
- Save only aggregate evaluation reports in git.
