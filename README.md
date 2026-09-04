# moodle-local_quizanalytics_documentation.github.io

Published documentation site for [`local_quizanalytics`](https://github.com/ernestwting/moodle-local_quizanalytics)
("STACK q-type Analytics"), a Moodle analytics plugin for STACK (Maxima CAS)
quizzes.

Plain static HTML/CSS (no build step, no Jekyll) — one page per chapter,
synced from the plugin repo's own `docs/guide/*.md` (see below). Math is
rendered client-side via [KaTeX](https://katex.org/) (CDN).

## Structure

- `index.html` — home / table of contents
- `introduction.html`, `getting-started.html`, `installation.html`,
  `using.html`, `calculations.html`, `privacy-security.html`,
  `architecture.html`, `glossary.html`, `references.html` — one per chapter
- `assets/style.css`, `assets/nav.js` — shared layout/sidebar, no framework

## Publishing

This repo's name doesn't match the `<username>.github.io` special case, so
GitHub Pages needs to be turned on once by hand: **Settings → Pages →
Source: Deploy from a branch → `main` / `(root)`**.

## Keeping this in sync with the plugin

This site's nine chapter pages are **automatically synced** from
[`moodle-local_quizanalytics`](https://github.com/ernestwting/moodle-local_quizanalytics)'s
own [`docs/guide/*.md`](https://github.com/ernestwting/moodle-local_quizanalytics/tree/main/docs/guide) —
that Markdown is the real source of truth. A scheduled GitHub Action
(`.github/workflows/sync-from-plugin-docs.yml`, every 6 hours, or trigger
it by hand from the Actions tab) pulls the current Markdown, converts it
with pandoc, and replaces each chapter page's `<article>` content —
`scripts/sync_docs.py` has the exact file mapping. No secrets are
involved: the source repo is public, and the workflow only ever pushes
back to its own repo using the `GITHUB_TOKEN` Actions provides
automatically.

**Do not hand-edit a chapter page's `<article>` body** — the next sync run
overwrites it. Edit `docs/guide/` in the plugin repo instead. `index.html`
(the cover/TOC page), `assets/`, `.github/`, and `scripts/` are this
repo's own and aren't touched by the sync.

To preview what a sync would change before it runs, install `pandoc`
locally and run `python3 scripts/sync_docs.py` from the repo root.
