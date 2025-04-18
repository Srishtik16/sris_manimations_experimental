from manim import *

class SummaryScene(Scene):
    def construct(self):
        # Title
        title = Text("Stars and Bars: Key Takeaways", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # Key points
        points = VGroup(
            MathTex(r"\text{Stars} = \text{values to distribute}"),
            MathTex(r"\text{Bars} = \text{dividers between variables}"),
            MathTex(r"\text{Non-negative case: } C(n + k - 1, k - 1)"),
            MathTex(r"\text{Positive case: } C(n - 1, k - 1)")
        )

        # Create a grid layout for points and examples
        grid = VGroup()
        for i, point in enumerate(points):
            row = VGroup()
            row.add(point)
            row.arrange(RIGHT, buff=0.5, aligned_edge=LEFT)
            grid.add(row)
        
        # Arrange the grid vertically
        grid.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        grid.next_to(title, DOWN, buff=0.8)

        # Animate points and examples
        for row in grid:
            self.play(Write(row[0]))
            if len(row) > 1:
                self.play(Create(row[1]))
            self.wait(0.5)

        self.wait(1)

        # Final message
        final_text = Text(
            "A powerful technique for integer partitions and distribution problems!",
            font_size=32,
            color=YELLOW
        )
        final_text.next_to(grid, DOWN, buff=1.0)
        
        # Add an effect to the final text
        self.play(
            Write(final_text),
            final_text.animate.scale(1.1).set_color(GREEN),
            rate_func=linear,
            run_time=2
        )
        
        # Keep the final text on screen
        self.wait(5)  # Extended wait time to ensure text stays visible 