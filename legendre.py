from manim import *
import numpy as np


class PowerOfPerpendicular(Scene):
    """Scene 1: Review orthogonal bases in R^2."""

    def construct(self):
        # Title
        title = Text("When Polynomials Become Perpendicular", font_size=42)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.scale(0.5).to_edge(UP))

        # 2D axes with basis vectors
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5,
            y_length=5,
            background_line_style={"stroke_opacity": 0.3},
        ).shift(DOWN * 0.3)
        self.play(Create(plane), run_time=0.8)

        # Basis vectors
        e1 = Arrow(plane.c2p(0, 0), plane.c2p(1, 0), buff=0, color=BLUE, stroke_width=5)
        e2 = Arrow(plane.c2p(0, 0), plane.c2p(0, 1), buff=0, color=YELLOW, stroke_width=5)
        e1_label = MathTex(r"\mathbf{e}_1", color=BLUE).next_to(e1, DOWN, buff=0.15)
        e2_label = MathTex(r"\mathbf{e}_2", color=YELLOW).next_to(e2, LEFT, buff=0.15)
        self.play(GrowArrow(e1), GrowArrow(e2), FadeIn(e1_label), FadeIn(e2_label))

        # Arbitrary vector
        v = Arrow(plane.c2p(0, 0), plane.c2p(2.3, 1.7), buff=0, color=WHITE, stroke_width=4)
        v_label = MathTex(r"\mathbf{v}", color=WHITE).next_to(v.get_end(), UR, buff=0.1)
        self.play(GrowArrow(v), FadeIn(v_label))
        self.wait(0.3)

        # Projection lines
        proj_x = DashedLine(
            plane.c2p(2.3, 1.7), plane.c2p(2.3, 0), color=BLUE_A, stroke_width=2
        )
        proj_y = DashedLine(
            plane.c2p(2.3, 1.7), plane.c2p(0, 1.7), color=YELLOW_A, stroke_width=2
        )
        # Projection vectors
        comp_x = Arrow(plane.c2p(0, 0), plane.c2p(2.3, 0), buff=0, color=BLUE_B, stroke_width=4)
        comp_y = Arrow(plane.c2p(0, 0), plane.c2p(0, 1.7), buff=0, color=YELLOW_B, stroke_width=4)
        self.play(Create(proj_x), Create(proj_y), run_time=0.6)
        self.play(GrowArrow(comp_x), GrowArrow(comp_y), run_time=0.6)

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
        self.wait(0.5)

        # Transition text
        question = Text(
            "But what if our vectors aren't arrows...\nbut functions?",
            font_size=32,
            color=BLUE_A,
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeOut(formula), FadeIn(question, shift=UP * 0.3))
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects])


