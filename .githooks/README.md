# Git hooks (tracked)

These hooks live in the repo so there is one shared source of truth instead of
each clone hand-editing `.git/hooks/`.

## Activate (once per clone)

```
git config core.hooksPath .githooks
```

That is the only manual step. Verify with:

```
git config core.hooksPath   # → .githooks
```

## pre-commit

Gates `posts/*.md` edits through `tools/posts-eval.py`:

- Fires **only** when a commit stages `posts/*.md`. Every other commit
  (contracts, tools, GOVERNANCE, docs, …) passes instantly — no added friction.
- **FAIL blocks** the commit; **WARN passes** (posts-eval exits 1 only on FAIL).
- Evaluates the **whole** staged file (all post blocks), so a pre-existing FAIL
  in an untouched block of the same file will also block — fix it or the file
  stays frozen.

Deliberate override (use only when you mean it): `git commit --no-verify`.

### Why this exists

`contracts/posts/*` is a real authoring contract that was only ever enforced by
documents agents read voluntarily, and compliance decayed across the corpus
(see `contracts/posts/EVOLUTION.md`). This hook moves the FAIL line from
"please remember to run eval" to a mechanical precondition of committing a draft.
It does **not** enforce score / review_log (those are not in posts-eval) — only
what posts-eval mechanically checks.
