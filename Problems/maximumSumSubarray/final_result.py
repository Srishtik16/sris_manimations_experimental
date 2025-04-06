from manim import *
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from CustomArray import CreateArray

class FinalResultScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.max_sum = 6
        self.start_idx = 3
        self.end_idx = 6
    
    def construct(self):
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
        
        # Create green highlight for maximum subarray
        highlight_width = self.end_idx - self.start_idx + 1
        highlight_x = -len(self.nums)/2 + (self.start_idx + self.end_idx)/2 + 0.5
        max_highlight = Rectangle(
            width=highlight_width,
            height=1,
            color="#00FF00",  # Bright green
            stroke_width=2,
            fill_opacity=0.2
        ).move_to([highlight_x, 0, 0])
        
        # Create result text
        result_title = Text("Maximum Subarray Found!", color=GREEN, font_size=40)
        result_title.to_edge(UP, buff=0.5)
        
        # Create max sum display
        max_sum_text = Text(f"Maximum Sum: {self.max_sum}", font_size=36, color=YELLOW)
        max_sum_text.next_to(array_group, DOWN, buff=0.8)
        
        # Create subarray display
        subarray = self.nums[self.start_idx:self.end_idx + 1]
        subarray_text = Text(f"Subarray: {subarray}", font_size=28, color=BLUE)
        subarray_text.next_to(max_sum_text, DOWN, buff=0.5)
        
        # Create time complexity tag
        complexity_tag = VGroup()
        time_complexity = Text("Time Complexity: O(n)", font_size=24, color=GRAY)
        space_complexity = Text("Space Complexity: O(1)", font_size=24, color=GRAY)
        complexity_tag.add(time_complexity, space_complexity)
        complexity_tag.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        complexity_tag.to_edge(DR, buff=0.5)
        
        # Animation sequence
        self.play(
            Create(array_group)
        )
        self.wait(0.5)
        
        self.play(
            Write(result_title)
        )
        self.wait(0.5)
        
        self.play(
            GrowFromCenter(max_highlight)
        )
        self.wait(0.5)
        
        self.play(
            Write(max_sum_text)
        )
        self.wait(0.5)
        
        self.play(
            Write(subarray_text)
        )
        self.wait(0.5)
        
        self.play(
            Write(complexity_tag)
        )
        self.wait(2) 