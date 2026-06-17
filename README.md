# card-pilot parallel demo

A sandbox that exercises the [card-pilot-toolkit](https://github.com/liminalarc/card-pilot-toolkit)
**trunk-based parallel** flow on a real (tiny) app, so the commit history shows
the pattern in action.

What this repo is built to demonstrate:

- **Real-time trunk integration** — every green increment is committed and pushed
  to `main` immediately (rebase + re-prove-green before each push). No PRs, no
  feature branches.
- **Minimal foundation, then fan-out** — CARD01 lands the bare table + ports;
  the remaining cards build in parallel, each in its own worktree, integrating to
  the same `main`.
- **Lane-disjoint scheduling** — cards run concurrently when they edit disjoint
  files. Outside-in / inside-out splits keep lanes apart on a shared slice.
- **Schema as a seam** — consumers own their additive migrations; a column another
  card needs is a hot seam the producer lands first. The migrations dir is a
  serialized hub.

Read the commit history (`git log --graph --oneline`) to see it: foundation first,
then interleaved parallel commits from multiple agents, all green.

## Stack

FastAPI + SQLAlchemy 2 + Alembic + pytest, managed with `uv`.

```sh
uv sync
uv run pytest          # run the suite
uv run uvicorn app.main:app --reload   # run the app
uv run alembic upgrade head            # apply migrations
```

## The app

A small `orders` API. Trivial on purpose — the point is the *process*, not the domain.
