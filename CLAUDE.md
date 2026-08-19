# CLAUDE.md

GitHub profile README repo (`alexgaoth/alexgaoth`). The README renders on the profile page; only a push makes changes visible.

## Generated files — never hand-edit

- `banner.svg` — regenerate with `python3 scripts/make_banner.py > banner.svg`; edit the field function in the script.
- `metrics.isocalendar.svg` — written daily by `.github/workflows/metrics.yml`. Local edits are overwritten.

## Rules

- The Stack badge wall is deliberately exhaustive — every language, framework and tool Alex has touched. Add to it; never trim it for tidiness.
- No language-distribution chart. Do not re-enable the `plugin_languages` step in the metrics workflow.
- Every project row states a concrete result (place, metric, "on PyPI"), never an adjective.
- The canonical project list lives in the `alexgaoth.github.io` repo at `astro/src/data/content.js` — read it before editing Selected work rather than inventing entries.
- `alexgaoth.com/resume.pdf` (same bytes as `alexgaoth.github.io/resume.pdf`) is the authoritative source for awards, metrics and the skills list. Read it with `pdftotext -layout` before restating any credential.
- The resume redacts MRR as `$XXk` — keep the real figure off the README.

## Gotchas

- Animate SVG with CSS `@keyframes`, not SMIL. Chrome pauses SMIL in hidden/background tabs, so an SMIL banner renders frozen and cannot be verified under browser automation; CSS animations keep running.
- Verify README rendering with GitHub's own parser: `gh api -X POST /markdown --input <json with {mode:"gfm",text:...}>`. A single newline in a `.md` file is not a line break — end the line with two spaces.
- Verify shields.io badges resolve their *logo*, not just HTTP 200: an unknown slug still returns 200 with no icon. Check the response contains `data:image`. Dead slugs found so far: `csharp` (use `dotnet`), `css3` (use `css`), `powershell` (no icon exists — omit the logo).
- The Chrome extension refuses `file://`. To inspect `banner.svg`, serve the directory over `python3 -m http.server` and load `http://localhost:<port>/`.
