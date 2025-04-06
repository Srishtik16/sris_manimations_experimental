from manim import *
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from CustomArray import CreateArray

class OptimalScene(Scene):
    def construct(self):
        # Title
        title = Text("Approach #2: Two Pointers (Optimal)", font_size=40)
        title.to_edge(UP)
        
        # Complexity analysis
        complexity = Text("Time: O(n)   Space: O(1)", font_size=28)
        complexity.next_to(title, DOWN, buff=0.5)
        
        # Create sorted array visualization
        nums = [2, 7, 11, 15]  # Already sorted
        target = 18
        
        # Create array using CreateArray scene
        array_creator = CreateArray(nums)
        array_group = VGroup()
        array_group.add(Rectangle(width=len(nums), height=1, color=WHITE))  # Index 0: Rectangle
        
        # Add dividing lines
        lines = VGroup()
        for i in range(len(nums) - 1):
            x_pos = -len(nums)/2 + (i + 1)
            line = Line(start=[x_pos, -0.5, 0], end=[x_pos, 0.5, 0], color=WHITE)
            lines.add(line)
        array_group.add(lines)
        
        # Add numbers
        numbers = VGroup()
        for i, num in enumerate(nums):
            x_pos = -len(nums)/2 + i + 0.5
            number = MathTex(r"\mathbf{" + str(num) + "}")
            number.move_to([x_pos, 0, 0])
            numbers.add(number)
        array_group.add(numbers)
        
        # Add indices
        indices = VGroup()
        for i in range(len(nums)):
            x_pos = -len(nums)/2 + i + 0.5
            index = Text(str(i), font_size=24, color=BLUE)
            index.move_to([x_pos, -0.8, 0])
            indices.add(index)
        array_group.add(indices)
        
        # Position array in center
        array_group.move_to(ORIGIN)
        array_group.shift(UP * 0.5)
        
        # Create status areas
        status_center = array_group.get_bottom() + DOWN * 1.5
        check_center = status_center + DOWN * 1.5
        result_center = check_center + DOWN * 1.5
        
        # Show initial explanation
        self.play(Write(title))
        self.play(Write(complexity))
        self.wait(1)
        
        # Create array visualization
        self.play(Create(array_group[0]))  # Rectangle
        self.play(Create(array_group[1]))  # Lines
        self.play(Create(array_group[2]))  # Numbers
        self.play(Create(array_group[3]))  # Indices
        self.wait(1)
        
        # Fade out title before continuing to avoid overlap
        self.play(FadeOut(title))
        
        # Add explanation text
        explanation = Text("Using two pointers from both ends moving inward", font_size=28)
        explanation.move_to(status_center)
        
        # Fade out complexity and show explanation
        self.play(FadeOut(complexity))
        self.play(Write(explanation))
        self.wait(1)
        
        # Create left and right pointers
        left_pointer = Arrow(start=UP, end=DOWN, color=RED, max_tip_length_to_length_ratio=0.2)
        right_pointer = Arrow(start=UP, end=DOWN, color=GREEN, max_tip_length_to_length_ratio=0.2)
        
        left_label = Text("left", font_size=24, color=RED)
        right_label = Text("right", font_size=24, color=GREEN)
        
        # Initialize pointer positions
        left_pos = array_group[0].get_corner(UL) + RIGHT * 0.5
        right_pos = array_group[0].get_corner(UR) + LEFT * 0.5
        
        left_pointer.next_to(left_pos, UP, buff=0.2)
        right_pointer.next_to(right_pos, UP, buff=0.2)
        left_label.next_to(left_pointer, UP, buff=0.1)
        right_label.next_to(right_pointer, UP, buff=0.1)
        
        self.play(
            Create(left_pointer),
            Create(right_pointer),
            Write(left_label),
            Write(right_label)
        )
        
        # Create left and right check areas
        left_check = check_center + LEFT * 4
        right_check = check_center + RIGHT * 4
        
        # Add target display
        target_heading = Text("Looking for:", font_size=24, color=WHITE)
        target_text = Text(f"Target = {target}", font_size=32, color=YELLOW)
        target_group = VGroup(target_heading, target_text).arrange(DOWN, buff=0.5)
        target_group.move_to(left_check)
        
        # Create sum check area
        sum_heading = Text("Current check:", font_size=24, color=WHITE)
        sum_text = Text("calculating...", font_size=32)  # Initialize with non-empty string
        sum_group = VGroup(sum_heading, sum_text).arrange(DOWN, buff=0.5)
        sum_group.move_to(right_check)
        
        # Show target and sum headings
        self.play(FadeOut(explanation))
        self.play(Write(target_group))
        self.play(Write(sum_heading))
        
        # Store sum text position
        sum_text_pos = sum_group[1].get_center()
        
        # Two pointer algorithm animation
        left = 0
        right = len(nums) - 1
        
        while left < right:
            # Move pointers
            left_pos = array_group[0].get_corner(UL) + RIGHT * (left + 0.5)
            right_pos = array_group[0].get_corner(UL) + RIGHT * (right + 0.5)
            
            # Create animations for pointer and label movements
            pointer_animations = [
                left_pointer.animate.next_to(left_pos, UP, buff=0.2),
                right_pointer.animate.next_to(right_pos, UP, buff=0.2)
            ]
            
            # Update label positions after pointer movement
            self.play(*pointer_animations, run_time=0.5)
            self.play(
                left_label.animate.next_to(left_pointer, UP, buff=0.1),
                right_label.animate.next_to(right_pointer, UP, buff=0.1),
                run_time=0.3
            )
            
            # Highlight current elements
            left_number = array_group[2][left]
            right_number = array_group[2][right]
            self.play(
                left_number.animate.set_color(RED),
                right_number.animate.set_color(GREEN),
                run_time=0.3
            )
            
            # Calculate and show sum
            current_sum = nums[left] + nums[right]
            new_sum_text = Text(f"{nums[left]} + {nums[right]} = {current_sum}", font_size=32)
            new_sum_text.move_to(sum_text_pos)
            
            if current_sum == target:
                new_sum_text.set_color(GREEN)
                self.play(Transform(sum_text, new_sum_text))
                
                # Show success message
                success = Text("Found the solution!", font_size=32, color=GREEN)
                success.move_to(result_center)
                self.play(Write(success))
                
                # Show return value
                return_text = Text(f"return [{left}, {right}]", font_size=32, color=GREEN)
                return_text.next_to(success, DOWN, buff=0.5)
                self.play(Write(return_text))
                
                self.wait(2)
                break
                
            elif current_sum < target:
                new_sum_text.set_color(RED)
                self.play(Transform(sum_text, new_sum_text))
                
                # Add explanation for moving left pointer with mathematical comparison
                comparison = Text(f"{current_sum} < {target}", font_size=28, color=RED)
                comparison.move_to(result_center + UP * 1.2)  # Increased vertical spacing
                move_text = Text("Sum too small, move left pointer right", font_size=24, color=RED)
                move_text.move_to(result_center + DOWN * 0.2)  # Adjusted position
                self.play(Write(comparison))
                self.play(Write(move_text))
                self.wait(1)
                self.play(FadeOut(comparison), FadeOut(move_text))
                
                # Reset colors and move left pointer
                self.play(
                    left_number.animate.set_color(WHITE),
                    right_number.animate.set_color(WHITE),
                    FadeOut(sum_text)
                )
                left += 1
                
            else:  # current_sum > target
                new_sum_text.set_color(RED)
                self.play(Transform(sum_text, new_sum_text))
                
                # Add explanation for moving right pointer with mathematical comparison
                comparison = Text(f"{current_sum} > {target}", font_size=28, color=RED)
                comparison.move_to(result_center + UP * 1.2)  # Increased vertical spacing
                move_text = Text("Sum too large, move right pointer left", font_size=24, color=RED)
                move_text.move_to(result_center + DOWN * 0.2)  # Adjusted position
                self.play(Write(comparison))
                self.play(Write(move_text))
                self.wait(1)
                self.play(FadeOut(comparison), FadeOut(move_text))
                
                # Reset colors and move right pointer
                self.play(
                    left_number.animate.set_color(WHITE),
                    right_number.animate.set_color(WHITE),
                    FadeOut(sum_text)
                )
                right -= 1
            
            sum_text = Text("calculating...", font_size=32)
            sum_text.move_to(sum_text_pos)
        
        # Clean fade out (title already faded out)
        self.play(
            *[FadeOut(mob) for mob in [
                left_pointer, right_pointer,
                left_label, right_label, target_group,
                sum_heading, sum_text
            ]]
        )
        
        # Fade out array group
        self.play(FadeOut(array_group))
        
        # Show the code implementation
        code = '''def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left + 1, right + 1]  # 1-indexed array
        elif curr_sum < target:
            left += 1
        else:
            right -= 1'''
            
        code_text = Code(
            code_string=code,
            tab_width=4,
            background="window",
            language="python",
        )
        code_text.to_edge(DOWN, buff=0.5)
        
        # Add a heading for the code
        code_heading = Text("Implementation", font_size=36)
        code_heading.next_to(code_text, UP, buff=0.5)
        
        # Show code with typing animation
        self.play(Write(code_heading))
        self.play(Write(code_text))
        self.wait(3)
        
        # Final fadeout
        self.play(
            FadeOut(code_heading),
            FadeOut(code_text)
        )
        self.wait(0.5) 