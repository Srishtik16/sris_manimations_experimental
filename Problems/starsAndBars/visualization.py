from manim import *

class VisualizationScene(Scene):
    def construct(self):
        # Title
        title = Text("Visualizing Stars and Bars", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(1)

        # Create initial stars and bars
        stars_bars = VGroup()
        for i in range(5):
            star = Star(color=YELLOW, fill_opacity=1, outer_radius=0.2)
            stars_bars.add(star)
            if i < 4:  # Add bars between stars
                bar = Text("|", font_size=36, color=WHITE)
                stars_bars.add(bar)
        stars_bars.arrange(RIGHT, buff=0.2)
        stars_bars.next_to(title, DOWN, buff=0.8)
        
        # Create variable labels
        variables = VGroup()
        for i in range(3):
            var = MathTex(f"x_{i+1}", font_size=24)
            variables.add(var)
        variables.arrange(RIGHT, buff=1.5)
        variables.next_to(stars_bars, DOWN, buff=0.5)
        
        # Create value labels
        values = VGroup()
        for i in range(3):
            val = MathTex("3", "1", "1", font_size=24)[i]
            values.add(val)
        values.arrange(RIGHT, buff=1.5)
        values.next_to(variables, DOWN, buff=0.3)
        
        # Align values with variables
        for i in range(3):
            values[i].move_to(variables[i].get_center() + DOWN * 0.3)

        # Show initial configuration
        self.play(Create(stars_bars))
        self.wait(1)
        self.play(
            Create(variables),
            Create(values)
        )
        self.wait(1)

        # Create arrows
        arrows = VGroup()
        for i in range(3):
            start = stars_bars[2*i].get_center()  # Star position
            end = values[i].get_center()
            arrow = Arrow(start, end, color=YELLOW, buff=0.2)
            arrows.add(arrow)
        
        self.play(Create(arrows))
        self.wait(2)

        # Animate different configurations
        configurations = [
            [3, 1, 1],  # 3,1,1
            [2, 2, 1],  # 2,2,1
            [1, 3, 1],  # 1,3,1
            [1, 1, 3],  # 1,1,3
            [2, 1, 2]   # 2,1,2
        ]

        new_values = [
            ["3", "1", "1"],
            ["2", "2", "1"],
            ["1", "3", "1"],
            ["1", "1", "3"],
            ["2", "1", "2"]
        ]

        for config, vals in zip(configurations[1:], new_values[1:]):
            # Create new stars and bars
            new_stars_bars = VGroup()
            for i, count in enumerate(config):
                # Add stars
                for _ in range(count):
                    star = Star(color=YELLOW, fill_opacity=1, outer_radius=0.2)
                    new_stars_bars.add(star)
                # Add bar if not last group
                if i < len(config) - 1:
                    bar = Text("|", font_size=36, color=WHITE)
                    new_stars_bars.add(bar)
            new_stars_bars.arrange(RIGHT, buff=0.2)
            new_stars_bars.move_to(stars_bars.get_center())

            # Update values
            new_vals = VGroup()
            for val in vals:
                new_vals.add(MathTex(val, font_size=24))
            new_vals.arrange(RIGHT, buff=1.5)
            new_vals.next_to(variables, DOWN, buff=0.3)
            
            # Align new values
            for i in range(3):
                new_vals[i].move_to(variables[i].get_center() + DOWN * 0.3)

            # Animate transition
            self.play(
                Transform(stars_bars, new_stars_bars),
                Transform(values, new_vals),
                run_time=1.5
            )
            self.wait(1)

        # Final explanation
        explanation = Text(
            "Each arrangement represents a different solution",
            font_size=24,
            color=YELLOW
        )
        explanation.next_to(values, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(2) 