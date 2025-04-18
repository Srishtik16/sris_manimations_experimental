from manim import *

class PositiveCaseScene(Scene):
    def construct(self):
        # Frame 1: Question and Initial Setup
        title = Text("Positive vs Non-Negative Case", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(1)

        # Initial question
        question = Text(
            "What if each friend must get at least one candy?",
            font_size=28,
            color=YELLOW
        )
        question.next_to(title, DOWN, buff=0.5)
        self.play(Write(question))
        self.wait(1)

        # Initial stars
        initial_stars = VGroup()
        for i in range(5):
            star = Star(color=YELLOW, fill_opacity=1, outer_radius=0.2)
            initial_stars.add(star)
        initial_stars.arrange(RIGHT, buff=0.2)
        initial_stars.next_to(question, DOWN, buff=0.5)

        # Label for initial stars
        initial_label = Text("5 candies", font_size=24)
        initial_label.next_to(initial_stars, DOWN, buff=0.3)
        
        self.play(Create(initial_stars))
        self.play(Write(initial_label))
        self.wait(1)

        # Show giving one to each friend
        friends = VGroup()
        for i in range(3):
            friend = Text(f"Friend {i+1}", font_size=24)
            friends.add(friend)
        friends.arrange(RIGHT, buff=0.8)
        friends.next_to(initial_label, DOWN, buff=0.5)

        # Show one star for each friend
        friend_stars = VGroup()
        for i in range(3):
            star = Star(color=YELLOW, fill_opacity=1, outer_radius=0.2)
            friend_stars.add(star)
        friend_stars.arrange(RIGHT, buff=0.8)
        friend_stars.next_to(friends, DOWN, buff=0.3)

        self.play(
            Create(friends),
            Create(friend_stars)
        )
        self.wait(2)

        # Clear and move to Frame 2
        self.play(
            FadeOut(title),
            FadeOut(question),
            FadeOut(initial_stars),
            FadeOut(initial_label),
            FadeOut(friends),
            FadeOut(friend_stars)
        )
        self.wait(0.5)

        # Frame 2: Formula Derivation
        # Show the transformation
        transform_title = Text("Transformation to Non-Negative Case", font_size=32, color=BLUE)
        transform_title.to_edge(UP, buff=0.3)
        self.play(Write(transform_title))

        # Original equation
        orig_eq = MathTex(r"x_1 + x_2 + x_3 = 5", r"\text{ where } x_i \geq 1")
        orig_eq.next_to(transform_title, DOWN, buff=0.5)
        self.play(Write(orig_eq))
        self.wait(1)

        # Let y_i = x_i - 1
        let_eq = MathTex(r"Let\ y_i = x_i - 1\ \Rightarrow\ x_i = y_i + 1")
        let_eq.next_to(orig_eq, DOWN, buff=0.5)
        self.play(Write(let_eq))
        self.wait(1)

        # Substituted equation
        sub_eq = MathTex(r"(y_1 + 1) + (y_2 + 1) + (y_3 + 1) = 5")
        sub_eq.next_to(let_eq, DOWN, buff=0.5)
        self.play(Write(sub_eq))
        self.wait(1)

        # Simplified equation
        simp_eq = MathTex(r"y_1 + y_2 + y_3 = 2", r"\text{ where } y_i \geq 0")
        simp_eq.next_to(sub_eq, DOWN, buff=0.5)
        self.play(Write(simp_eq))
        self.wait(1)

        # Show the formula
        formula = MathTex(r"C(n - k + k - 1, k - 1) = C(n - 1, k - 1)")
        formula.next_to(simp_eq, DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(1)

        # Numerical example
        example = MathTex(r"C(5 - 1, 3 - 1) = C(4, 2) = 6")
        example.next_to(formula, DOWN, buff=0.5)
        self.play(Write(example))
        self.wait(2)

        # Clear and show visualization
        self.play(
            FadeOut(transform_title),
            FadeOut(orig_eq),
            FadeOut(let_eq),
            FadeOut(sub_eq),
            FadeOut(simp_eq),
            FadeOut(formula),
            FadeOut(example)
        )

        self.wait(1)