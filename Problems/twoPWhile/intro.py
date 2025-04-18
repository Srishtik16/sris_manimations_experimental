from manim import *
from CustomArray import CreateArray

class IntroScene(Scene):
    def construct(self):
        # Title
        title = Text("Longest Substring Without Repeating Characters", 
                    color=BLUE, 
                    font_size=44)
        title.to_edge(UP, buff=0.5)
        
        # Problem description
        description = VGroup(
            Text("Given a string s, find the length of the", font_size=28),
            Text("longest substring that contains", font_size=28),
            Text("no repeating characters.", font_size=28)
        ).arrange(DOWN, buff=0.2)
        description.next_to(title, DOWN, buff=0.5)
        
        input_array = ['a', 'b', 'c', 'a', 'b', 'c', 'b', 'b']
        array_vis = CreateArray(input_array)  # Increased font size
        
        # Position the array in the center
        array_vis.scale(0.8)
        array_vis.move_to(ORIGIN)
        array_vis.next_to(description, DOWN, buff=0.5)
        array_vis.shift(DOWN * 0.5)
        
        array_label = Text("Input String:", font_size=28, color=YELLOW)
        array_label.next_to(array_vis, LEFT, buff=0.5)
        
        # Input label
        input_label = Text("Input String:", font_size=28, color=YELLOW)
        input_label.next_to(array_vis, LEFT, buff=0.5)
        
        # Question prompt
        question = Text(
            "What's the longest substring without repeating characters?",
            font_size=32,
            color=GREEN
        )
        question.next_to(array_vis, DOWN, buff=1.0)
        
        # Animations
        # 1. Show title
        self.play(Write(title))
        self.wait(0.5)
        
        # 2. Show description line by line
        for line in description:
            self.play(AddTextLetterByLetter(line), run_time=1)
        self.wait(0.5)

        # 3. Show input array with label
        self.play(
            Write(array_label),
            array_vis.create_animation(),
            run_time=1.5
        )
        self.wait(0.5)
        
        # 4. Show question with typewriter effect
        self.play(AddTextLetterByLetter(question), run_time=2)
        self.wait(2) 