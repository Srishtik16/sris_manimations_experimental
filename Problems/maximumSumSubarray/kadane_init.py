from manim import *
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from CustomArray import CreateArray

class KadaneInitScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # Default array if none provided
    
    def construct(self):
        # Title
        title = Text("Kadane's Algorithm - Initialization", font_size=40)
        title.to_edge(UP)
        
        # Create array visualization
        array_creator = CreateArray(self.nums)
        array_group = VGroup()
        
        # Add main rectangle
        main_rect = Rectangle(width=len(self.nums), height=1, color=WHITE)
        array_group.add(main_rect)
        
        # Add dividing lines
        lines = VGroup()
        for i in range(len(self.nums) - 1):
            x_pos = -len(self.nums)/2 + (i + 1)
            line = Line(start=[x_pos, -0.5, 0], end=[x_pos, 0.5, 0], color=WHITE)
            lines.add(line)
        array_group.add(lines)
        
        # Add numbers with color based on sign
        numbers = VGroup()
        for i, num in enumerate(self.nums):
            x_pos = -len(self.nums)/2 + i + 0.5
            number = MathTex(r"\mathbf{" + str(num) + "}")
            if num > 0:
                number.set_color(GREEN)
            elif num < 0:
                number.set_color(RED)
            number.move_to([x_pos, 0, 0])
            numbers.add(number)
        array_group.add(numbers)
        
        # Add indices
        indices = VGroup()
        for i in range(len(self.nums)):
            x_pos = -len(self.nums)/2 + i + 0.5
            index = Text(str(i), font_size=24, color=BLUE)
            index.move_to([x_pos, -0.8, 0])
            indices.add(index)
        array_group.add(indices)
        
        # Position array in center
        array_group.move_to(ORIGIN)
        
        # Initialize Kadane's variables
        current_sum = self.nums[0]
        max_sum = self.nums[0]
        
        # Create variable displays
        var_group = VGroup()
        
        # Current Sum display
        current_sum_label = Text("Current Sum: ", font_size=32)
        current_sum_value = MathTex(str(current_sum), font_size=32, color=YELLOW)
        current_sum_group = VGroup(current_sum_label, current_sum_value).arrange(RIGHT)
        
        # Max Sum display
        max_sum_label = Text("Max Sum: ", font_size=32)
        max_sum_value = MathTex(str(max_sum), font_size=32, color=YELLOW)
        max_sum_group = VGroup(max_sum_label, max_sum_value).arrange(RIGHT)
        
        # Arrange variable displays
        var_group = VGroup(current_sum_group, max_sum_group).arrange(RIGHT, buff=1)
        var_group.next_to(array_group, DOWN, buff=1)
        
        # Create highlight for first element
        first_element_x = -len(self.nums)/2 + 0.5
        highlight = Rectangle(
            width=1,
            height=1,
            color=YELLOW,
            stroke_width=2,
            fill_opacity=0
        ).move_to([first_element_x, 0, 0])
        
        # Create explanation text
        explanation = Text(
            "Initialize both current_sum and max_sum with the first element",
            font_size=28,
            color=BLUE
        )
        explanation.next_to(var_group, DOWN, buff=0.5)
        
        # Animations
        # 1. Show title
        self.play(Write(title))
        self.wait(0.5)
        
        # 2. Show array
        self.play(
            Create(array_group[0]),  # Main rectangle
            Create(array_group[1]),  # Lines
            run_time=1
        )
        
        self.play(
            *[Write(num) for num in array_group[2]],  # Numbers
            run_time=1
        )
        
        self.play(Create(array_group[3]))  # Indices
        self.wait(1)
        
        # 3. Show explanation
        self.play(Write(explanation))
        self.wait(1)
        
        # 4. Highlight first element with growing effect
        self.play(GrowFromCenter(highlight))
        
        # 5. Show variable initializations with write effect
        self.play(
            Write(current_sum_group),
            Write(max_sum_group),
            run_time=1
        )
        
        # 6. Add pulsing effect to highlight
        self.play(
            highlight.animate.scale(1.1),
            rate_func=there_and_back,
            run_time=0.5
        )
        
        self.wait(2) 