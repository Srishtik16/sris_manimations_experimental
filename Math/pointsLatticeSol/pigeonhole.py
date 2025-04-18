from manim import *

class PigeonholeScene(Scene):
    def construct(self):
        # Title
        title = Text("Pigeonhole Principle", font_size=36)
        title.to_edge(UP, buff=0.3)
        
        # Create bins
        bins = {
            (0, 0): "Even, Even",
            (0, 1): "Even, Odd",
            (1, 0): "Odd, Even",
            (1, 1): "Odd, Odd"
        }
        
        # Create bin rectangles
        bin_rects = VGroup()
        bin_labels = VGroup()
        bin_points = VGroup()
        
        # Colors for different parity groups
        parity_colors = {
            (0, 0): GREEN,
            (0, 1): YELLOW,
            (1, 0): BLUE,
            (1, 1): RED
        }
        
        # Create bins and labels
        for i, ((x_par, y_par), label) in enumerate(bins.items()):
            # Create bin rectangle
            rect = Rectangle(
                width=2,
                height=1.5,
                color=parity_colors[(x_par, y_par)],
                fill_opacity=0.2
            )
            
            # Position bins in a 2x2 grid
            if i < 2:
                rect.to_edge(LEFT, buff=1.0)
            else:
                rect.to_edge(RIGHT, buff=1.0)
            if i % 2 == 0:
                rect.to_edge(UP, buff=2.0)
            else:
                rect.to_edge(DOWN, buff=2.0)
            
            # Create bin label
            bin_label = MathTex(
                f"({x_par},{y_par})",
                font_size=24
            )
            bin_label.next_to(rect, UP, buff=0.2)
            
            bin_rects.add(rect)
            bin_labels.add(bin_label)
        
        # Sample points with their parity
        points = [
            (1, 1, (1, 1)),     # (odd, odd)
            (2, 2, (0, 0)),     # (even, even)
            (3, 5, (1, 1)),     # (odd, odd)
            (6, 3, (0, 1)),     # (even, odd)
            (5, 6, (1, 0))      # (odd, even)
        ]
        
        # Create points and place them in bins
        for x, y, parity in points:
            point = Dot(
                color=parity_colors[parity],
                radius=0.1
            )
            
            # Find the corresponding bin
            for i, ((x_par, y_par), _) in enumerate(bins.items()):
                if (x_par, y_par) == parity:
                    # Position point inside the bin
                    point.move_to(bin_rects[i].get_center())
                    # Add some random offset within the bin
                    point.shift(np.random.uniform(-0.5, 0.5) * RIGHT)
                    point.shift(np.random.uniform(-0.5, 0.5) * UP)
                    break
            
            bin_points.add(point)
        
        # Create explanation text
        explanation = Text(
            "Only 4 bins, but 5 points → at least one bin has ≥ 2",
            font_size=24
        )
        explanation.next_to(bin_rects, DOWN, buff=1.0)
        
        # Highlight the repeated class (odd, odd)
        highlight_rect = Rectangle(
            width=2.2,
            height=1.7,
            color=RED,
            fill_opacity=0.1
        )
        highlight_rect.move_to(bin_rects[3])  # (1,1) bin
        
        # Animations
        self.play(Write(title))
        self.wait(0.5)
        
        # Show bins
        self.play(
            Create(bin_rects),
            Write(bin_labels),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Add points to bins
        self.play(
            LaggedStart(
                *[FadeIn(point) for point in bin_points],
                lag_ratio=0.2
            ),
            run_time=2
        )
        self.wait(0.5)
        
        # Show explanation
        self.play(Write(explanation))
        self.wait(1)
        
        # Highlight repeated class
        self.play(
            Create(highlight_rect),
            bin_rects[3].animate.set_fill(opacity=0.3),
            run_time=1
        )
        self.wait(2)
        
        # Clear the scene
        self.play(
            FadeOut(title),
            FadeOut(bin_rects),
            FadeOut(bin_labels),
            FadeOut(bin_points),
            FadeOut(explanation),
            FadeOut(highlight_rect)
        ) 