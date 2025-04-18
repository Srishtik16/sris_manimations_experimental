from manim import *
import random

class GoalScene(Scene):
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
        title = Text("What's the Goal?", font_size=36)
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
        
        # Question
        question = Text(
            "Is it always guaranteed that some two of these points\nhave a midpoint with integer coordinates?",
            font_size=24,
            color=YELLOW
        )
        question.next_to(grid, DOWN, buff=0.5)
        self.play(Write(question))
        self.wait(1)
        
        # Select two points and show their midpoint
        point1, point2 = points[0], points[1]
        x1, y1 = point1
        x2, y2 = point2
        
        # Create line between points
        line = Line(
            grid.c2p(x1, y1),
            grid.c2p(x2, y2),
            color=WHITE
        )
        
        # Calculate midpoint
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        
        # Create midpoint dot
        mid_dot = Dot(grid.c2p(mid_x, mid_y), color=WHITE, radius=0.08)
        
        # Midpoint formula
        formula = MathTex(
            r"\text{Midpoint} = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)",
            font_size=24
        )
        formula.next_to(question, DOWN, buff=0.5)
        
        # Fade out other points
        other_points = VGroup(*[dot for i, dot in enumerate(point_dots) if i not in [0, 1]])
        other_labels = VGroup(*[label for i, label in enumerate(point_labels) if i not in [0, 1]])
        
        self.play(
            FadeOut(other_points),
            FadeOut(other_labels),
            FadeOut(question)
        )
        
        # Show line and midpoint
        self.play(Create(line))
        self.play(Create(mid_dot))
        self.play(Write(formula))
        
        self.wait(2)
        
        # Clear the scene
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(x_labels),
            FadeOut(y_labels),
            FadeOut(point_dots),
            FadeOut(point_labels),
            FadeOut(line),
            FadeOut(mid_dot),
            FadeOut(formula)
        )