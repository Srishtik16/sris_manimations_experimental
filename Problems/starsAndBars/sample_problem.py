from manim import *

class SampleProblemScene(Scene):
    def construct(self):
        # Title
        title = Text("Sample Problem: Stars and Bars", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(1)

        # Problem statement
        problem = MathTex(
            r"x_1 + x_2 + x_3 = 4",
            r"\text{ where } x_i \geq 0"
        )
        problem.next_to(title, DOWN, buff=0.5)
        self.play(Write(problem))
        self.wait(1)

        # Problem breakdown
        breakdown = VGroup(
            MathTex(r"\text{Total stars (n)} = 4"),
            MathTex(r"\text{Number of variables (k)} = 3"),
            MathTex(r"\text{Bars needed} = k - 1 = 2"),
            MathTex(r"\text{Total slots} = n + k - 1 = 6")
        )
        breakdown.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        breakdown.next_to(problem, DOWN, buff=0.5)
        self.play(Write(breakdown))
        self.wait(1)

        # Formula
        formula = MathTex(
            r"C(n + k - 1, k - 1) = C(6, 2) = 15"
        )
        formula.next_to(breakdown, DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(1)

        # Clear previous elements
        self.play(
            FadeOut(title),
            FadeOut(problem),
            FadeOut(breakdown),
            FadeOut(formula)
        )

        # Show all configurations
        config_title = Text("All Possible Distributions", font_size=32, color=BLUE)
        config_title.to_edge(UP, buff=0.3)
        self.play(Write(config_title))

        # Create all possible distributions
        distributions = VGroup()
        count = 0
        for x1 in range(5):
            for x2 in range(5 - x1):
                x3 = 4 - x1 - x2
                dist = MathTex(
                    f"({x1}, {x2}, {x3})",
                    font_size=24
                )
                distributions.add(dist)
                count += 1
                if count == 15:
                    break
            if count == 15:
                break
        
        # Arrange distributions in a grid
        distributions.arrange_in_grid(rows=3, cols=5, buff=0.5)
        distributions.next_to(config_title, DOWN, buff=2.5)
        
        self.play(Write(distributions))
        self.wait(2)

        # Final message
        final_text = Text(
            "Total of 15 possible distributions",
            font_size=24,
            color=YELLOW
        )
        final_text.next_to(distributions, DOWN, buff=1.0)
        self.play(Write(final_text))
        self.wait(2)