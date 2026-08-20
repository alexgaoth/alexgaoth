# CLAUDE.md

GitHub profile README repo (`alexgaoth/alexgaoth`). The README renders on the profile page; only a push makes changes visible.

## Generated files — never hand-edit

- `banner.svg` — regenerate with `python3 scripts/make_banner.py > banner.svg`; edit the field function in the script.
- `metrics.isocalendar.svg` — written daily by `.github/workflows/metrics.yml`. Local edits are overwritten.

## Rules

- The Stack badge wall is deliberately exhaustive — every language, framework and tool Alex has touched. Add to it; never trim it for tidiness.
- No language-distribution chart. Do not re-enable the `plugin_languages` step in the metrics workflow.
- Every project row states a concrete result (place, metric, "on PyPI"), never an adjective.
- Stack entries come from three sources: the resume, the project list in `alexgaoth.github.io`, and declared dependencies across the repos in `~/Documents`. Exclude deps found only in `github.ibm.com` repos (IBM-internal) or only in cloned third-party repos like `the-algorithm` (Twitter's, not Alex's).
- The canonical project list lives in the `alexgaoth.github.io` repo at `astro/src/data/content.js` — read it before editing the project table rather than inventing entries.
- `alexgaoth.com/resume.pdf` (same bytes as `alexgaoth.github.io/resume.pdf`) is the authoritative source for awards, metrics and the skills list. Read it with `pdftotext -layout` before restating any credential.
- The resume redacts MRR as `$XXk` — keep the real figure off the README.

## Gotchas

- Animate SVG with CSS `@keyframes`, not SMIL. Chrome pauses SMIL in hidden/background tabs, so an SMIL banner renders frozen and cannot be verified under browser automation; CSS animations keep running.
- Verify README rendering with GitHub's own parser: `gh api -X POST /markdown --input <json with {mode:"gfm",text:...}>`. A single newline in a `.md` file is not a line break — end the line with two spaces.
- The Stack section is generated: edit `scripts/make_badges.py`, run it, and splice the output between `## Stack` and the next heading. Verify with `./scripts/check_badges.sh`.
- An unknown shields.io logo slug still returns HTTP 200, just with no icon — status alone proves nothing, so check the body contains `data:image` (what `check_badges.sh` does). Simple-icons keeps dropping trademarked slugs; dead so far: `csharp` (use `dotnet`), `css3` (use `css`), and `powershell`, `openai`, `playwright`, `aws`, `apify` (no icon exists — omit the logo).
- The Chrome extension refuses `file://`. To inspect `banner.svg`, serve the directory over `python3 -m http.server` and load `http://localhost:<port>/`.
