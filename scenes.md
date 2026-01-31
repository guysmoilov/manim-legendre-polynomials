# Legendre Polynomials: When Polynomials Become Perpendicular

## Overview
- **Topic**: Legendre polynomials as orthogonal polynomial basis on [-1, 1]
- **Hook**: "You know vectors can be perpendicular. But what does it mean for *polynomials* to be perpendicular?"
- **Target Audience**: Comfortable with calculus and linear algebra (inner products, basis, projections, Gram-Schmidt)
- **Estimated Length**: 7-9 minutes
- **Key Insight**: The inner product on functions naturally extends the dot product, and Gram-Schmidt on {1, x, x², ...} produces the Legendre polynomials — a "coordinate system" for function space.

## Narrative Arc
We start with the familiar idea that orthogonal bases are powerful in ℝⁿ, then ask: can we do the same for functions? We define an inner product on functions, apply Gram-Schmidt to the monomial basis, and *discover* the Legendre polynomials. We then show their orthogonality visually and close with why this matters — optimal function approximation.

---

## Scene 1: The Power of Perpendicular (Vectors)
**Duration**: ~50 seconds
**Purpose**: Anchor the viewer in familiar territory — orthogonal bases in ℝ²/ℝ³ are powerful because projections are trivial.

### Visual Elements
- 2D coordinate axes with standard basis vectors **e₁**, **e₂**
- An arbitrary vector **v** decomposed via projection onto each basis vector
- Show the formula: coefficients = dot products (no matrix inversion needed)
- Brief flash of a non-orthogonal basis to contrast how messy decomposition becomes

### Content
Open with: "Orthogonal bases are one of the most powerful ideas in linear algebra."
Show a vector **v** in ℝ², project onto e₁ and e₂. Highlight that the coefficient is just ⟨v, eᵢ⟩. Then briefly show a skewed (non-orthogonal) basis — decomposition requires solving a system. Orthogonality makes life simple.

### Narration Notes
Tone: confident, setting up something the viewer already knows. Quick pacing — this is review, not new content. End with the pivot: "But what if our 'vectors' aren't arrows in space... but *functions*?"

### Technical Notes
- `NumberPlane`, `Arrow`, `Vector` for the 2D setup
- `DashedLine` for projection lines
- Use `TransformMatchingShapes` or `ReplacementTransform` to morph between bases
- Colors: basis vectors in BLUE and YELLOW, target vector in WHITE

---

## Scene 2: Functions as Vectors
**Duration**: ~70 seconds
**Purpose**: Bridge from ℝⁿ to function space. Define the inner product on functions as an integral.

### Visual Elements
- Axes showing two functions f(x) and g(x) on [-1, 1]
- The product f(x)·g(x) shown as a third curve
- Shaded area under f·g representing the integral (inner product)
- Side-by-side comparison: dot product formula ↔ function inner product formula

### Content
"A function on [-1, 1] is really just an infinite-dimensional vector — its value at each point is a 'component'."

Show the analogy:
- Vector: (v₁, v₂, ..., vₙ) → Function: f(x) for each x ∈ [-1,1]
- Dot product: Σ vᵢwᵢ → Inner product: ∫₋₁¹ f(x)g(x) dx

Visually: plot f(x) = x and g(x) = x², show their product x³, shade the area under it. The integral is 0! These functions are "perpendicular."

### Narration Notes
This is the key conceptual leap. Slow down here. Let the integral = 0 land as a surprise. "The area above and below the axis cancel perfectly. These two functions are *orthogonal*."

### Technical Notes
- `Axes` with x-range [-1, 1]
- `plot()` for function curves
- `area = axes.get_area(product_graph, ...)` with positive/negative coloring
- MathTex for the inner product formula
- Animate the dot product formula morphing into the integral formula

---

## Scene 3: Gram-Schmidt on Polynomials
**Duration**: ~120 seconds
**Purpose**: The core of the video. Apply Gram-Schmidt to {1, x, x², x³} and discover Legendre polynomials.

