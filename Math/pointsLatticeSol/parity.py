from manim import *

class ParityScene(Scene):
    def construct(self):
        # Title
        title = Text("Coordinate Parity Concept", font_size=36)
        title.to_edge(UP)
        
        # Midpoint formula
        formula = MathTex(
            r"M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)",
            font_size=36
        )
        formula.next_to(title, DOWN, buff=0.8)
        
        # Question
        question = Text(
            "When is this an integer?",
            font_size=28,
            color=YELLOW
        )
        question.next_to(formula, DOWN, buff=0.6)
        
        # Condition
        condition = MathTex(
            r"\text{If } x_1 + x_2 \text{ and } y_1 + y_2 \text{ are even}",
            r"\rightarrow \text{midpoint is integer}",
            font_size=28
        )
        condition.next_to(question, DOWN, buff=0.5)
        
        # Explanation
        explanation = Text(
            "This happens only when x's and y's have the same parity",
            font_size=24
        )
        explanation.next_to(condition, DOWN, buff=0.5)
        
        # Parity types
        parity_types = VGroup(
            MathTex(r"(even, even) \rightarrow (0,0)", font_size=24),
            MathTex(r"(even, odd) \rightarrow (0,1)", font_size=24),
            MathTex(r"(odd, even) \rightarrow (1,0)", font_size=24),
            MathTex(r"(odd, odd) \rightarrow (1,1)", font_size=24)
        )
        parity_types.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        parity_types.next_to(explanation, DOWN, buff=0.8)
        
        # Animations
        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(formula))
        self.wait(0.5)
        self.play(Write(question))
        self.wait(0.5)
        self.play(Write(condition))
        self.wait(0.5)
        self.play(Write(explanation))
        self.wait(0.5)
        
        # Animate parity types one by one
        for ptype in parity_types:
            self.play(Write(ptype))
            self.wait(0.3)
        
        self.wait(2)
        
        # Clear the scene
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(question),
            FadeOut(condition),
            FadeOut(explanation),
            FadeOut(parity_types)
        ) 