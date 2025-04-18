from manim import *

class CombinatoricsScene(Scene):
    def construct(self):
        # Title
        title = Text("Mapping to Combinatorics", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(1)

        # Total symbols explanation
        total_text = Text(
            "Total symbols = n stars + k - 1 bars",
            font_size=28
        )
        total_text.next_to(title, DOWN, buff=0.8)
        self.play(Write(total_text))
        self.wait(1)

        # Question
        question = Text(
            "How many unique ways can we place bars among these?",
            font_size=28,
            color=YELLOW
        )
        question.next_to(total_text, DOWN, buff=0.8)
        self.play(Write(question))
        self.wait(1)

        # Create slots visualization
        n = 5  # number of stars
        k = 3  # number of variables
        total_slots = n + k - 1

        # Create slots with stars and bars
        bars = [2, 4]
        slots = VGroup()
        for i in range(total_slots):
            if i != bars[0] and i != bars[1]:  # Place stars
                star = Star(color=YELLOW, fill_opacity=1, outer_radius=0.2)
                slots.add(star)
            else:  # Place bars
                bar = Text("|", font_size=36, color=WHITE)
                slots.add(bar)
        slots.arrange(RIGHT, buff=0.2)
        slots.next_to(question, DOWN, buff=0.8)
        
        # Add slot numbers
        numbers = VGroup()
        for i in range(total_slots):
            num = Text(str(i+1), font_size=20)
            num.next_to(slots[i], DOWN, buff=0.1)
            numbers.add(num)

        self.play(Create(slots))
        self.play(Create(numbers))
        self.wait(1)

        # Show choosing positions
        choose_text = Text(
            "Choose k-1 positions to place bars among (n + k - 1) total slots",
            font_size=24
        )
        choose_text.next_to(slots, DOWN, buff=0.8)
        self.play(Write(choose_text))
        self.wait(1)

        # Show example selection
        # Highlight two positions (for k=3, we need k-1=2 bars)
        selected_positions = [2, 4]  # example positions
        highlights = VGroup()
        for pos in selected_positions:
            highlight = SurroundingRectangle(slots[pos], color=YELLOW, buff=0.1)
            highlights.add(highlight)
        
        self.play(Create(highlights))
        self.wait(1)

        # Show formula
        formula = MathTex(
            r"\text{Ways} = C(n + k - 1, k - 1)",
            font_size=32,
            color=GREEN
        )
        formula.next_to(choose_text, DOWN, buff=0.8)
        
        # Add explanation
        explanation = MathTex(
            r"= C(5 + 3 - 1, 3 - 1) = C(7, 2) = 21",
            font_size=32,
            color=GREEN
        )
        explanation.next_to(formula, DOWN, buff=0.3)

        self.play(Write(formula))
        self.wait(1)
        self.play(Write(explanation))
        self.wait(2)

        # Final explanation
        final_text = Text(
            "This gives us all possible ways to distribute the stars",
            font_size=24,
            color=YELLOW
        )
        final_text.next_to(explanation, DOWN, buff=0.6)
        self.play(Write(final_text))
        self.wait(2) 