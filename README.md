# moodle-local_quizanalytics_documentation.github.io

Published documentation site for [`local_quizanalytics`](https://github.com/ernestwting/moodle-local_quizanalytics)
("STACK q-type Analytics"), a Moodle analytics plugin for STACK (Maxima CAS)
quizzes.

Plain static HTML/CSS (no build step, no Jekyll) — one page per chapter,
mirroring the plugin's own PDF documentation exactly (see the PDF for the
authoritative wording; this site is that content published as a browsable
site). Math is rendered client-side via [KaTeX](https://katex.org/) (CDN).

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

This site's content is a snapshot of the plugin's own documentation PDF as
of the date it was published here. The plugin repository's own
[`docs/guide/`](https://github.com/ernestwting/moodle-local_quizanalytics/tree/main/docs/guide)
covers the same material in Markdown and is the place ongoing plugin
changes get documented first. When plugin behavior changes enough to affect
this site's wording, that update should be carried over here by hand (see
`CLAUDE.md` in this repo) — the two are cross-linked, not auto-generated
from one another, since this site's wording is deliberately hand-edited and
should not be silently overwritten by an automated sync.
