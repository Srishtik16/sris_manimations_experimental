from manim import *

class IntroScene(Scene):
    def construct(self):
        # Title
        title = Text("Midpoints in a Lattice Grid – What's Guaranteed?", font_size=36)
        title.to_edge(UP)
        
        # Problem statement parts with highlighted keywords
        problem_parts = [
            VGroup(
                Text("Suppose you pick any ", font_size=24),
                Text("5 points", font_size=24, color=YELLOW)
            ).arrange(RIGHT, buff=0.1),
            
            VGroup(
                Text("with ", font_size=24),
                Text("integer coordinates", font_size=24, color=GREEN),
                Text(" in the plane", font_size=24)
            ).arrange(RIGHT, buff=0.1),
            
            VGroup(
                Text("such that each coordinate is ", font_size=24),
                Text("between 1 and 8", font_size=24, color=BLUE),
                Text(" (inclusive).", font_size=24)
            ).arrange(RIGHT, buff=0.1),
            
            Text("Prove that there must exist two points", font_size=24),
            
            VGroup(
                Text("such that the ", font_size=24),
                Text("midpoint", font_size=24, color=RED),
                Text(" of the segment joining them", font_size=24)
            ).arrange(RIGHT, buff=0.1),
            
            Text("also has integer coordinates.", font_size=24)
        ]
        
        # Arrange problem texts vertically with more spacing
        problem_texts = VGroup(*problem_parts)
        problem_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        problem_texts.next_to(title, DOWN, buff=0.8)
        
        # Animations
        self.play(Write(title))
        self.wait(0.5)
        
        # Animate each part of the problem statement
        for text in problem_texts:
            self.play(Write(text))
            self.wait(0.3)
        
        self.wait(2)
        
        # Clear the scene
        self.play(
            FadeOut(title),
            FadeOut(problem_texts)
        ) 