### Visual Elements
- Axes on [-1, 1] showing each polynomial being constructed step by step
- Each step: show the monomial, subtract its projections, normalize
- Build up P₀, P₁, P₂, P₃ one at a time
- Running list of completed Legendre polynomials on the right side

### Content
"We have an inner product. We have a starting basis — the monomials {1, x, x², ...}. What does Gram-Schmidt give us?"

**Step 1: P₀**
Start with f₀(x) = 1. Normalize: P₀(x) = 1. (Trivial, but show the graph.)

**Step 2: P₁**
Start with f₁(x) = x. Compute ⟨x, P₀⟩ = ∫₋₁¹ x dx = 0. Already orthogonal! P₁(x) = x.

**Step 3: P₂**
Start with f₂(x) = x². Compute ⟨x², P₀⟩ = ∫₋₁¹ x² dx = 2/3. Compute ⟨x², P₁⟩ = ∫₋₁¹ x³ dx = 0.
Subtract: x² − (2/3)/(2) · 1 = x² − 1/3.
Normalize (so P₂(1) = 1): P₂(x) = (3x² − 1)/2.
Show the curve — it's orthogonal to both P₀ and P₁!

**Step 4: P₃**
Show the process faster for x³. Result: P₃(x) = (5x³ − 3x)/2.

### Narration Notes
This is the longest scene and the heart of the video. For P₂, go through every step deliberately. For P₃, speed up — the viewer gets the pattern. Emphasize: "We didn't *define* these polynomials — we *discovered* them. Gram-Schmidt forced them into existence."

### Technical Notes
- Animate integrals being computed (show shaded areas briefly)
- Use `Transform` to show x² morphing into P₂ as the projection is subtracted
- Display formulas with `MathTex`, animate the subtraction step
- Color code: monomials in RED, finished Legendre polynomials in GREEN
- Keep a `VGroup` list of completed polynomials on the right, `FadeIn` each new one

---

## Scene 4: The Orthogonality Grid
**Duration**: ~60 seconds
**Purpose**: Visually verify orthogonality. Show the "inner product matrix" and product-integral visualizations.

### Visual Elements
- A 4×4 grid/matrix showing ⟨Pᵢ, Pⱼ⟩ values
- Diagonal lights up (non-zero), off-diagonal is all zeros
- For one off-diagonal pair (e.g., P₁ and P₂): show the product curve and its integral canceling to zero
- For one diagonal entry: show the product P₂² and its positive integral

### Content
"Let's verify. If we compute every inner product between our polynomials, we get..."

Show the matrix filling in. Off-diagonal: all zeros. Diagonal: non-zero values (2/(2n+1)).

Pick P₁·P₂ = x·(3x²−1)/2 — plot it, shade it, show perfect cancellation. Then P₂² — always positive, integral = 2/5.

"This is the identity matrix's elegant cousin — a diagonal matrix. Our polynomials form an orthogonal basis."

### Narration Notes
Satisfying visual payoff. Let the matrix appear with some drama — perhaps fill in off-diagonal zeros with a slight delay for each. The "all zeros off diagonal" should feel like a revelation.

### Technical Notes
- `Matrix` or custom `MobjectMatrix` for the grid
- `Integer` and `DecimalNumber` for entries
- Animate entries appearing one by one or row by row
- Use BLUE for zero entries, GOLD for diagonal entries
- Split-color area shading (positive GREEN, negative RED) for the product integrals

---

## Scene 5: Why This Matters — Function Approximation
**Duration**: ~60 seconds
**Purpose**: Close with the payoff — Legendre polynomials let you optimally approximate any function on [-1,1], analogous to Fourier series.

### Visual Elements
- A "complicated" function (e.g., |x| or a step-like function) on [-1,1]
- Successively add Legendre polynomial terms: show the approximation improving
- Side by side: Fourier (sines/cosines) vs Legendre (polynomials) approximation
- Final text: connection to physics (spherical harmonics, electrostatics)

