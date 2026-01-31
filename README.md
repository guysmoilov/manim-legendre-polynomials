# Legendre Polynomials: An Explainer Video

A 3Blue1Brown-style educational video explaining Legendre polynomials through the lens of orthogonality and Gram-Schmidt orthogonalization.

Made using Claude Code + https://github.com/adithya-s-k/manim_skill

## About

This video demonstrates:
- Why orthogonal bases are powerful in linear algebra
- How the inner product extends from vectors to functions
- The Gram-Schmidt process applied to polynomials {1, x, x², x³}
- How this naturally produces Legendre polynomials
- Function approximation using orthogonal polynomial bases

**Duration:** ~3 minutes
**Target Audience:** Viewers comfortable with calculus and linear algebra (inner products, projections, Gram-Schmidt)

## Structure

1. **The Power of Perpendicular** — Orthogonal bases in ℝ² make decomposition trivial
2. **Functions as Vectors** — The integral as a continuous dot product
3. **Gram-Schmidt on Polynomials** — Discovering P₀, P₁, P₂, P₃ step by step
4. **Orthogonality Grid** — Visualizing the inner product matrix
5. **Function Approximation** — Using Legendre series to approximate |x|
6. **Closing Card** — Summary of key formulas

## Requirements

- Python 3.10+
- [Manim Community Edition](https://www.manim.community/)
- LaTeX (BasicTeX or equivalent)
- ffmpeg (for video concatenation)

## Usage

Install dependencies:
```bash
uv sync
```

### Build the video

Render the full video at 720p/30fps using Make (recommended):
```bash
make
```

The Makefile provides intelligent caching — it only re-renders scenes when `legendre.py` changes:
```bash
make status    # Check which scenes need rendering
make -j4       # Build with 4 parallel jobs
make scene3    # Render just Scene 3 (Gram-Schmidt)
make clean     # Remove all generated videos
```

Alternatively, use the shell script to rebuild everything:
```bash
bash render.sh
```

### Preview individual scenes

Render individual scenes at lower quality for preview:
```bash
uv run manim render -ql legendre.py S03_GramSchmidt
```

## Files

- `legendre.py` — All 6 Manim scenes
- `scenes.md` — Detailed scene-by-scene plan and narration notes
- `Makefile` — Smart build system with caching and parallel rendering
- `render.sh` — Shell script alternative (rebuilds everything)

## Credits

Created with [Manim Community Edition](https://www.manim.community/)
Video style inspired by [3Blue1Brown](https://www.3blue1brown.com/)
Skill by https://github.com/adithya-s-k/manim_skill