class FunctionsAsVectors(Scene):
    """Scene 2: Define inner product on functions, show x and x^2 are orthogonal."""

    def construct(self):
        # Analogy side by side
        dot_tex = MathTex(
            r"\langle \mathbf{v}, \mathbf{w} \rangle",
            r"= \sum_i v_i \, w_i",
        ).scale(0.8)
        func_tex = MathTex(
            r"\langle f, g \rangle",
            r"= \int_{-1}^{1} f(x)\, g(x)\, dx",
        ).scale(0.8)
        dot_tex.set_color(BLUE)
        func_tex.set_color(YELLOW)

        analogy = VGroup(dot_tex, func_tex).arrange(DOWN, buff=0.6).to_edge(UP, buff=0.8)
        arrow = MathTex(r"\Downarrow").scale(1.2).move_to(analogy)

        self.play(Write(dot_tex))
        self.wait(0.5)
        self.play(FadeIn(arrow, shift=DOWN * 0.2))
        self.play(Write(func_tex))
        self.wait(0.8)
        self.play(FadeOut(arrow), analogy.animate.scale(0.6).to_corner(UL))

        # Axes
        axes = Axes(
            x_range=[-1.2, 1.2, 0.5],
            y_range=[-1.2, 1.2, 0.5],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True, "font_size": 20},
        ).shift(DOWN * 0.5)
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), FadeIn(axes_labels), run_time=0.8)

        # f(x) = x, g(x) = x^2
        f_graph = axes.plot(lambda x: x, color=BLUE, x_range=[-1, 1])
        g_graph = axes.plot(lambda x: x**2, color=YELLOW, x_range=[-1, 1])
        f_label = MathTex("f(x) = x", color=BLUE, font_size=30).next_to(axes, RIGHT, buff=0.3).shift(UP)
        g_label = MathTex("g(x) = x^2", color=YELLOW, font_size=30).next_to(f_label, DOWN, buff=0.3)
        self.play(Create(f_graph), FadeIn(f_label), run_time=0.6)
        self.play(Create(g_graph), FadeIn(g_label), run_time=0.6)
        self.wait(0.5)

        # Product f*g = x^3
        product_graph = axes.plot(lambda x: x**3, color=GREEN, x_range=[-1, 1])
        product_label = MathTex("f \\cdot g = x^3", color=GREEN, font_size=30).next_to(g_label, DOWN, buff=0.3)
        self.play(
            FadeOut(f_graph), FadeOut(g_graph),
            Create(product_graph), FadeIn(product_label),
            run_time=0.8,
        )

        # Shade positive and negative areas
        pos_area = axes.get_area(product_graph, x_range=[0, 1], color=GREEN, opacity=0.4)
        neg_area = axes.get_area(product_graph, x_range=[-1, 0], color=RED, opacity=0.4)
        self.play(FadeIn(pos_area), FadeIn(neg_area))

        # Result
        result = MathTex(
            r"\int_{-1}^{1} x^3 \, dx = 0",
            color=WHITE,
            font_size=36,
        ).to_edge(DOWN, buff=0.5)
        perp = Text("These functions are orthogonal!", font_size=28, color=GREEN_A).next_to(result, DOWN, buff=0.2)
        self.play(Write(result))
        self.play(FadeIn(perp, shift=UP * 0.2))
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects])


