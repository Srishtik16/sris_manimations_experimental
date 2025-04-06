from manim import *
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from CustomArray import CreateArray

class VisualizationScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # Default array if none provided
    
    def construct(self):
        # Title
        title = Text("Maximum Subarray Visualization", font_size=40)
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
        
        # Find the maximum subarray (Kadane's algorithm)
        max_sum = float('-inf')
        curr_sum = 0
        start = 0
        end = 0
        temp_start = 0
        
        for i, num in enumerate(self.nums):
            curr_sum = max(num, curr_sum + num)
            if curr_sum == num:
                temp_start = i
            if curr_sum > max_sum:
                max_sum = curr_sum
                start = temp_start
                end = i
        
        # Create highlight rectangle for maximum subarray
        highlight_width = end - start + 1
        highlight_x = -len(self.nums)/2 + (start + end)/2 + 0.5
        highlight = Rectangle(
            width=highlight_width,
            height=1,  # Match the height of the main rectangle
            color=YELLOW,
            stroke_width=2,  # Reduced stroke width
            fill_opacity=0.2
        ).move_to([highlight_x, 0, 0])  # Exact same y-position as main rectangle
        
        # Sum display
        sum_text = Text(f"Maximum Sum: {max_sum}", font_size=36, color=YELLOW)
        sum_text.next_to(array_group, DOWN, buff=1)
        
        # Animations
        # 1. Show title
        self.play(Write(title))
        self.wait(0.5)
        
        # 2. Create array visualization with fade-in effect
        self.play(
            Create(array_group[0]),  # Main rectangle
            Create(array_group[1]),  # Lines
            run_time=1
        )
        
        # 3. Show numbers with fade in effect
        self.play(
            *[Write(num) for num in array_group[2]],  # Numbers
            run_time=1
        )
        
        # 4. Show indices
        self.play(Create(array_group[3]))  # Indices
        self.wait(1)
        
        # 5. Highlight maximum subarray with a growing effect
        self.play(
            GrowFromCenter(highlight),
            Write(sum_text),
            run_time=1.5
        )
        
        # 6. Add pulsing effect to highlight
        self.play(
            highlight.animate.scale(1.1).set_opacity(0.3),  # Slightly increase opacity during pulse
            rate_func=there_and_back,
            run_time=0.5
        )
        self.play(
            highlight.animate.scale(1.05).set_opacity(0.25),  # Slightly increase opacity during pulse
            rate_func=there_and_back,
            run_time=0.3
        )
        
        self.wait(2) 