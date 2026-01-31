from manim import *
import numpy as np


# ──────────────────────────────────────────────────────────────────────
# Scene 1: The Power of Perpendicular
# ──────────────────────────────────────────────────────────────────────
class S01_PowerOfPerpendicular(Scene):
    """Review orthogonal bases in R^2 — why orthogonality makes decomposition trivial."""

    def construct(self):
        # Title
        title = Text("When Polynomials Become Perpendicular", font_size=42)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.5).to_edge(UP))

        # 2D axes with basis vectors
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5,
            y_length=5,
            background_line_style={"stroke_opacity": 0.3},
        ).shift(DOWN * 0.3)
        self.play(Create(plane), run_time=1)

        # Basis vectors
        e1 = Arrow(plane.c2p(0, 0), plane.c2p(1, 0), buff=0, color=BLUE, stroke_width=5)
        e2 = Arrow(plane.c2p(0, 0), plane.c2p(0, 1), buff=0, color=YELLOW, stroke_width=5)
        e1_label = MathTex(r"\mathbf{e}_1", color=BLUE).next_to(e1, DOWN, buff=0.15)
        e2_label = MathTex(r"\mathbf{e}_2", color=YELLOW).next_to(e2, LEFT, buff=0.15)
        self.play(GrowArrow(e1), GrowArrow(e2), FadeIn(e1_label), FadeIn(e2_label))
        self.wait(0.5)

        # Arbitrary vector
        v = Arrow(plane.c2p(0, 0), plane.c2p(2.3, 1.7), buff=0, color=WHITE, stroke_width=4)
        v_label = MathTex(r"\mathbf{v}", color=WHITE).next_to(v.get_end(), UR, buff=0.1)
        self.play(GrowArrow(v), FadeIn(v_label))
        self.wait(0.5)

        # Projection lines
        proj_x = DashedLine(plane.c2p(2.3, 1.7), plane.c2p(2.3, 0), color=BLUE_A, stroke_width=2)
        proj_y = DashedLine(plane.c2p(2.3, 1.7), plane.c2p(0, 1.7), color=YELLOW_A, stroke_width=2)
        comp_x = Arrow(plane.c2p(0, 0), plane.c2p(2.3, 0), buff=0, color=BLUE_B, stroke_width=4)
        comp_y = Arrow(plane.c2p(0, 0), plane.c2p(0, 1.7), buff=0, color=YELLOW_B, stroke_width=4)
        self.play(Create(proj_x), Create(proj_y), run_time=0.8)
        self.play(GrowArrow(comp_x), GrowArrow(comp_y), run_time=0.8)

        # Formula
        formula = MathTex(
            r"\mathbf{v}", r"=",
            r"\langle \mathbf{v}, \mathbf{e}_1 \rangle", r"\mathbf{e}_1",
            r"+",
            r"\langle \mathbf{v}, \mathbf{e}_2 \rangle", r"\mathbf{e}_2",
        ).scale(0.75).to_edge(DOWN, buff=0.5)
        formula[0].set_color(WHITE)
        formula[2].set_color(BLUE_B)
        formula[3].set_color(BLUE)
        formula[5].set_color(YELLOW_B)
        formula[6].set_color(YELLOW)
        self.play(Write(formula))
        self.wait(1)

        # Transition text
        question = Text(
            "But what if our vectors aren't arrows...\nbut functions?",
            font_size=32,
            color=BLUE_A,
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeOut(formula), FadeIn(question, shift=UP * 0.3))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ──────────────────────────────────────────────────────────────────────
# Scene 2: Functions as Vectors
# ──────────────────────────────────────────────────────────────────────
class S02_FunctionsAsVectors(Scene):
    """Define inner product on functions with intuitive explanation."""

    def construct(self):
        # ── Part A: The analogy ──
        header = Text("Functions live in an infinite-dimensional vector space", font_size=28, color=BLUE_A)
        header.to_edge(UP, buff=0.5)
        self.play(FadeIn(header, shift=DOWN * 0.2))
        self.wait(1)

        # Discrete vs continuous comparison
        disc_title = Text("Vectors in Rⁿ", font_size=24, color=BLUE).shift(LEFT * 3 + UP * 1.5)
        cont_title = Text("Functions on [-1, 1]", font_size=24, color=YELLOW).shift(RIGHT * 3 + UP * 1.5)

        disc_items = VGroup(
            Text("n components: (v₁, v₂, ..., vₙ)", font_size=18),
            MathTex(r"\langle \mathbf{v}, \mathbf{w} \rangle = \sum_i v_i w_i", font_size=24),
            Text("Sum: multiply matching\ncomponents, add up", font_size=16, color=GREY_A),
        ).arrange(DOWN, buff=0.3).next_to(disc_title, DOWN, buff=0.3)

        cont_items = VGroup(
            Text("∞ components: f(x) for each x", font_size=18),
            MathTex(r"\langle f, g \rangle = \int_{-1}^{1} f(x) g(x)\,dx", font_size=24),
            Text("Integral: multiply matching\nvalues, integrate", font_size=16, color=GREY_A),
        ).arrange(DOWN, buff=0.3).next_to(cont_title, DOWN, buff=0.3)

        disc_items[1].set_color(BLUE)
        cont_items[1].set_color(YELLOW)

        self.play(FadeIn(disc_title), FadeIn(cont_title))
        for d, c in zip(disc_items, cont_items):
            self.play(FadeIn(d, shift=UP * 0.1), FadeIn(c, shift=UP * 0.1))
            self.wait(0.8)

        # Highlight the key insight
        insight = Text(
            "The integral replaces the sum — it's the continuous version of a dot product.",
            font_size=20, color=GREEN,
        ).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(insight, shift=UP * 0.2))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Part B: Visual demonstration ──
        ip_formula = MathTex(
            r"\langle f, g \rangle = \int_{-1}^{1} f(x)\,g(x)\,dx",
            font_size=28, color=YELLOW,
        ).to_corner(UL, buff=0.4)
        self.play(FadeIn(ip_formula))

        axes = Axes(
            x_range=[-1.2, 1.2, 0.5],
            y_range=[-1.2, 1.2, 0.5],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True, "font_size": 20},
        ).shift(DOWN * 0.3)
        self.play(Create(axes), run_time=0.8)

        # f(x) = x, g(x) = x²
        f_graph = axes.plot(lambda x: x, color=BLUE, x_range=[-1, 1])
        g_graph = axes.plot(lambda x: x**2, color=YELLOW, x_range=[-1, 1])
        f_label = MathTex("f(x) = x", color=BLUE, font_size=28).next_to(axes, RIGHT, buff=0.3).shift(UP * 0.5)
        g_label = MathTex("g(x) = x^2", color=YELLOW, font_size=28).next_to(f_label, DOWN, buff=0.3)
        self.play(Create(f_graph), FadeIn(f_label))
        self.play(Create(g_graph), FadeIn(g_label))
        self.wait(0.5)

        # Explain what we're about to do
        explain = Text("Multiply them pointwise, then integrate:", font_size=20, color=GREY_A).next_to(axes, UP, buff=0.2).shift(RIGHT * 1)
        self.play(FadeIn(explain))
        self.wait(0.8)

        # Product f*g = x³
        product_graph = axes.plot(lambda x: x**3, color=GREEN, x_range=[-1, 1])
        product_label = MathTex("f(x) \\cdot g(x) = x^3", color=GREEN, font_size=26).next_to(g_label, DOWN, buff=0.3)
        self.play(
            FadeOut(f_graph), FadeOut(g_graph), FadeOut(explain),
            Create(product_graph), FadeIn(product_label),
        )

        # Shade positive and negative areas
        pos_area = axes.get_area(product_graph, x_range=[0, 1], color=GREEN, opacity=0.4)
        neg_area = axes.get_area(product_graph, x_range=[-1, 0], color=RED, opacity=0.4)
        self.play(FadeIn(pos_area), FadeIn(neg_area))
        self.wait(0.5)

        cancel_note = Text(
            "Positive and negative areas cancel perfectly",
            font_size=20, color=GREY_A,
        ).next_to(axes, DOWN, buff=0.2)
        self.play(FadeIn(cancel_note))
        self.wait(1)

        result = MathTex(
            r"\langle f, g \rangle = \int_{-1}^{1} x^3 \, dx = 0",
            color=WHITE, font_size=32,
        ).next_to(cancel_note, DOWN, buff=0.2)
        perp = Text("These functions are orthogonal!", font_size=26, color=GREEN_A).next_to(result, DOWN, buff=0.15)
        self.play(Write(result))
        self.wait(0.5)
        self.play(FadeIn(perp, shift=UP * 0.2))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ──────────────────────────────────────────────────────────────────────