class GramSchmidtOnPolynomials(Scene):
    """Scene 3: Apply Gram-Schmidt to {1, x, x², x³} and discover Legendre polynomials."""

    def construct(self):
        title = Text("Gram-Schmidt on Polynomials", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Inner product reminder in corner
        ip_reminder = MathTex(
            r"\langle f, g \rangle = \int_{-1}^{1} f(x)\,g(x)\,dx",
            font_size=24,
            color=GREY_B,
        ).to_corner(UR)
        self.play(FadeIn(ip_reminder))

        # Axes for plotting polynomials
        axes = Axes(
            x_range=[-1.2, 1.2, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=7,
            y_length=4,
            axis_config={"include_numbers": True, "font_size": 20},
        ).shift(DOWN * 0.3 + LEFT * 0.5)
        self.play(Create(axes), run_time=0.8)

        # Running list of completed polynomials on the right
        poly_list_title = Text("Legendre Polynomials", font_size=20, color=GREEN).to_edge(RIGHT).shift(UP * 2)
        poly_list = VGroup(poly_list_title)
        self.play(FadeIn(poly_list_title))

        # Color for each degree
        colors = [BLUE, YELLOW, GREEN, RED_B]

        # ── P₀ ──
        step_label = Text("Step 1: Start with f₀(x) = 1", font_size=22, color=GREY_A).next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(step_label))

        p0_graph = axes.plot(lambda x: 1, color=colors[0], x_range=[-1, 1])
        p0_tex = MathTex(r"P_0(x) = 1", color=colors[0], font_size=28)
        p0_tex.next_to(poly_list_title, DOWN, buff=0.3).align_to(poly_list_title, LEFT)
        self.play(Create(p0_graph))
        self.play(FadeIn(p0_tex))
        poly_list.add(p0_tex)
        self.wait(0.5)

        # ── P₁ ──
        new_step = Text("Step 2: Start with f₁(x) = x", font_size=22, color=GREY_A).next_to(title, DOWN, buff=0.3)
        self.play(ReplacementTransform(step_label, new_step))
        step_label = new_step

        mono_graph = axes.plot(lambda x: x, color=RED, x_range=[-1, 1], stroke_width=3)
        self.play(Create(mono_graph))

        # Show inner product computation
        ip_calc = MathTex(
            r"\langle x, P_0 \rangle = \int_{-1}^{1} x \, dx = 0",
            font_size=26,
            color=GREY_A,
        ).next_to(axes, DOWN, buff=0.4)
        self.play(Write(ip_calc))
        self.wait(0.5)

        already_ortho = Text("Already orthogonal!", font_size=20, color=GREEN).next_to(ip_calc, DOWN, buff=0.15)
        self.play(FadeIn(already_ortho))
        self.wait(0.3)

        p1_graph = axes.plot(lambda x: x, color=colors[1], x_range=[-1, 1])
        self.play(
            ReplacementTransform(mono_graph, p1_graph),
            FadeOut(ip_calc), FadeOut(already_ortho),
        )
        p1_tex = MathTex(r"P_1(x) = x", color=colors[1], font_size=28)
        p1_tex.next_to(p0_tex, DOWN, buff=0.2).align_to(p0_tex, LEFT)
        self.play(FadeIn(p1_tex))
        poly_list.add(p1_tex)
        self.wait(0.3)

        # ── P₂ ──
        new_step = Text("Step 3: Start with f₂(x) = x²", font_size=22, color=GREY_A).next_to(title, DOWN, buff=0.3)
        self.play(ReplacementTransform(step_label, new_step))
        step_label = new_step

        mono2_graph = axes.plot(lambda x: x**2, color=RED, x_range=[-1, 1], stroke_width=3)
        self.play(Create(mono2_graph))

        # Inner product with P0
        ip1 = MathTex(
            r"\langle x^2, P_0 \rangle = \int_{-1}^{1} x^2 \, dx = \frac{2}{3}",
            font_size=24,
            color=GREY_A,
        ).next_to(axes, DOWN, buff=0.3)
        self.play(Write(ip1))
        self.wait(0.3)

        # Inner product with P1
        ip2 = MathTex(
            r"\langle x^2, P_1 \rangle = \int_{-1}^{1} x^3 \, dx = 0",
            font_size=24,
            color=GREY_A,
        ).next_to(ip1, DOWN, buff=0.15)
        self.play(Write(ip2))
        self.wait(0.3)

        # Subtraction step
        subtract = MathTex(
            r"x^2 - \frac{\langle x^2, P_0\rangle}{\langle P_0, P_0\rangle} P_0",
            r"= x^2 - \frac{1}{3}",
            font_size=24,
            color=WHITE,
        ).next_to(ip2, DOWN, buff=0.15)
        self.play(FadeOut(ip1), FadeOut(ip2), Write(subtract))
        self.wait(0.3)

        # Normalize
        normalize = MathTex(
            r"P_2(x) = \frac{3x^2 - 1}{2}",
            font_size=28,
            color=colors[2],
        ).next_to(subtract, DOWN, buff=0.15)
        self.play(Write(normalize))

        # Morph the graph
        p2_func = lambda x: (3 * x**2 - 1) / 2
        p2_graph = axes.plot(p2_func, color=colors[2], x_range=[-1, 1])
        self.play(
            ReplacementTransform(mono2_graph, p2_graph),
            FadeOut(subtract), FadeOut(normalize),
        )

        p2_tex = MathTex(r"P_2(x) = \tfrac{3x^2 - 1}{2}", color=colors[2], font_size=28)
        p2_tex.next_to(p1_tex, DOWN, buff=0.2).align_to(p1_tex, LEFT)
        self.play(FadeIn(p2_tex))
        poly_list.add(p2_tex)
        self.wait(0.3)

        # ── P₃ (faster) ──
        new_step = Text("Step 4: Start with f₃(x) = x³", font_size=22, color=GREY_A).next_to(title, DOWN, buff=0.3)
        self.play(ReplacementTransform(step_label, new_step))
        step_label = new_step

        mono3_graph = axes.plot(lambda x: x**3, color=RED, x_range=[-1, 1], stroke_width=3)
        self.play(Create(mono3_graph))

        # Faster — just show the result
        result3 = MathTex(
            r"x^3 - \frac{3}{5}x \;\longrightarrow\; P_3(x) = \frac{5x^3 - 3x}{2}",
            font_size=24,
            color=WHITE,
        ).next_to(axes, DOWN, buff=0.3)
        self.play(Write(result3))
        self.wait(0.5)

        p3_func = lambda x: (5 * x**3 - 3 * x) / 2
        p3_graph = axes.plot(p3_func, color=colors[3], x_range=[-1, 1])
        self.play(
            ReplacementTransform(mono3_graph, p3_graph),
            FadeOut(result3),
        )

        p3_tex = MathTex(r"P_3(x) = \tfrac{5x^3 - 3x}{2}", color=colors[3], font_size=28)
        p3_tex.next_to(p2_tex, DOWN, buff=0.2).align_to(p2_tex, LEFT)
        self.play(FadeIn(p3_tex))
        poly_list.add(p3_tex)
        self.wait(0.3)

        # Final moment: all four on the axes together
        self.play(FadeOut(step_label))
        discovery = Text(
            "We didn't define these — Gram-Schmidt forced them into existence.",
            font_size=22,
            color=BLUE_A,
        ).next_to(axes, DOWN, buff=0.4)
        self.play(FadeIn(discovery, shift=UP * 0.2))
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects])


