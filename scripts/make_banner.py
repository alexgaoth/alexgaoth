#!/usr/bin/env python3
"""Generate banner.svg: 1-bit ordered-dither wave fronts that drift on a loop.

Ordered (Bayer 4x4) dithering, one quantised level per 8x8 tile, each level drawn
as an SVG <pattern>. The field is periodic in x, so translating the artwork by one
period loops seamlessly. Motion is CSS keyframes, not SMIL — Chrome pauses SMIL in
hidden tabs, CSS keeps running. Run: python3 scripts/make_banner.py > banner.svg
"""
import math

W, H = 1200, 120         # visible strip
DOT = 2                  # dot size in px
TILE = DOT * 4           # Bayer 4x4 tile
COLS, ROWS = 2 * W // TILE, H // TILE   # two periods wide so the loop is seamless
BG, FG = "#161b22", "#ffffff"   # the Stack badge palette
DUR = "34s"

BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


# Wave fronts, far to near: (height, amplitude, cycles across W, phase, peak, thickness).
# Nearer fronts sit lower, swell wider and slower and burn brighter, so the strip
# reads as depth. Integer cycle counts keep the field periodic in x, hence loopable.
FRONTS = ((0.30, 0.16, 3, 4.1, 0.38, 0.085),
          (0.55, 0.20, 2, 2.2, 0.58, 0.100),
          (0.82, 0.24, 1, 0.0, 0.75, 0.115))


def field(col, row):
    """Density in [0,1] at a tile, periodic in x over W.

    Each front is a Gaussian band around an undulating crest line; taking the max
    (not the sum) keeps overlaps from saturating into solid white slabs.
    """
    nx = 2 * math.pi * (col * TILE) / W
    ny = row / (ROWS - 1)
    return max(
        peak * math.exp(-(((ny - (off + amp * math.sin(k * nx + ph)
                                  + 0.4 * amp * math.sin((k + 1) * nx + ph + 1.1)))
                           / sig) ** 2))
        for off, amp, k, ph, peak, sig in FRONTS
    )


def patterns():
    out = []
    for k in range(1, 17):
        dots = "".join(
            f'<rect x="{i*DOT}" y="{j*DOT}" width="{DOT}" height="{DOT}"/>'
            for j in range(4) for i in range(4) if BAYER[j][i] < k
        )
        out.append(
            f'<pattern id="d{k}" patternUnits="userSpaceOnUse" '
            f'width="{TILE}" height="{TILE}"><g fill="{FG}">{dots}</g></pattern>'
        )
    return "".join(out)


def tiles():
    out = []
    for row in range(ROWS):
        col = 0
        while col < COLS:
            level = round(field(col, row) * 16)
            run = 1
            while col + run < COLS and round(field(col + run, row) * 16) == level:
                run += 1
            if level:
                out.append(
                    f'<rect x="{col*TILE}" y="{row*TILE}" width="{run*TILE}" '
                    f'height="{TILE}" fill="url(#d{level})"/>'
                )
            col += run
    return "".join(out)


print(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" '
    f'height="{H}" role="img" aria-label="Dithered wave banner">'
    f'<defs>{patterns()}</defs>'
    f'<style>@keyframes drift{{from{{transform:translateX(0)}}'
    f'to{{transform:translateX(-{W}px)}}}}'
    f'.f{{animation:drift {DUR} linear infinite}}'
    f'@media(prefers-reduced-motion:reduce){{.f{{animation:none}}}}</style>'
    f'<rect width="{W}" height="{H}" fill="{BG}"/>'
    f'<g class="f">{tiles()}</g>'
    f'</svg>'
)
