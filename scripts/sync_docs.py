#!/usr/bin/env python3
"""Pulls docs/guide/*.md from the public moodle-local_quizanalytics repo,
converts each to HTML via pandoc, and replaces the <article>...</article>
region of the matching chapter page in this repo.

Run by .github/workflows/sync-from-plugin-docs.yml; safe to run locally
too (`python3 scripts/sync_docs.py` from the repo root, with pandoc
installed) to preview what a sync would change before it runs on schedule.
"""
import re
import subprocess
import sys
import urllib.request

SOURCE_RAW = (
    "https://raw.githubusercontent.com/ernestwting/moodle-local_quizanalytics"
    "/main/docs/guide/{}.md"
)

# docs/guide/<key>.md in moodle-local_quizanalytics -> this site's chapter page.
# index.md is intentionally not synced -- this site's index.html is a
# hand-built cover/TOC page with no equivalent structure in docs/guide/.
MAPPING = {
    "about": "introduction.html",
    "getting-started": "getting-started.html",
    "installation": "installation.html",
    "instructor-guide": "using.html",
    "calculations": "calculations.html",
    "privacy-and-security": "privacy-security.html",
    "architecture": "architecture.html",
    "glossary": "glossary.html",
    "references": "references.html",
}

ARTICLE_RE = re.compile(r"<article>.*?</article>", re.DOTALL)


def fetch(name: str) -> str:
    with urllib.request.urlopen(SOURCE_RAW.format(name), timeout=30) as resp:
        return resp.read().decode("utf-8")


def strip_leading_frontmatter(md: str) -> str:
    # Drop docs/guide/*.md's own breadcrumb line ("\[ [STACK q-type
    # Analytics Docs](index.md) -> About \]") and its top-level "# Title"
    # heading -- the site page already renders its own crumb and
    # <h1 class="page-title">, so both would otherwise duplicate here.
    lines = md.split("\n")
    if lines and lines[0].startswith("\\["):
        lines = lines[1:]
    md = "\n".join(lines).lstrip("\n")
    md = re.sub(r"\A#\s+[^\n]*\n+", "", md, count=1)
    return md


def rewrite_md_link(match: re.Match) -> str:
    stem, fragment = match.group(1), match.group(2) or ""
    # docs/guide/foo.md -> this site's target file for foo, per MAPPING
    # (several don't share a filename with their source, e.g. about.md ->
    # introduction.html) -- fall back to a plain .md->.html swap for
    # anything not in MAPPING, though every real cross-link should be.
    target = MAPPING.get(stem, f"{stem}.html")
    return f'href="{target}{fragment}"'


def md_to_html(md: str) -> str:
    result = subprocess.run(
        ["pandoc", "--from=gfm+tex_math_dollars", "--to=html", "--mathjax", "--wrap=none"],
        input=md,
        capture_output=True,
        text=True,
        check=True,
    )
    html = result.stdout.strip()
    # Point same-guide cross-links (foo.md, foo.md#anchor) at the site
    # page that actually holds that content -- see rewrite_md_link().
    html = re.sub(r'href="([a-zA-Z0-9_-]+)\.md(#[^"]*)?"', rewrite_md_link, html)
    return html


def sync_one(source_key: str, target_file: str) -> bool:
    md = strip_leading_frontmatter(fetch(source_key))
    body = md_to_html(md)
    with open(target_file, "r", encoding="utf-8") as f:
        page = f.read()
    # A plain string replacement would let re treat backslashes in the
    # LaTeX (\frac, \sum, ...) as regex backreference escapes -- a
    # function replacement is inserted literally, with no such parsing.
    new_page, n = ARTICLE_RE.subn(
        lambda _m: f"<article>\n{body}\n</article>", page, count=1
    )
    if n != 1:
        print(
            f"::error::{target_file}: expected exactly one <article> block, "
            f"found {n} -- refusing to touch this file",
            file=sys.stderr,
        )
        raise SystemExit(1)
    if new_page == page:
        return False
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(new_page)
    return True


def main() -> int:
    changed = [
        target
        for source_key, target in MAPPING.items()
        if sync_one(source_key, target)
    ]
    if changed:
        print("Updated: " + ", ".join(changed))
    else:
        print("Already up to date -- no changes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
