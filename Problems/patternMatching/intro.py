from manim import *

class IntroScene(Scene):
    def construct(self):
        # Title
        title = Text("Z-Algorithm – Efficient Pattern Matching", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # Problem Statement
        problem = Text("Find where pattern P occurs in string T", font_size=32, color=WHITE)
        problem.next_to(title, DOWN, buff=0.8)
        self.play(Write(problem))
        self.wait(1)

        # Example Strings
        p_label = Text("P = ", font_size=32, color=WHITE)
        p_text = Text('"abc"', font_size=32, color=YELLOW)
        p_group = VGroup(p_label, p_text).arrange(RIGHT, buff=0.2)
        
        t_label = Text("T = ", font_size=32, color=WHITE)
        t_text = Text('"xabcabcabcx"', font_size=32, color=YELLOW)
        t_group = VGroup(t_label, t_text).arrange(RIGHT, buff=0.2)
        
        s_label = Text("S = ", font_size=32, color=WHITE)
        s_text = Text('"abc$abcabcabcx"', font_size=32, color=YELLOW)
        s_group = VGroup(s_label, s_text).arrange(RIGHT, buff=0.2)
        
        # Arrange all groups vertically
        all_groups = VGroup(p_group, t_group, s_group)
        all_groups.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        all_groups.next_to(problem, DOWN, buff=1.0)
        
        # Animate each group
        self.play(Write(p_group))
        self.wait(0.5)
        self.play(Write(t_group))
        self.wait(0.5)
        self.play(Write(s_group))
        self.wait(1)

        # Explanation of combined string
        explanation = Text("We want all positions where Z[i] == len(P)", font_size=32, color=GREEN)
        explanation.next_to(all_groups, DOWN, buff=0.8)
        self.play(Write(explanation))
        
        # Highlight the combined string
        highlight = SurroundingRectangle(s_text, color=GREEN, buff=0.2)
        self.play(Create(highlight))
        self.wait(2)

        # Fade out the highlight
        self.play(FadeOut(highlight))
        self.wait(1) 