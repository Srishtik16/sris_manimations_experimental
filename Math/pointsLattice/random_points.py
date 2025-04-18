from manim import *
import random

class RandomPointsScene(Scene):
    def construct(self):
        # Create 8x8 grid
        grid = NumberPlane(
            x_range=(1, 9, 1),
            y_range=(1, 9, 1),
            x_length=8,
            y_length=8,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
            }
        )
        grid.scale(0.7)
        grid.to_edge(UP, buff=1.0)
        
        # Add axis labels
        x_labels = VGroup()
        y_labels = VGroup()
        for i in range(1, 9):
            x_label = Text(str(i), font_size=20).next_to(grid.c2p(i, 1), DOWN, buff=0.1)
            y_label = Text(str(i), font_size=20).next_to(grid.c2p(1, i), LEFT, buff=0.1)
            x_labels.add(x_label)
            y_labels.add(y_label)
        
        # Create grid first
        self.play(Create(grid))
        self.play(Write(x_labels), Write(y_labels))
        
        # Title
        title = Text("Randomly Pick 5 Points", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Generate 5 random points
        points = []
        point_dots = VGroup()
        point_labels = VGroup()
        colors = [RED, GREEN, BLUE, YELLOW, PURPLE]
        
        for i in range(5):
            # Generate unique random coordinates
            while True:
                x = random.randint(1, 8)
                y = random.randint(1, 8)
                if (x, y) not in points:
                    points.append((x, y))
                    break
            
            # Create dot and label
            dot = Dot(grid.c2p(x, y), color=colors[i], radius=0.08)
            label = Text(f"({x},{y})", font_size=20, color=colors[i])
            label.next_to(dot, UP, buff=0.1)
            
            point_dots.add(dot)
            point_labels.add(label)
            
            # Animate placing the point
            self.play(
                Create(dot),
                Write(label),
                run_time=0.5
            )
            self.wait(0.2)
        
        # Add explanation text
        explanation = Text(
            "You're free to pick any 5 points from this 8×8 grid",
            font_size=24,
            color=YELLOW
        )
        explanation.next_to(grid, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(2)
        
        # Clear the scene
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(x_labels),
            FadeOut(y_labels),
            FadeOut(point_dots),
            FadeOut(point_labels),
            FadeOut(explanation)
        ) 