### Content
"Just as Fourier series decompose functions into sines and cosines, Legendre series decompose functions into these orthogonal polynomials."

Show f(x) = |x|. Compute c₀P₀ + c₁P₁ — crude approximation. Add c₂P₂ — much better. Add more terms — converging beautifully.

"The coefficients? Just inner products. No systems of equations. The power of orthogonality."

Briefly mention: "These same polynomials appear when you solve Laplace's equation in spherical coordinates — they're the backbone of spherical harmonics, multipole expansions, and quantum mechanics."

### Narration Notes
Bring it home. The tone shifts from construction to *power* — what you can do with these. End on a forward-looking note about physics applications to leave the viewer wanting more.

### Technical Notes
- `always_redraw` or successive `Transform` calls for the approximation
- Use `ValueTracker` to animate number of terms
- `MathTex` for the series formula f(x) = Σ cₙPₙ(x)
- Final frame: elegant typography with key takeaways

---

## Scene 6: Closing Card
**Duration**: ~15 seconds
**Purpose**: Summary and sign-off.

### Visual Elements
- Clean title card with the key formulas:
  - Inner product: ⟨f, g⟩ = ∫₋₁¹ f(x)g(x) dx
  - First four: P₀=1, P₁=x, P₂=(3x²−1)/2, P₃=(5x³−3x)/2
  - Orthogonality: ⟨Pₘ, Pₙ⟩ = 0 for m ≠ n
- Fade to black

### Technical Notes
- `VGroup` of `MathTex` objects, nicely laid out
- `FadeIn` with stagger, hold, `FadeOut`

---

## Transitions & Flow
- Scene 1 → 2: Vector **v** morphs/dissolves into a function curve (visual bridge from discrete to continuous)
- Scene 2 → 3: The inner product formula stays on screen as we begin Gram-Schmidt
- Scene 3 → 4: The list of polynomials on the right expands into the full matrix
- Scene 4 → 5: Diagonal matrix dissolves, polynomials reappear on axes for approximation
- Scene 5 → 6: Approximation freezes, formulas replace it

## Color Palette
- Primary: `BLUE` (#58C4DD) — basis vectors, key formulas, Legendre polynomials
- Secondary: `YELLOW` (#FFFF00) — second basis vector, highlights, emphasis
- Accent: `GREEN` (#83C167) — positive areas, completed/verified items
- Negative: `RED` (#FC6255) — negative areas, non-orthogonal bases, things being subtracted
- Background: `#1C1C1C` (dark gray, standard 3b1b)
- Monomials: `RED_B` — the "raw" polynomials before orthogonalization
- Legendre: `BLUE_C` to `BLUE_A` gradient by degree

## Mathematical Content
- Dot product: **v · w** = Σ vᵢwᵢ
- Function inner product: ⟨f, g⟩ = ∫₋₁¹ f(x)g(x) dx
- Gram-Schmidt: eₙ = fₙ − Σₖ₌₀ⁿ⁻¹ (⟨fₙ, eₖ⟩/⟨eₖ, eₖ⟩) eₖ
- P₀(x) = 1
- P₁(x) = x
- P₂(x) = (3x² − 1)/2
- P₃(x) = (5x³ − 3x)/2
- Orthogonality: ∫₋₁¹ Pₘ(x)Pₙ(x) dx = 2/(2n+1) · δₘₙ
- Fourier-Legendre series: f(x) = Σ cₙPₙ(x), where cₙ = (2n+1)/2 · ∫₋₁¹ f(x)Pₙ(x) dx

## Implementation Order
1. **Scene 2** (Functions as Vectors) — core visual language, reusable axes/area code
2. **Scene 3** (Gram-Schmidt) — heart of the video, most complex animations
3. **Scene 1** (Vector review) — simpler, can be polished after core is working
4. **Scene 4** (Orthogonality grid) — builds on Scene 3 outputs
5. **Scene 5** (Approximation) — standalone, needs function plotting
6. **Scene 6** (Closing) — trivial, do last
