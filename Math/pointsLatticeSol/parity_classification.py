from manim import *

class ParityClassificationScene(Scene):
    def construct(self):
        # Title
        title = Text("Classifying Points by Parity", font_size=36)
        title.to_edge(UP, buff=0.3)  # Reduced top buffer
        
        # Create grid
        grid = NumberPlane(
            x_range=[0, 9, 1],
            y_range=[0, 9, 1],
            x_length=8,
            y_length=8,
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
            }
        )
        grid.next_to(title, DOWN, buff=0.4)  # Reduced buffer between title and grid
        grid.scale(0.7)  # Slightly larger scale
        
        # Sample points with their correct parity values
        points = [
            (1, 1, (1, 1)),     # (odd, odd)
            (2, 2, (0, 0)),     # (even, even)
            (3, 4, (1, 0)),     # (odd, even)
            (6, 3, (0, 1)),     # (even, odd)
            (5, 7, (1, 1))      # (odd, odd)
        ]
        
        # Create dots, coordinate labels, and parity labels
        dots = VGroup()
        coord_labels = VGroup()
        parity_labels = VGroup()
        
        # Colors for different parity groups
        parity_colors = {
            (0, 0): GREEN,  # even, even
            (0, 1): YELLOW, # even, odd
            (1, 0): BLUE,   # odd, even
            (1, 1): RED     # odd, odd
        }
        
        for x, y, _ in points:
            # Calculate actual parity
            parity = (x % 2, y % 2)
            
            # Create dot with color based on parity
            dot = Dot(
                grid.c2p(x, y),
                color=parity_colors[parity],
                radius=0.1
            )
            dots.add(dot)
            
            # Create coordinate label
            coord_label = MathTex(
                f"({x},{y})",
                font_size=24
            )
            coord_label.next_to(dot, UP, buff=0.2)
            coord_labels.add(coord_label)
            
            # Create parity label
            parity_label = MathTex(
                f"\\rightarrow ({parity[0]},{parity[1]})",
                font_size=20,
                color=parity_colors[parity]
            )
            parity_label.next_to(coord_label, RIGHT, buff=0.2)
            parity_labels.add(parity_label)
        
        # Create legend
        legend = VGroup()
        legend_title = Text("Parity Types:", font_size=24)
        legend.add(legend_title)
        
        for parity, color in parity_colors.items():
            item = VGroup(
                Dot(color=color, radius=0.1),
                MathTex(f"({parity[0]},{parity[1]})", font_size=20)
            )
            item.arrange(RIGHT, buff=0.2)
            legend.add(item)
        
        legend.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        legend.next_to(grid, RIGHT, buff=0.8)
        
        # Animations
        self.play(Write(title))
        self.wait(0.5)
        self.play(Create(grid))
        self.wait(0.5)
        
        # Animate points and labels
        for dot, coord_label, parity_label in zip(dots, coord_labels, parity_labels):
            self.play(
                FadeIn(dot),
                Write(coord_label),
                Write(parity_label),
                run_time=0.5
            )
            self.wait(0.3)
        
        # Show legend
        self.play(Write(legend))
        self.wait(2)
        
        # Clear the scene
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(dots),
            FadeOut(coord_labels),
            FadeOut(parity_labels),
            FadeOut(legend)
        ) 