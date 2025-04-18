from manim import *

class IntegerMidpointsScene(Scene):
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
        title = Text("What Does 'Integer Midpoint' Mean?", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Example 1: Non-integer midpoint
        point1 = Dot(grid.c2p(2, 2), color=RED, radius=0.08)
        point2 = Dot(grid.c2p(3, 4), color=RED, radius=0.08)
        label1 = Text("(2,2)", font_size=20, color=RED).next_to(point1, UP, buff=0.1)
        label2 = Text("(3,4)", font_size=20, color=RED).next_to(point2, UP, buff=0.1)
        
        line1 = Line(point1.get_center(), point2.get_center(), color=RED)
        mid1 = Dot(grid.c2p(2.5, 3), color=WHITE, radius=0.08)
        mid_label1 = Text("(2.5, 3)", font_size=20, color=WHITE).next_to(mid1, DOWN, buff=0.1)
        
        # Show first example
        self.play(Create(point1), Create(point2))
        self.play(Write(label1), Write(label2))
        self.play(Create(line1))
        self.play(Create(mid1), Write(mid_label1))
        
        # Explanation for non-integer midpoint
        explanation1 = Text(
            "Midpoint coordinates are not integers",
            font_size=24,
            color=RED
        )
        explanation1.next_to(grid, DOWN, buff=0.5)
        self.play(Write(explanation1))
        self.wait(1)
        
        # Clear first example
        self.play(
            FadeOut(point1), FadeOut(point2),
            FadeOut(label1), FadeOut(label2),
            FadeOut(line1), FadeOut(mid1),
            FadeOut(mid_label1), FadeOut(explanation1)
        )
        
        # Example 2: Integer midpoint
        point3 = Dot(grid.c2p(2, 2), color=GREEN, radius=0.08)
        point4 = Dot(grid.c2p(4, 4), color=GREEN, radius=0.08)
        label3 = Text("(2,2)", font_size=20, color=GREEN).next_to(point3, UP, buff=0.1)
        label4 = Text("(4,4)", font_size=20, color=GREEN).next_to(point4, UP, buff=0.1)
        
        line2 = Line(point3.get_center(), point4.get_center(), color=GREEN)
        mid2 = Dot(grid.c2p(3, 3), color=WHITE, radius=0.08)
        mid_label2 = Text("(3, 3)", font_size=20, color=WHITE).next_to(mid2, DOWN, buff=0.1)
        
        # Show second example
        self.play(Create(point3), Create(point4))
        self.play(Write(label3), Write(label4))
        self.play(Create(line2))
        self.play(Create(mid2), Write(mid_label2))
        
        # Explanation for integer midpoint
        explanation2 = Text(
            "Midpoint coordinates are integers",
            font_size=24,
            color=GREEN
        )
        explanation2.next_to(grid, DOWN, buff=0.5)
        self.play(Write(explanation2))
        self.wait(1)
        
        # Final question
        question = Text(
            "Can this always be guaranteed?",
            font_size=36,
            color=YELLOW
        )
        question.next_to(explanation2, DOWN, buff=0.8)
        self.play(Write(question))
        self.wait(1)
        
        # Clear the scene
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(x_labels),
            FadeOut(y_labels),
            FadeOut(point3),
            FadeOut(point4),
            FadeOut(label3),
            FadeOut(label4),
            FadeOut(line2),
            FadeOut(mid2),
            FadeOut(mid_label2),
            FadeOut(explanation2),
            FadeOut(question)
        )
        
        # Think and Ponder message in center
        think_text = Text(
            "Think and Ponder...",
            font_size=48,
            color=BLUE
        )
        self.play(Write(think_text))
        self.wait(2)
        
        # Clear the final message
        self.play(FadeOut(think_text)) 