# Commit policy

Never add a `Co-Authored-By: Claude` (or any Anthropic/Claude) trailer to
commit messages in this repo, and never set the commit author/committer to
Claude. All commits must be authored solely by the human contributor who
made them. This mirrors the same standing policy in the
[`moodle-local_quizanalytics`](https://github.com/ernestwting/moodle-local_quizanalytics)
repo's own `CLAUDE.md`.

Only commit (or push) when explicitly asked in that session. Finishing a
task — even a large one — is not by itself a request to commit; leave
changes in the working tree and say what's ready, then wait to be told to
commit. This does not apply to `.github/workflows/sync-from-plugin-docs.yml`'s
own scheduled commits — that automation is the user's own infrastructure,
running unattended by design, and its `docs-sync-bot` commits are not
Claude acting in a session.

# Documentation update policy

**`docs/guide/*.md` in [`moodle-local_quizanalytics`](https://github.com/ernestwting/moodle-local_quizanalytics)
is the source of truth.** `.github/workflows/sync-from-plugin-docs.yml`
pulls it on a schedule (and via manual dispatch), converts it with pandoc,
and replaces the `<article>...</article>` body of the matching chapter
page here — see `scripts/sync_docs.py` for the exact file mapping. Do not
hand-edit a chapter page's `<article>` content directly; it will be
overwritten by the next sync run. Edit `docs/guide/` in the plugin repo
instead, following that repo's own documentation-update policy (its
`CLAUDE.md`) for what counts as a big-enough change to update docs for.

Outside the `<article>` block — the shared `assets/style.css`,
`assets/nav.js`, `index.html`'s cover/TOC, and anything in `.github/` or
`scripts/` — is this repo's own, not synced from anywhere, and edited
directly here as normal.
