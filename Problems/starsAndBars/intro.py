from manim import *

class IntroScene(Scene):
    def construct(self):
        # Title
        title = Text("Stars and Bars", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(1)

        # Equation
        equation = MathTex(
            r"x_1 + x_2 + x_3 = 5, \quad x_i \geq 0",
            font_size=32
        )
        equation.next_to(title, DOWN, buff=0.5)
        self.play(Write(equation))
        self.wait(1)

        # Story text
        story1 = Text("You have 5 candies (stars)", font_size=28)
        story1.next_to(equation, DOWN, buff=0.5)
        self.play(Write(story1))
        self.wait(1)

        # Create stars (candies)
        stars = VGroup()
        for i in range(5):
            star = Star(color=YELLOW, fill_opacity=1, outer_radius=0.2)
            stars.add(star)
        stars.arrange(RIGHT, buff=0.3)
        stars.next_to(story1, DOWN, buff=0.5)
        self.play(Create(stars))
        self.wait(1)

        # Story text 2
        story2 = Text("You want to divide them between 3 friends (bars)", font_size=28)
        story2.next_to(stars, DOWN, buff=0.5)
        self.play(Write(story2))
        self.wait(1)

        # Create friend labels
        friends = VGroup()
        for i in range(3):
            friend = Text(f"Friend {i+1}", font_size=24)
            friends.add(friend)
        friends.arrange(RIGHT, buff=0.8)
        friends.next_to(story2, DOWN, buff=0.5)
        
        # Add variable labels below friends
        variables = VGroup()
        for i in range(3):
            var = MathTex(f"x_{i+1}", font_size=24)
            variables.add(var)
        variables.arrange(RIGHT, buff=0.8)
        variables.next_to(friends, DOWN, buff=0.3)
        
        # Align variables with friends
        for i in range(3):
            variables[i].move_to(friends[i].get_center() + DOWN * 0.3)

        self.play(
            Create(friends),
            Create(variables)
        )
        self.wait(2)

        # Final explanation
        explanation = Text(
            "Each solution represents a way to distribute the candies",
            font_size=24,
            color=YELLOW
        )
        explanation.next_to(variables, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(2) 