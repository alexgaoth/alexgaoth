# CLAUDE.md

GitHub profile README repo (`alexgaoth/alexgaoth`). The README renders on the profile page; only a push makes changes visible.

## Generated files — never hand-edit

- `banner.svg` — regenerate with `python3 scripts/make_banner.py > banner.svg`; edit `FRONTS`/`field()` in the script. Its palette is locked to the Stack badge scheme (`#161b22` ground, white dots).
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
- Verify README rendering with `gh api -X POST /markdown --input <json with {mode:"markdown",text:...}>`. Use `mode:"markdown"`, never `mode:"gfm"`: gfm is *comment* rendering, where every newline becomes a `<br>`, so a broken line break passes the check. Tables still render under `markdown`.
- To break a line in the README, use an explicit `<br>`. A plain newline and a single trailing space both clump; two trailing spaces work but are invisible in an editor and were silently lost twice.
- The Stack section is generated: edit `scripts/make_badges.py`, run it, and splice the output between `## Stack` and the next heading. Verify with `./scripts/check_badges.sh`.
- An unknown shields.io logo slug still returns HTTP 200, just with no icon — status alone proves nothing, so check the body contains `data:image` (what `check_badges.sh` does). Simple-icons keeps dropping trademarked slugs; dead so far: `csharp` (use `dotnet`), `css3` (use `css`), and `powershell`, `openai`, `playwright`, `aws`, `apify` (no icon exists — omit the logo).
- To look at `banner.svg`, rasterize it: `google-chrome --headless=new --disable-gpu --screenshot=out.png --window-size=900,140 --allow-file-access-from-files file://<abs path to a wrapper .html>`. The Chrome extension refuses `file://`, so the alternative is serving the directory over `python3 -m http.server` — slower, and unnecessary for a still frame.
- Judge the dither field by rasterizing it, never by an ASCII/level dump. At the strip's 10:1 aspect a crest that looks wavy in a level dump renders as flat horizontal stripes; amplitude has to be read against the 1200px width, not against the tile grid.