class OrthogonalityGrid(Scene):
    """Scene 4: Visualize the inner product matrix — diagonal = nonzero, off-diagonal = 0."""

    def construct(self):
        title = Text("Verifying Orthogonality", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Build the 4x4 matrix of inner products
        # <P_m, P_n> = 2/(2n+1) * delta_{mn}
        n_polys = 4
        diag_vals = [r"\frac{2}{%d}" % (2 * n + 1) for n in range(n_polys)]  # 2, 2/3, 2/5, 2/7

        # Create matrix entries
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

        # Row/column labels
        labels = [MathTex(f"P_{i}", font_size=26) for i in range(n_polys)]

        # Arrange into a grid
        cell_size = 1.0
        grid = VGroup()
        for i in range(n_polys):
            for j in range(n_polys):
                entries[i][j].move_to(
                    RIGHT * (j - 1.5) * cell_size + DOWN * (i - 1.5) * cell_size
                )
                grid.add(entries[i][j])

        # Add row labels (left)
        row_labels = VGroup()
        for i in range(n_polys):
            lbl = labels[i].copy().move_to(
                LEFT * 2.5 * cell_size + DOWN * (i - 1.5) * cell_size
            )
            row_labels.add(lbl)

        # Add column labels (top)
        col_labels = VGroup()
        for j in range(n_polys):
            lbl = labels[j].copy().move_to(
                RIGHT * (j - 1.5) * cell_size + UP * 2.5 * cell_size
            )
            col_labels.add(lbl)

        # Bracket decoration
        left_bracket = MathTex(r"\Bigg[", font_size=80).next_to(grid, LEFT, buff=0.15)
        right_bracket = MathTex(r"\Bigg]", font_size=80).next_to(grid, RIGHT, buff=0.15)

        matrix_group = VGroup(grid, left_bracket, right_bracket, row_labels, col_labels)
        matrix_group.move_to(ORIGIN).shift(LEFT * 1)

        # Header
        matrix_label = MathTex(
            r"\langle P_m, P_n \rangle",
            font_size=30,
        ).next_to(matrix_group, UP, buff=0.3)

        self.play(Write(matrix_label), FadeIn(row_labels), FadeIn(col_labels))
        self.play(FadeIn(left_bracket), FadeIn(right_bracket))

        # Animate entries appearing — off-diagonal first, then diagonal
        off_diag = [entries[i][j] for i in range(n_polys) for j in range(n_polys) if i != j]
        diag = [entries[i][i] for i in range(n_polys)]

        self.play(LaggedStart(*[FadeIn(e, scale=0.5) for e in off_diag], lag_ratio=0.05))
        self.wait(0.3)
        self.play(LaggedStart(*[FadeIn(e, scale=1.5) for e in diag], lag_ratio=0.1))
        self.wait(0.5)

        # Verification visual on the right: pick P1 * P2
        verify_title = Text("Verify: P1 * P2", font_size=22, color=GREEN).shift(RIGHT * 4.5 + UP * 2)
        axes_small = Axes(
            x_range=[-1.1, 1.1, 0.5],
            y_range=[-1, 1, 0.5],
            x_length=3.5,
            y_length=2.5,
            axis_config={"font_size": 14},
        ).shift(RIGHT * 4.5 + DOWN * 0.2)

        product_func = lambda x: x * (3 * x**2 - 1) / 2
        product_graph = axes_small.plot(product_func, color=GREEN, x_range=[-1, 1])
        pos_area = axes_small.get_area(product_graph, x_range=[0, 1], color=GREEN, opacity=0.3)
        neg_area = axes_small.get_area(product_graph, x_range=[-1, 0], color=RED, opacity=0.3)
        zero_label = MathTex("= 0", font_size=28, color=GREEN).next_to(axes_small, DOWN, buff=0.2)

        self.play(FadeIn(verify_title), Create(axes_small))
        self.play(Create(product_graph))
        self.play(FadeIn(pos_area), FadeIn(neg_area))
        self.play(Write(zero_label))
        self.wait(0.5)

        conclusion = Text(
            "A diagonal matrix — our polynomials are an orthogonal basis.",
            font_size=22,
            color=BLUE_A,
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(conclusion, shift=UP * 0.2))
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects])


