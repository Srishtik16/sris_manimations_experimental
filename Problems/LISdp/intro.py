from manim import *
from CustomArray import CreateArray

class IntroScene(Scene):
    def construct(self):
        # Title
        title = Text("Longest Increasing Subsequence (DP)", color=BLUE, font_size=44)
        title.to_edge(UP, buff=0.5)
        
        # Problem description
        description = VGroup(
            Text("Given an array of numbers, find the length of the", font_size=28),
            Text("longest subsequence where each element is", font_size=28),
            Text("strictly greater than the previous element.", font_size=28)
        ).arrange(DOWN, buff=0.2)
        description.next_to(title, DOWN, buff=0.5)
        
        # Sample input array using CreateArray
        input_array = [10, 9, 2, 5, 3, 7, 101, 18]
        array_vis = CreateArray(input_array)  # Increased font size
        
        # Position the array in the center
        array_vis.scale(0.8)
        array_vis.move_to(ORIGIN)
        array_vis.next_to(description, DOWN, buff=0.5)
        array_vis.shift(DOWN * 0.5)
        
        array_label = Text("Input Array:", font_size=28, color=YELLOW)
        array_label.next_to(array_vis, LEFT, buff=0.5)
        
        # Question prompt
        question = Text(
            "What's the length of the longest increasing subsequence?",
            color=GREEN,
            font_size=32
        )
        question.next_to(array_vis, DOWN, buff=1.5)
        
        # Animations
        # 1. Fade in title with write effect
        self.play(Write(title))
        self.wait(0.5)
        
        # 2. Reveal description line by line
        for line in description:
            self.play(FadeIn(line, shift=UP*0.2))
            self.wait(0.3)
        
        # 3. Show input array with label
        self.play(
            Write(array_label),
            array_vis.create_animation(),
            run_time=1.5
        )
        self.wait(0.5)
        
        # 4. Pop up the question with grow effect
        self.play(
            GrowFromCenter(question),
            run_time=1
        )
        self.wait(1)
        
        # Store the elements for future reference
        self.title = title
        self.description = description
        self.array_vis = array_vis
        self.array_label = array_label
        self.question = question 