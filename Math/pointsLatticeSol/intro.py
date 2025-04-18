from manim import *

class SolutionIntroScene(Scene):
    def construct(self):
        # Title
        title = Text("Integer Midpoint Proof – 5 Points on 8×8 Grid", font_size=36)
        title.to_edge(UP)
        
        # Problem recap
        recap = Text(
            "Pick any 5 lattice points with x, y ∈ [1, 8]",
            font_size=24
        )
        recap.next_to(title, DOWN, buff=2.0)
        
        # Question prompt
        question = Text(
            "Is there always a pair whose midpoint has integer coordinates?",
            font_size=28,
            color=YELLOW
        )
        question.next_to(recap, DOWN, buff=1.5)
        
        # Animations
        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(recap))
        self.wait(0.5)
        self.play(Write(question))
        self.wait(2)
        
        # Clear the scene
        self.play(
            FadeOut(title),
            FadeOut(recap),
            FadeOut(question)
        ) 