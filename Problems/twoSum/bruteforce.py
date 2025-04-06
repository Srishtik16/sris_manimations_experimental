from manim import *
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from CustomArray import CreateArray

class BruteForceScene(Scene):
    def construct(self):
        # First Part: Brute Force Animation
        self.show_brute_force_animation()
        
        # Clean transition
        self.clear()
        self.wait(0.5)
        
        # Second Part: Code Display
        self.show_code_section()
    
    def show_brute_force_animation(self):
        # Title
        title = Text("Approach #1: Brute Force", font_size=40)
        title.to_edge(UP)
        
        # Complexity analysis
        complexity = Text("Time: O(n²)   Space: O(1)", font_size=28)
        complexity.next_to(title, DOWN, buff=0.5)
        
        # Create array visualization
        nums = [2, 7, 11, 15]
        target = 18
        
        # Create array using CreateArray scene
        array_creator = CreateArray(nums)
        array_group = VGroup()
        array_group.add(Rectangle(width=len(nums), height=1, color=WHITE))  # Index 0: Rectangle
        
        # Add dividing lines (Indices 1 to len(nums)-1)
        lines = VGroup()
        for i in range(len(nums) - 1):
            x_pos = -len(nums)/2 + (i + 1)
            line = Line(start=[x_pos, -0.5, 0], end=[x_pos, 0.5, 0], color=WHITE)
            lines.add(line)
        array_group.add(lines)
        
        # Add numbers (Index len(nums))
        numbers = VGroup()
        for i, num in enumerate(nums):
            x_pos = -len(nums)/2 + i + 0.5
            number = MathTex(r"\mathbf{" + str(num) + "}")
            number.move_to([x_pos, 0, 0])
            numbers.add(number)
        array_group.add(numbers)
        
        # Add indices (Index len(nums)+1)
        indices = VGroup()
        for i in range(len(nums)):
            x_pos = -len(nums)/2 + i + 0.5
            index = Text(str(i), font_size=24, color=BLUE)
            index.move_to([x_pos, -0.8, 0])
            indices.add(index)
        array_group.add(indices)
        
        # Position array in center of scene
        array_group.move_to(ORIGIN)
        array_group.shift(UP * 0.5)  # Slight shift up from center to make room below
        
        # Create three distinct vertical sections below array
        status_center = array_group.get_bottom() + DOWN * 1.5  # Section for status text
        check_center = status_center + DOWN * 1.5  # Section for target and current check (reduced from 2)
        result_center = check_center + DOWN * 1.5  # Section for success/return messages (reduced from 2)
        
        # Add explanation text in status section
        explanation = Text("Using two pointers i and j to check all possible pairs", font_size=28)
        explanation.move_to(status_center)
        
        # Create left and right areas in the check section
        left_check = check_center + LEFT * 4
        right_check = check_center + RIGHT * 4
        
        # Add target display on the left side with a heading
        target_heading = Text("Looking for:", font_size=24, color=WHITE)
        target_text = Text(f"Target = {target}", font_size=32, color=YELLOW)
        target_group = VGroup(target_heading, target_text).arrange(DOWN, buff=0.3)
        target_group.move_to(left_check)
        
        # Create a fixed position for sum text on the right side with a heading
        sum_heading = Text("Current check:", font_size=24, color=WHITE)
        sum_text = Text("Calculating...", font_size=32)
        sum_group = VGroup(sum_heading, sum_text).arrange(DOWN, buff=0.5)
        sum_group.move_to(right_check)
        
        # Store the position where sum text should appear
        sum_text_pos = sum_group[1].get_center()  # Store the exact position for sum text
        
        # Success messages will appear in the result section
        success_pos = result_center
        
        # Animations
        # 1. Show title and complexity
        self.play(Write(title))
        self.play(Write(complexity))
        self.wait(1)
        
        # 2. Create array visualization
        self.play(Create(array_group[0]))  # Rectangle
        self.play(Create(array_group[1]))  # Lines
        self.play(Create(array_group[2]))  # Numbers
        self.play(Create(array_group[3]))  # Indices
        self.wait(1)
        
        # Fade out title and complexity before showing pointers
        self.play(FadeOut(title), FadeOut(complexity))
        self.play(Write(explanation))
        self.wait(1)
        
        # 3. Show nested loop comparison
        i_pointer = Arrow(start=UP, end=DOWN, color=RED, max_tip_length_to_length_ratio=0.2)
        j_pointer = Arrow(start=UP, end=DOWN, color=GREEN, max_tip_length_to_length_ratio=0.2)
        
        i_label = Text("i", font_size=24, color=RED)
        j_label = Text("j", font_size=24, color=GREEN)
        
        # Initialize pointers above array
        first_cell_pos = array_group[0].get_corner(UL) + RIGHT * 0.5
        second_cell_pos = first_cell_pos + RIGHT
        
        i_pointer.next_to(first_cell_pos, UP, buff=0.2)
        j_pointer.next_to(second_cell_pos, UP, buff=0.2)
        i_label.next_to(i_pointer, UP, buff=0.1)
        j_label.next_to(j_pointer, UP, buff=0.1)
        
        # Create VGroups to keep pointers and labels together
        i_group = VGroup(i_pointer, i_label)
        j_group = VGroup(j_pointer, j_label)
        
        self.play(
            Create(i_group),
            Create(j_group)
        )
        
        # Fade out explanation and show target
        self.play(FadeOut(explanation))
        self.play(Write(target_group))
        
        self.play(Write(sum_heading))
        
        for i in range(len(nums)):
            # Highlight current i element
            i_number = array_group[2][i]  # Numbers are in the third VGroup
            self.play(i_number.animate.set_color(RED))
            
            for j in range(i + 1, len(nums)):
                # Calculate pointer positions
                i_pos = array_group[0].get_corner(UL) + RIGHT * (i + 0.5)
                j_pos = array_group[0].get_corner(UL) + RIGHT * (j + 0.5)
                
                # Move pointer groups together
                self.play(
                    i_group.animate.arrange(UP, buff=0.1).next_to(i_pos, UP, buff=0.2),
                    j_group.animate.arrange(UP, buff=0.1).next_to(j_pos, UP, buff=0.2),
                    run_time=0.5
                )
                
                # Highlight current j element
                j_number = array_group[2][j]  # Numbers are in the third VGroup
                self.play(j_number.animate.set_color(GREEN), run_time=0.3)
                
                # Show current sum on the right side
                current_sum = nums[i] + nums[j]
                new_sum_text = Text(f"{nums[i]} + {nums[j]} = {current_sum}", font_size=32)
                new_sum_text.move_to(sum_text_pos)  # Use stored position
                
                if current_sum == target:
                    new_sum_text.set_color(GREEN)
                    self.play(Transform(sum_text, new_sum_text))
                    
                    # Show success message in result section
                    success = Text("Found the solution!", font_size=32, color=GREEN)
                    success.move_to(result_center)
                    self.play(Write(success))
                    
                    # Show return value below success
                    return_text = Text(f"return [{i}, {j}]", font_size=32, color=GREEN)
                    return_text.next_to(success, DOWN, buff=0.5)
                    self.play(Write(return_text))
                    
                    self.wait(2)
                    
                    # Clean fade out
                    self.play(
                        *[FadeOut(mob) for mob in [
                            i_group, j_group,
                            target_group, sum_heading, sum_text, success, return_text
                        ]]
                    )
                    break
                else:
                    new_sum_text.set_color(RED)
                    self.play(Transform(sum_text, new_sum_text))
                    self.wait(0.3)
                    
                # Reset j number color if not the solution
                if current_sum != target:
                    self.play(j_number.animate.set_color(WHITE), run_time=0.3)
            
            # Reset i number color if no solution found with this i
            if i < len(nums) - 1:  # Don't reset color on the last iteration
                self.play(i_number.animate.set_color(WHITE), run_time=0.3)
        
        # Fade out array group last
        self.play(FadeOut(array_group))
    
    def show_code_section(self):
        # Title for code section
        title = Text("Implementation", font_size=40, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Show the complete implementation
        code = '''def twoSum(nums: List[int], target: int) -> List[int]:
    # Iterate through each element
    for i in range(len(nums)):
        # Check all elements after i
        for j in range(i + 1, len(nums)):
            # If pair sums to target, return indices
            if nums[i] + nums[j] == target:
                return [i, j]
    
    # No solution found
    return []'''
        
        code_text = Code(
            code_string=code,
            language="python",
            background="window",
        )
        code_text.next_to(title, DOWN, buff=0.5)
        
        # Add explanation text
        explanation = VGroup(
            Text("• Time Complexity: O(n²) - nested loops", font_size=24, color=GRAY),
            Text("• Space Complexity: O(1) - no extra space needed", font_size=24, color=GRAY),
            Text("• Simple but not optimal for large inputs", font_size=24, color=GRAY)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        explanation.next_to(code_text, DOWN, buff=0.5)
        
        # Animate code and explanation
        self.play(Write(code_text))
        self.wait(1)
        self.play(Write(explanation))
        self.wait(2) 