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
commit.

# Documentation update policy

This site's wording is a deliberately hand-edited, published version of the
plugin's documentation — not something that should be silently regenerated
or overwritten from `moodle-local_quizanalytics`'s `docs/guide/` (the two
have already diverged in wording and structure). When the plugin's own
documentation changes enough that this site would otherwise mislead a
reader, update the relevant chapter page(s) here by hand, matching the
plugin repo's own policy of updating docs only for changes big enough to
matter — not for small self-contained bug fixes. See the plugin repo's
`CLAUDE.md` for the fuller version of that rule.