class FunctionApproximation(Scene):
    """Scene 5: Approximate |x| using Legendre series — the payoff."""

    def construct(self):
        title = Text("Why This Matters: Function Approximation", font_size=32).to_edge(UP)
        self.play(Write(title))

        # Fourier-Legendre series formula
        series_tex = MathTex(
            r"f(x) = \sum_{n=0}^{\infty} c_n P_n(x), \quad c_n = \frac{2n+1}{2}\int_{-1}^{1} f(x) P_n(x)\,dx",
            font_size=26,
        ).next_to(title, DOWN, buff=0.3)
        self.play(Write(series_tex))
        self.wait(0.5)

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
        self.wait(0.5)

        # Precompute Legendre coefficients for |x|
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
            label_text = f"n = {n_terms} term{'s' if n_terms > 1 else ''}"
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
            self.wait(0.4)

        insight = Text(
            "Coefficients are just inner products — the power of orthogonality.",
            font_size=22,
            color=BLUE_A,
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(insight, shift=UP * 0.2))
        self.wait(1)

        # Physics connection
        physics = Text(
            "These polynomials are the backbone of spherical harmonics,\nmultipole expansions, and quantum mechanics.",
            font_size=20,
            color=GREY_B,
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeOut(insight), FadeIn(physics, shift=UP * 0.2))
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects])


class ClosingCard(Scene):
    """Scene 6: Summary card with key formulas."""

    def construct(self):
        heading = Text("Legendre Polynomials", font_size=40, color=BLUE).to_edge(UP, buff=0.8)

        formulas = VGroup(
            MathTex(r"\langle f, g \rangle = \int_{-1}^{1} f(x)\,g(x)\,dx", font_size=30),
            MathTex(r"P_0 = 1, \quad P_1 = x, \quad P_2 = \tfrac{3x^2-1}{2}, \quad P_3 = \tfrac{5x^3-3x}{2}", font_size=28),
            MathTex(r"\langle P_m, P_n \rangle = \frac{2}{2n+1}\,\delta_{mn}", font_size=30),
            MathTex(r"f(x) = \sum_{n=0}^{\infty} c_n P_n(x)", font_size=30),
        ).arrange(DOWN, buff=0.5).next_to(heading, DOWN, buff=0.6)

        self.play(FadeIn(heading, shift=DOWN * 0.3))
        self.play(LaggedStart(*[FadeIn(f, shift=UP * 0.2) for f in formulas], lag_ratio=0.3))
        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects])