# Scene 3: Gram-Schmidt on Polynomials
# ──────────────────────────────────────────────────────────────────────
class S03_GramSchmidt(Scene):
    """Apply Gram-Schmidt to {1, x, x², x³} with full explanations."""

    def construct(self):
        title = Text("Gram-Schmidt on Polynomials", font_size=36).to_edge(UP)
        self.play(Write(title))

        # ── Explain the Gram-Schmidt idea first ──
        gs_idea = VGroup(
            Text("The Gram-Schmidt recipe:", font_size=24, color=BLUE_A),
            Text("1. Take the next monomial (1, x, x², x³, ...)", font_size=20),
            Text("2. Subtract its projection onto each polynomial we've already built", font_size=20),
            Text("3. What's left is the part that's orthogonal to all previous ones", font_size=20),
            Text("4. Normalize so P(1) = 1", font_size=20),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).shift(DOWN * 0.5)
        self.play(LaggedStart(*[FadeIn(item, shift=RIGHT * 0.2) for item in gs_idea], lag_ratio=0.3))
        self.wait(2.5)

        # Show the projection formula
        proj_formula = MathTex(
            r"\text{proj}_{P_k}(f) = \frac{\langle f, P_k \rangle}{\langle P_k, P_k \rangle} P_k",
            font_size=26, color=YELLOW,
        ).next_to(gs_idea, DOWN, buff=0.4)
        proj_note = Text(
            "This is how much of f 'points in the direction' of Pₖ",
            font_size=18, color=GREY_A,
        ).next_to(proj_formula, DOWN, buff=0.15)
        self.play(Write(proj_formula))
        self.play(FadeIn(proj_note))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects if m != title])

        # Inner product reminder in corner
        ip_reminder = MathTex(
            r"\langle f, g \rangle = \int_{-1}^{1} f(x)\,g(x)\,dx",
            font_size=22, color=GREY_B,
        ).to_corner(UR)
        self.play(FadeIn(ip_reminder))

        # Axes
        axes = Axes(
            x_range=[-1.2, 1.2, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=6.5,
            y_length=3.8,
            axis_config={"include_numbers": True, "font_size": 18},
        ).shift(DOWN * 0.5 + LEFT * 0.5)
        self.play(Create(axes), run_time=0.8)

        # Running list of completed polynomials
        poly_list_title = Text("Result", font_size=18, color=GREEN).to_edge(RIGHT, buff=0.3).shift(UP * 2.5)
        poly_list = VGroup(poly_list_title)
        self.play(FadeIn(poly_list_title))

        colors = [BLUE, YELLOW, GREEN, RED_B]

        # ── P₀ ──
        step_label = Text("Step 1: f₀(x) = 1", font_size=22, color=GREY_A).next_to(title, DOWN, buff=0.25)
        self.play(FadeIn(step_label))

        p0_graph = axes.plot(lambda x: 1, color=colors[0], x_range=[-1, 1])
        self.play(Create(p0_graph))

        p0_note = Text("No previous polynomials to subtract. Just normalize.", font_size=18, color=GREY_A)
        p0_note.next_to(axes, DOWN, buff=0.3)
        self.play(FadeIn(p0_note))
        self.wait(1)

        p0_tex = MathTex(r"P_0(x) = 1", color=colors[0], font_size=26)
        p0_tex.next_to(poly_list_title, DOWN, buff=0.25).align_to(poly_list_title, LEFT)
        self.play(FadeIn(p0_tex), FadeOut(p0_note))
        poly_list.add(p0_tex)
        self.wait(0.5)

        # ── P₁ ──
        new_step = Text("Step 2: f₁(x) = x", font_size=22, color=GREY_A).next_to(title, DOWN, buff=0.25)
        self.play(ReplacementTransform(step_label, new_step))
        step_label = new_step

        mono_graph = axes.plot(lambda x: x, color=RED, x_range=[-1, 1], stroke_width=3)
        self.play(Create(mono_graph))

        # Explain
        ip_calc = VGroup(
            Text("Subtract projection onto P₀:", font_size=18, color=GREY_A),
            MathTex(
                r"\langle x, P_0 \rangle = \int_{-1}^{1} x \cdot 1 \, dx = 0",
                font_size=24, color=GREY_A,
            ),
            Text("x is odd, 1 is even → product is odd → integral is 0", font_size=16, color=GREEN),
        ).arrange(DOWN, buff=0.15).next_to(axes, DOWN, buff=0.25)
        self.play(FadeIn(ip_calc[0]))
        self.play(Write(ip_calc[1]))
        self.wait(0.5)
        self.play(FadeIn(ip_calc[2]))
        self.wait(1.5)

        p1_graph = axes.plot(lambda x: x, color=colors[1], x_range=[-1, 1])
        self.play(
            ReplacementTransform(mono_graph, p1_graph),
            FadeOut(ip_calc),
        )
        p1_tex = MathTex(r"P_1(x) = x", color=colors[1], font_size=26)
        p1_tex.next_to(p0_tex, DOWN, buff=0.15).align_to(p0_tex, LEFT)
        self.play(FadeIn(p1_tex))
        poly_list.add(p1_tex)
        self.wait(0.5)

        # ── P₂ — the key step, fully explained ──
        new_step = Text("Step 3: f₂(x) = x²", font_size=22, color=GREY_A).next_to(title, DOWN, buff=0.25)
        self.play(ReplacementTransform(step_label, new_step))
        step_label = new_step

        mono2_graph = axes.plot(lambda x: x**2, color=RED, x_range=[-1, 1], stroke_width=3)
        self.play(Create(mono2_graph))

        # Step-by-step inner products
        p2_steps = VGroup(
            Text("Subtract projections onto P₀ and P₁:", font_size=18, color=GREY_A),
            MathTex(
                r"\langle x^2, P_0 \rangle = \int_{-1}^{1} x^2 \, dx = \frac{2}{3}",
                font_size=22,
            ),
            MathTex(
                r"\langle P_0, P_0 \rangle = \int_{-1}^{1} 1 \, dx = 2",
                font_size=22,
            ),
        ).arrange(DOWN, buff=0.12).next_to(axes, DOWN, buff=0.2)
        self.play(FadeIn(p2_steps[0]))
        self.play(Write(p2_steps[1]))
        self.wait(0.5)
        self.play(Write(p2_steps[2]))
        self.wait(0.5)

        # The subtraction
        p2_sub = VGroup(
            MathTex(
                r"\text{proj}_{P_0}(x^2) = \frac{2/3}{2} \cdot 1 = \frac{1}{3}",
                font_size=22, color=YELLOW,
            ),
            MathTex(
                r"\text{proj}_{P_1}(x^2) = 0 \quad \text{(odd × even = 0)}",
                font_size=22, color=YELLOW,
            ),
        ).arrange(DOWN, buff=0.1).next_to(p2_steps, DOWN, buff=0.15)
        self.play(FadeOut(p2_steps[0]), Write(p2_sub[0]))
        self.wait(0.5)
        self.play(Write(p2_sub[1]))
        self.wait(0.5)

        # Result before normalization
        self.play(FadeOut(p2_steps[1:]), FadeOut(p2_sub))
        result2 = VGroup(
            MathTex(
                r"x^2 - \frac{1}{3} \quad\text{(subtract the }P_0\text{ component)}",
                font_size=22, color=WHITE,
            ),
            MathTex(
                r"\text{Normalize } (P(1)=1): \quad P_2(x) = \frac{3x^2 - 1}{2}",
                font_size=24, color=colors[2],
            ),
        ).arrange(DOWN, buff=0.15).next_to(axes, DOWN, buff=0.25)
        self.play(Write(result2[0]))
        self.wait(1)
        self.play(Write(result2[1]))
        self.wait(1)

        # Morph graph
        p2_graph = axes.plot(lambda x: (3 * x**2 - 1) / 2, color=colors[2], x_range=[-1, 1])
        self.play(ReplacementTransform(mono2_graph, p2_graph), FadeOut(result2))

        p2_tex = MathTex(r"P_2 = \tfrac{3x^2 - 1}{2}", color=colors[2], font_size=26)
        p2_tex.next_to(p1_tex, DOWN, buff=0.15).align_to(p1_tex, LEFT)
        self.play(FadeIn(p2_tex))
        poly_list.add(p2_tex)
        self.wait(0.5)

        # ── P₃ — show full work since user found it unclear ──
        new_step = Text("Step 4: f₃(x) = x³", font_size=22, color=GREY_A).next_to(title, DOWN, buff=0.25)
        self.play(ReplacementTransform(step_label, new_step))
        step_label = new_step

        mono3_graph = axes.plot(lambda x: x**3, color=RED, x_range=[-1, 1], stroke_width=3)
        self.play(Create(mono3_graph))

        # Inner products for P3
        p3_steps = VGroup(
            Text("Subtract projections onto P₀, P₁, P₂:", font_size=18, color=GREY_A),
            MathTex(
                r"\langle x^3, P_0 \rangle = 0, \quad \langle x^3, P_2 \rangle = 0",
                font_size=22,
            ),
            Text("(x³ is odd → pairing with even functions gives 0)", font_size=16, color=GREEN),
            MathTex(
                r"\langle x^3, P_1 \rangle = \int_{-1}^{1} x^3 \cdot x \, dx = \int_{-1}^{1} x^4 \, dx = \frac{2}{5}",
                font_size=22,
            ),
            MathTex(
                r"\langle P_1, P_1 \rangle = \int_{-1}^{1} x^2 \, dx = \frac{2}{3}",
                font_size=22,
            ),
        ).arrange(DOWN, buff=0.1).next_to(axes, DOWN, buff=0.2)
        self.play(FadeIn(p3_steps[0]))
        self.play(Write(p3_steps[1]))
        self.play(FadeIn(p3_steps[2]))
        self.wait(1)
        self.play(Write(p3_steps[3]))
        self.play(Write(p3_steps[4]))
        self.wait(1)

        # The subtraction
        self.play(FadeOut(p3_steps))
        p3_result = VGroup(
            MathTex(
                r"\text{proj}_{P_1}(x^3) = \frac{2/5}{2/3} \cdot x = \frac{3}{5}x",
                font_size=22, color=YELLOW,
            ),
            MathTex(
                r"x^3 - \frac{3}{5}x \quad\text{(subtract the }P_1\text{ component)}",
                font_size=22, color=WHITE,
            ),
            MathTex(
                r"\text{Normalize: } P_3(x) = \frac{5x^3 - 3x}{2}",
                font_size=24, color=colors[3],
            ),
        ).arrange(DOWN, buff=0.12).next_to(axes, DOWN, buff=0.2)
        self.play(Write(p3_result[0]))
        self.wait(1)
        self.play(Write(p3_result[1]))
        self.wait(1)
        self.play(Write(p3_result[2]))
        self.wait(1)

        p3_graph = axes.plot(lambda x: (5 * x**3 - 3 * x) / 2, color=colors[3], x_range=[-1, 1])
        self.play(ReplacementTransform(mono3_graph, p3_graph), FadeOut(p3_result))

        p3_tex = MathTex(r"P_3 = \tfrac{5x^3 - 3x}{2}", color=colors[3], font_size=26)
        p3_tex.next_to(p2_tex, DOWN, buff=0.15).align_to(p2_tex, LEFT)
        self.play(FadeIn(p3_tex))
        poly_list.add(p3_tex)
        self.wait(0.5)

        # Final moment
        self.play(FadeOut(step_label))
        discovery = Text(
            "We didn't define these polynomials — Gram-Schmidt forced them into existence.",
            font_size=20, color=BLUE_A,
        ).next_to(axes, DOWN, buff=0.4)
        self.play(FadeIn(discovery, shift=UP * 0.2))
        self.wait(2.5)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ──────────────────────────────────────────────────────────────────────
# Scene 4: Orthogonality Grid
# ──────────────────────────────────────────────────────────────────────
class S04_OrthogonalityGrid(Scene):
    """Visualize the inner product matrix with explanation of diagonal values."""

    def construct(self):
        title = Text("Verifying Orthogonality", font_size=36).to_edge(UP)
        self.play(Write(title))

        # 4x4 matrix of inner products
        n_polys = 4
        diag_vals = [r"2", r"\frac{2}{3}", r"\frac{2}{5}", r"\frac{2}{7}"]

        entries = []
        for i in range(n_polys):
            row = []
            for j in range(n_polys):
                if i == j:
                    val = MathTex(diag_vals[i], font_size=28, color=GOLD)
                else:
                    val = MathTex("0", font_size=28, color=BLUE_D)
                row.append(val)
            entries.append(row)

        labels = [MathTex(f"P_{i}", font_size=26) for i in range(n_polys)]

        cell_size = 1.0
        grid = VGroup()
        for i in range(n_polys):
            for j in range(n_polys):
                entries[i][j].move_to(RIGHT * (j - 1.5) * cell_size + DOWN * (i - 1.5) * cell_size)
                grid.add(entries[i][j])

        row_labels = VGroup(*[
            labels[i].copy().move_to(LEFT * 2.5 * cell_size + DOWN * (i - 1.5) * cell_size)
            for i in range(n_polys)
        ])
        col_labels = VGroup(*[
            labels[j].copy().move_to(RIGHT * (j - 1.5) * cell_size + UP * 2.5 * cell_size)
            for j in range(n_polys)
        ])

        left_bracket = MathTex(r"\Bigg[", font_size=80).next_to(grid, LEFT, buff=0.15)
        right_bracket = MathTex(r"\Bigg]", font_size=80).next_to(grid, RIGHT, buff=0.15)

        matrix_group = VGroup(grid, left_bracket, right_bracket, row_labels, col_labels)
        matrix_group.move_to(ORIGIN).shift(LEFT * 1)

        matrix_label = MathTex(r"\langle P_m, P_n \rangle", font_size=30).next_to(matrix_group, UP, buff=0.3)

        self.play(Write(matrix_label), FadeIn(row_labels), FadeIn(col_labels))
        self.play(FadeIn(left_bracket), FadeIn(right_bracket))

        # Off-diagonal first, then diagonal
        off_diag = [entries[i][j] for i in range(n_polys) for j in range(n_polys) if i != j]
        diag = [entries[i][i] for i in range(n_polys)]

        self.play(LaggedStart(*[FadeIn(e, scale=0.5) for e in off_diag], lag_ratio=0.05))
        self.wait(0.5)
        self.play(LaggedStart(*[FadeIn(e, scale=1.5) for e in diag], lag_ratio=0.15))
        self.wait(1)

        # Explain the diagonal values
        diag_explain = VGroup(
            Text("Diagonal values:", font_size=20, color=GOLD),
            MathTex(
                r"\langle P_n, P_n \rangle = \frac{2}{2n+1}",
                font_size=24, color=GOLD,
            ),
            Text("n=0 → 2,  n=1 → 2/3,  n=2 → 2/5,  n=3 → 2/7", font_size=16, color=GREY_A),
        ).arrange(DOWN, buff=0.15).shift(RIGHT * 4.5 + UP * 1.5)
        self.play(FadeIn(diag_explain))
        self.wait(2)

        # Verification visual: P1 * P2
        verify_title = Text("Verify: P₁ · P₂", font_size=20, color=GREEN).shift(RIGHT * 4.5 + DOWN * 0.3)
        axes_small = Axes(
            x_range=[-1.1, 1.1, 0.5],
            y_range=[-1, 1, 0.5],
            x_length=3.2,
            y_length=2.2,
            axis_config={"font_size": 12},
        ).shift(RIGHT * 4.5 + DOWN * 1.8)

        product_func = lambda x: x * (3 * x**2 - 1) / 2
        product_graph = axes_small.plot(product_func, color=GREEN, x_range=[-1, 1])
        pos_area = axes_small.get_area(product_graph, x_range=[0, 1], color=GREEN, opacity=0.3)
        neg_area = axes_small.get_area(product_graph, x_range=[-1, 0], color=RED, opacity=0.3)
        zero_label = MathTex("= 0", font_size=24, color=GREEN).next_to(axes_small, DOWN, buff=0.15)

        self.play(FadeIn(verify_title), Create(axes_small))
        self.play(Create(product_graph))
        self.play(FadeIn(pos_area), FadeIn(neg_area))
        self.play(Write(zero_label))
        self.wait(1)

        conclusion = Text(
            "A diagonal matrix — our polynomials form an orthogonal basis.",
            font_size=22, color=BLUE_A,
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(conclusion, shift=UP * 0.2))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ──────────────────────────────────────────────────────────────────────
# Scene 5: Function Approximation
# ──────────────────────────────────────────────────────────────────────
class S05_FunctionApproximation(Scene):
    """Approximate |x| using Legendre series — with explanation of coefficient formula."""

    def construct(self):
        title = Text("Why This Matters: Function Approximation", font_size=32).to_edge(UP)
        self.play(Write(title))

        # ── Derive the coefficient formula ──
        derive = VGroup(
            Text("How do we find the coefficients?", font_size=24, color=BLUE_A),
            MathTex(r"f(x) = c_0 P_0(x) + c_1 P_1(x) + c_2 P_2(x) + \cdots", font_size=26),
            Text("Take the inner product of both sides with Pₙ:", font_size=20, color=GREY_A),
            MathTex(
                r"\langle f, P_n \rangle = c_0 \underbrace{\langle P_0, P_n \rangle}_{0}"
                r"+ \cdots + c_n \underbrace{\langle P_n, P_n \rangle}_{\neq 0}"
                r"+ \cdots",
                font_size=22,
            ),
            Text("Orthogonality kills every term except the n-th!", font_size=20, color=GREEN),
            MathTex(
                r"c_n = \frac{\langle f, P_n \rangle}{\langle P_n, P_n \rangle}"
                r"= \frac{2n+1}{2} \int_{-1}^{1} f(x)\, P_n(x)\, dx",
                font_size=24, color=YELLOW,
            ),
        ).arrange(DOWN, buff=0.25).shift(DOWN * 0.3)

        for item in derive:
            self.play(FadeIn(item, shift=UP * 0.15))
            self.wait(1)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects if m != title])

        # ── Visual demonstration ──
        series_tex = MathTex(
            r"c_n = \frac{2n+1}{2} \int_{-1}^{1} f(x)\, P_n(x)\, dx",
            font_size=24, color=YELLOW,
        ).to_corner(UL, buff=0.4)
        self.play(FadeIn(series_tex))

        axes = Axes(
            x_range=[-1.2, 1.2, 0.5],
            y_range=[-0.3, 1.3, 0.5],
            x_length=7,
            y_length=4,
            axis_config={"include_numbers": True, "font_size": 20},
        ).shift(DOWN * 0.5)
        self.play(Create(axes), run_time=0.8)

        # Target function |x|
        target = axes.plot(lambda x: abs(x), color=WHITE, x_range=[-1, 1], stroke_width=3)
        target_label = MathTex("f(x) = |x|", font_size=28, color=WHITE).next_to(axes, RIGHT, buff=0.2).shift(UP)
        self.play(Create(target), FadeIn(target_label))
        self.wait(0.8)

        # Precompute Legendre coefficients
        from scipy.special import legendre
        from scipy.integrate import quad

        def legendre_coeffs(f, n_max):
            coeffs = []
            for n in range(n_max + 1):
                Pn = legendre(n)
                val, _ = quad(lambda x: f(x) * Pn(x), -1, 1)
                coeffs.append((2 * n + 1) / 2 * val)
            return coeffs

        coeffs = legendre_coeffs(abs, 20)

        def legendre_approx(x, n_terms, coeffs):
            result = 0
            for n in range(n_terms):
                Pn = legendre(n)
                result += coeffs[n] * Pn(x)
            return result

        # Animate adding terms
        n_terms_list = [1, 2, 4, 8, 16]
        colors_approx = [RED, ORANGE, YELLOW, GREEN, TEAL]
        current_graph = None
        current_label = None

        for idx, n_terms in enumerate(n_terms_list):
            approx_func = lambda x, nt=n_terms: legendre_approx(x, nt, coeffs)
            new_graph = axes.plot(approx_func, color=colors_approx[idx], x_range=[-1, 1])
            label_text = f"{n_terms} term{'s' if n_terms > 1 else ''}"
            new_label = Text(label_text, font_size=22, color=colors_approx[idx]).next_to(
                axes, RIGHT, buff=0.2
            ).shift(DOWN * 0.5)

            if current_graph is None:
                self.play(Create(new_graph), FadeIn(new_label))
            else:
                self.play(
                    ReplacementTransform(current_graph, new_graph),
                    FadeOut(current_label), FadeIn(new_label),
                )
            current_graph = new_graph
            current_label = new_label
            self.wait(0.6)

        self.wait(0.5)

        insight = Text(
            "Each coefficient is just one integral — orthogonality makes this trivial.",
            font_size=20, color=BLUE_A,
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(insight, shift=UP * 0.2))
        self.wait(1.5)

        physics = Text(
            "These polynomials are the backbone of spherical harmonics,\nmultipole expansions, and quantum mechanics.",
            font_size=18, color=GREY_B,
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeOut(insight), FadeIn(physics, shift=UP * 0.2))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


