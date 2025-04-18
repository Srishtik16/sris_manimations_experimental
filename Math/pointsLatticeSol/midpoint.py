from manim import *

class MidpointScene(Scene):
    def construct(self):
        # Title
        title = Text("Integer Midpoint", font_size=36)
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
        
        # Two points with same parity (odd, odd)
        p1 = (1, 1)
        p2 = (3, 5)
        
        # Calculate midpoint
        midpoint = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
        
        # Create points
        point1 = Dot(
            grid.c2p(*p1),
            color=RED,
            radius=0.1
        )
        point2 = Dot(
            grid.c2p(*p2),
            color=RED,
            radius=0.1
        )
        mid_point = Dot(
            grid.c2p(*midpoint),
            color=GREEN,
            radius=0.1
        )
        
        # Create labels
        label1 = MathTex(
            f"({p1[0]},{p1[1]})",
            font_size=24
        )
        label1.next_to(point1, UP, buff=0.2)
        
        label2 = MathTex(
            f"({p2[0]},{p2[1]})",
            font_size=24
        )
        label2.next_to(point2, UP, buff=0.2)
        
        mid_label = MathTex(
            f"({int(midpoint[0])},{int(midpoint[1])})",
            font_size=24,
            color=GREEN
        )
        mid_label.next_to(mid_point, UP, buff=0.2)
        
        # Create line between points
        line = Line(
            grid.c2p(*p1),
            grid.c2p(*p2),
            color=WHITE
        )
        
        # Create midpoint formula
        formula = MathTex(
            r"M = \left(\frac{1+3}{2}, \frac{1+5}{2}\right) = (2, 3)",
            font_size=28
        )
        formula.next_to(grid, DOWN, buff=1.0)
        
        # Create glowing effect for midpoint
        glow = Circle(
            radius=0.3,
            color=GREEN,
            fill_opacity=0.2
        )
        glow.move_to(mid_point)
        
        # Create success message
        success = Text(
            "This is an integer point!",
            font_size=24,
            color=GREEN
        )
        success.next_to(formula, DOWN, buff=0.5)
        
        # Animations
        self.play(Write(title))
        self.wait(0.5)
        self.play(Create(grid))
        self.wait(0.5)
        
        # Show points and labels
        self.play(
            FadeIn(point1),
            Write(label1),
            run_time=0.5
        )
        self.wait(0.3)
        
        self.play(
            FadeIn(point2),
            Write(label2),
            run_time=0.5
        )
        self.wait(0.3)
        
        # Draw line
        self.play(Create(line))
        self.wait(0.5)
        
        # Show midpoint formula
        self.play(Write(formula))
        self.wait(1)
        
        # Show midpoint
        self.play(
            FadeIn(mid_point),
            Write(mid_label),
            run_time=0.5
        )
        self.wait(0.5)
        
        # Add glowing effect and success message
        self.play(
            Create(glow),
            Write(success),
            run_time=1
        )
        self.wait(2)
        
        # Clear the scene
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(point1),
            FadeOut(point2),
            FadeOut(mid_point),
            FadeOut(label1),
            FadeOut(label2),
            FadeOut(mid_label),
            FadeOut(line),
            FadeOut(formula),
            FadeOut(glow),
            FadeOut(success)
        ) 