# Reliquary of Truth — Demo Repository

This repository is a **demonstration target** for the Reliquary of Truth engine.

It intentionally starts as a simple application so the engine can:
- Accept a task
- Plan changes
- Implement code
- Run tests
- Produce verifiable proof (diffs + test results)

## Demo Scenario

**Task**
> Add a `/health` endpoint that returns `{ "ok": true }` and add a test for it.

**What Happened**
- Reliquary generated a plan
- Implemented the endpoint
- Added tests
- Ran the test suite
- Produced a clean, reviewable diff

## Why This Repo Exists

This repo proves:
- Reliquary works on *real code*
- Output is auditable
- Changes are test-backed
- No silent hallucinations

## How to Use

```bash
python -m reliquary --repo . --task "Your task here"
```

This repo will evolve as more complex scenarios are tested.