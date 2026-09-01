# CLAUDE.md

GitHub profile README repo (`alexgaoth/alexgaoth`). The README renders on the profile page; only a push makes changes visible.

## Generated files — never hand-edit

- `banner.png` — a 1-bit dither of `banner.jpg` (the source photo; keep it committed). Regenerate with:
  `magick banner.jpg -colorspace Gray -resize 600x -normalize -ordered-dither o4x4 -filter point -resize 200% +level-colors '#161b22,#ffffff' banner.png`
  Palette is locked to the Stack badge scheme (`#161b22` ground, white dots). `banner.svg` and `scripts/make_banner.py` are the retired animated wave banner — no longer referenced by the README.
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
- To look at a banner, screenshot it: `google-chrome --headless=new --disable-gpu --screenshot=out.png --window-size=900,600 --allow-file-access-from-files file://<abs path to a wrapper .html>`. The Chrome extension refuses `file://`, so the alternative is serving the directory over `python3 -m http.server` — slower, and unnecessary for a still frame.
- Judge any dither by rendering it at the README's ~880px display width, never at native size. Dithering straight to full width blends into flat grey once the browser scales it down, which is why the pipeline dithers at half width and point-upscales 2x to get 2px cells.
- ImageMagick's `-monochrome` thresholds rather than diffuses (blown-out blacks and whites), and `-colors 2` quantises to two greys. For a 1-bit look use `-ordered-dither`, then `+level-colors` to map the two levels.
