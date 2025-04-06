from manim import *
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from CustomArray import CreateArray

class IntroScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # Default array if none provided
    
    def construct(self):
        # Title
        title = Text("Kadane's Algorithm – Maximum Subarray", font_size=48)
        title.to_edge(UP)
        
        # Problem statement
        problem_text = """Find the contiguous subarray with the maximum sum."""
        
        problem = Text(problem_text, font_size=32, line_spacing=1.2)
        problem.next_to(title, DOWN, buff=1)
        
        # Create array visualization
        array_creator = CreateArray(self.nums)
        array_group = VGroup()
        array_group.add(Rectangle(width=len(self.nums), height=1, color=WHITE))  # Index 0: Rectangle
        
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
        
        # Question
        question = Text("What subarray has the largest sum?", font_size=36, color=YELLOW)
        question.next_to(array_group, DOWN, buff=1)
        
        # Animations
        # 1. Fade in title with a slight zoom effect
        self.play(
            Write(title, run_time=2),
            title.animate.scale(1.1),
        )
        self.wait(1)
        
        # 2. Transform into problem statement
        self.play(
            Write(problem),
            run_time=2
        )
        self.wait(1)
        
        # 3. Create array visualization with numbers appearing one by one
        self.play(Create(array_group[0]))  # Rectangle
        self.play(Create(array_group[1]))  # Lines
        
        # Animate numbers appearing one by one with a wave effect
        for number in array_group[2]:  # Numbers
            self.play(
                Write(number),
                run_time=0.3
            )
        
        self.play(Create(array_group[3]))  # Indices
        self.wait(1)
        
        # 4. Pop in the question with bounce effect
        self.play(
            Write(question),
            run_time=1
        )
        
        # Create bouncy effect using multiple scales
        self.play(
            question.animate.scale(1.2),
            rate_func=there_and_back,
            run_time=0.5
        )
        self.play(
            question.animate.scale(1.1),
            rate_func=there_and_back,
            run_time=0.3
        )
        self.play(
            question.animate.scale(1.05),
            rate_func=there_and_back,
            run_time=0.2
        )
        
        self.wait(2)
        
        # Optional: Add a fade out for smooth transition to next scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        ) 