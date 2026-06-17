# Cardpilot Backend: Local

Cards live in the repo as files; status in card frontmatter. Reviews in `specs/reviews/`.

## Cached Metadata

- Cards directory: `specs/cards/`
- Reviews directory: `specs/reviews/`

## Conventions

- Integration target branch: `main` (trunk-based; no feature branches)
- Commit style: conventional-commits
- Card title format: `SPEC01-CARD<NN>-<kebab-title>`

## Status Map

| Internal | Display |
|---|---|
| backlog | BACKLOG |
| draft | DRAFT |
| ready | READY |
| in_progress | IN PROGRESS |
| under_review | UNDER REVIEW |
| done | COMPLETED |

## Test & Branch

- Test command: `uv run pytest`
- Default branch: `main`
