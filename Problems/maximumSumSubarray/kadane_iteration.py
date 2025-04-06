from manim import *
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from CustomArray import CreateArray

class KadaneIterationScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # Default array if none provided
    
    def construct(self):
        # Title
        title = Text("Kadane's Algorithm - Iteration", font_size=40)
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
        start_idx = 0
        end_idx = 0
        temp_start = 0
        
        # Create variable displays
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
        
        # Create pointer arrow
        pointer = Arrow(
            start=UP,
            end=DOWN,
            color=BLUE,
            max_tip_length_to_length_ratio=0.2,
            stroke_width=3
        )
        pointer.next_to(array_group[2][0], UP, buff=0.3)  # Position at first number
        
        # Create decision box (moved higher and made wider)
        decision_box = Rectangle(
            width=6,  # Increased width
            height=2.5,  # Increased height
            color=WHITE,
            fill_opacity=0.1
        )
        decision_box.next_to(array_group, UP, buff=1.2)  # Increased buffer
        
        # Show initial setup
        self.play(
            Write(title),
            Create(array_group),
            Write(var_group),
            GrowArrow(pointer)
        )
        self.wait(1)
        
        # Fade out title to prevent overlap with decision box
        self.play(FadeOut(title))
        self.wait(0.5)
        
        # Keep track of current window highlight
        current_highlight = None
        best_highlight = None
        
        # Iterate through array starting from index 1
        for i in range(1, len(self.nums)):
            # Move pointer to current element
            new_pointer_x = -len(self.nums)/2 + i + 0.5
            self.play(
                pointer.animate.next_to(array_group[2][i], UP, buff=0.3),
                run_time=0.5
            )
            
            # Calculate options
            extend_sum = current_sum + self.nums[i]
            start_fresh = self.nums[i]
            
            # Show decision box with options
            decision_text = VGroup(
                Text("Options:", font_size=24, color=BLUE),
                Text(f"1. Extend current: {current_sum} + {self.nums[i]} = {extend_sum}", font_size=24),
                Text(f"2. Start fresh: {self.nums[i]}", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)  # Added buffer between lines
            decision_text.move_to(decision_box)
            
            self.play(
                Create(decision_box),
                Write(decision_text)
            )
            
            # Determine better option
            if extend_sum > start_fresh:
                choice_text = Text("→ Extending current subarray", color=GREEN, font_size=24)
                current_sum = extend_sum
                
                # Update current window highlight
                if current_highlight:
                    # Extend the current highlight
                    new_width = i - temp_start + 1
                    new_x = -len(self.nums)/2 + (temp_start + i)/2 + 0.5
                    new_highlight = Rectangle(
                        width=new_width,
                        height=1,
                        color=BLUE,
                        stroke_width=2,
                        fill_opacity=0.1
                    ).move_to([new_x, 0, 0])
                    self.play(Transform(current_highlight, new_highlight))
            else:
                choice_text = Text("→ Starting fresh", color=YELLOW, font_size=24)
                current_sum = start_fresh
                temp_start = i
                
                # Remove old highlight and create new one
                if current_highlight:
                    self.play(FadeOut(current_highlight))
                
                # Create new highlight for current window
                current_highlight = Rectangle(
                    width=1,
                    height=1,
                    color=BLUE,
                    stroke_width=2,
                    fill_opacity=0.1
                ).move_to([new_pointer_x, 0, 0])
                self.play(GrowFromCenter(current_highlight))
            
            choice_text.next_to(decision_text, DOWN, buff=0.3)  # Added buffer
            self.play(Write(choice_text))
            
            # Update current sum display
            new_current_sum = MathTex(str(current_sum), font_size=32, color=YELLOW)
            new_current_sum.move_to(current_sum_value)
            self.play(
                Transform(current_sum_value, new_current_sum)
            )
            
            # Check if we found a new maximum
            if current_sum > max_sum:
                max_sum = current_sum
                start_idx = temp_start
                end_idx = i
                
                # Update max sum display
                new_max_sum = MathTex(str(max_sum), font_size=32, color=YELLOW)
                new_max_sum.move_to(max_sum_value)
                
                # Create new highlight for best subarray
                if best_highlight:
                    self.play(FadeOut(best_highlight))
                
                highlight_width = end_idx - start_idx + 1
                highlight_x = -len(self.nums)/2 + (start_idx + end_idx)/2 + 0.5
                best_highlight = Rectangle(
                    width=highlight_width,
                    height=1,
                    color=YELLOW,
                    stroke_width=2,
                    fill_opacity=0.2
                ).move_to([highlight_x, 0, 0])
                
                # Show "New Max Found!" message
                new_max_text = Text("New Max Found!", color=GREEN, font_size=32)
                new_max_text.next_to(var_group, DOWN, buff=0.5)
                
                self.play(
                    Transform(max_sum_value, new_max_sum),
                    GrowFromCenter(best_highlight),
                    Write(new_max_text)
                )
                self.wait(0.5)
                self.play(FadeOut(new_max_text))
            
            # Clean up decision box
            self.play(
                FadeOut(decision_box),
                FadeOut(decision_text),
                FadeOut(choice_text)
            )
            self.wait(0.5)
        
        # Final state
        final_text = Text("Kadane's Algorithm Complete!", color=GREEN, font_size=32)
        final_text.next_to(var_group, DOWN, buff=0.5)
        self.play(Write(final_text))
        self.wait(2) 