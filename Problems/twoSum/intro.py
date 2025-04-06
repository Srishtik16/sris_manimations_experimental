from manim import *
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from CustomArray import CreateArray

class IntroScene(Scene):
    def construct(self):
        # Title
        title = Text("LeetCode #1 - Two Sum", font_size=48)
        title.to_edge(UP)
        
        # Problem statement
        problem_text = """Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution."""
        
        problem = Text(problem_text, font_size=24, line_spacing=0.5)
        problem.next_to(title, DOWN, buff=1)
        
        # Input example
        input_array = Text("nums = [2, 7, 11, 15]", font_size=32, color=BLUE)
        target_text = Text("target = 9", font_size=32, color=GREEN)
        
        input_group = VGroup(input_array, target_text).arrange(RIGHT, buff=1)
        input_group.next_to(problem, DOWN, buff=1)
        
        # Question
        question = Text("Which two numbers add up to 9?", font_size=36, color=YELLOW)
        question.next_to(input_group, DOWN, buff=1)
        
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
            run_time=3
        )
        self.wait(1)
        
        # 3. Slide in input array and target
        input_group.shift(RIGHT * 7)  # Move off screen first
        self.add(input_group)
        
        self.play(
            input_group.animate.shift(LEFT * 7),
            run_time=1.5,
            rate_func=smooth
        )
        self.wait(1)
        
        # 4. Circle around array and highlight target
        array_box = SurroundingRectangle(input_array, color=BLUE, buff=0.2)
        target_box = SurroundingRectangle(target_text, color=GREEN, buff=0.2)
        
        self.play(
            Create(array_box),
            Create(target_box)
        )
        self.wait(1)
        
        # 5. Pop in the question with bounce effect
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