from manim import *

class SamplePointsScene(Scene):
    def construct(self):
        # Title
        title = Text("Sample Points on 8×8 Grid", font_size=36)
        title.to_edge(UP, buff=0.3)
        
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
        grid.next_to(title, DOWN, buff=0.4)
        grid.scale(0.7)
        
        # Sample points
        points = [
            (1, 1),  # (even, even)
            (2, 2),  # (even, even)
            (3, 5),  # (odd, odd)
            (7, 3),  # (odd, odd)
            (5, 7)   # (odd, odd)
        ]
        
        # Create dots and labels
        dots = VGroup()
        labels = VGroup()
        
        for i, (x, y) in enumerate(points):
            # Create dot
            dot = Dot(
                grid.c2p(x, y),
                color=RED,
                radius=0.1
            )
            dots.add(dot)
            
            # Create label
            label = MathTex(
                f"({x},{y})",
                font_size=24
            )
            label.next_to(dot, UP, buff=0.2)
            labels.add(label)
        
        # Animations
        self.play(Write(title))
        self.wait(0.5)
        self.play(Create(grid))
        self.wait(0.5)
        
        # Animate points and labels
        for dot, label in zip(dots, labels):
            self.play(
                FadeIn(dot),
                Write(label),
                run_time=0.5
            )
            self.wait(0.3)
        
        self.wait(2)
        
        # Clear the scene
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(dots),
            FadeOut(labels)
        ) 