# ──────────────────────────────────────────────────────────────────────
# Scene 6: Closing Card
# ──────────────────────────────────────────────────────────────────────
class S06_ClosingCard(Scene):
    """Summary card with key formulas."""

    def construct(self):
        heading = Text("Legendre Polynomials", font_size=40, color=BLUE).to_edge(UP, buff=0.8)

        formulas = VGroup(
            MathTex(r"\langle f, g \rangle = \int_{-1}^{1} f(x)\,g(x)\,dx", font_size=30),
            MathTex(
                r"P_0 = 1, \quad P_1 = x, \quad P_2 = \tfrac{3x^2-1}{2}, \quad P_3 = \tfrac{5x^3-3x}{2}",
                font_size=28,
            ),
            MathTex(r"\langle P_m, P_n \rangle = \frac{2}{2n+1}\,\delta_{mn}", font_size=30),
            MathTex(r"f(x) = \sum_{n=0}^{\infty} c_n P_n(x)", font_size=30),
        ).arrange(DOWN, buff=0.5).next_to(heading, DOWN, buff=0.6)

        self.play(FadeIn(heading, shift=DOWN * 0.3))
        self.play(LaggedStart(*[FadeIn(f, shift=UP * 0.2) for f in formulas], lag_ratio=0.4))
        self.wait(4)
        self.play(*[FadeOut(m) for m in self.mobjects])
