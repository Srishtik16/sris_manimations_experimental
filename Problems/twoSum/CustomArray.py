from manim import *
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class CreateArray:
    def __init__(self, nums):
        self.nums = nums
        self.array_group = VGroup()
        
        # Create rectangle
        self.array_group.add(Rectangle(width=len(nums), height=1, color=WHITE))
        
        # Add dividing lines
        lines = VGroup()
        for i in range(len(nums) - 1):
            x_pos = -len(nums)/2 + (i + 1)
            line = Line(start=[x_pos, -0.5, 0], end=[x_pos, 0.5, 0], color=WHITE)
            lines.add(line)
        self.array_group.add(lines)
        
        # Add numbers
        numbers = VGroup()
        for i, num in enumerate(nums):
            x_pos = -len(nums)/2 + i + 0.5
            number = MathTex(r"\mathbf{" + str(num) + "}")
            number.move_to([x_pos, 0, 0])
            numbers.add(number)
        self.array_group.add(numbers)
        
        # Add indices
        indices = VGroup()
        for i in range(len(nums)):
            x_pos = -len(nums)/2 + i + 0.5
            index = Text(str(i), font_size=24, color=BLUE)
            index.move_to([x_pos, -0.8, 0])
            indices.add(index)
        self.array_group.add(indices)
        
        # Position array in center
        self.array_group.move_to(ORIGIN)
        
    def get_array(self):
        return self.array_group 