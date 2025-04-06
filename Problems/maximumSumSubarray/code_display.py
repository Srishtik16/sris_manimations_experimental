from manim import *

class CodeDisplayScene(Scene):
    def construct(self):
        # Create code text with syntax highlighting
        code = '''def kadanes_algorithm(nums):
    if not nums:
        return 0
        
    current_sum = max_sum = nums[0]
    start = end = temp_start = 0
    
    for i in range(1, len(nums)):
        # Decision: start fresh or extend
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]
            
        # Update maximum if needed
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
            
    return max_sum, nums[start:end+1]'''

        # Create code block with syntax highlighting
        code_block = Code(
            code_string=code,
            tab_width=4,
            background="window",
            language="python"
        )
        
        # Add title
        title = Text("Kadane's Algorithm Implementation", color=BLUE, font_size=36)
        
        # Create a group and arrange vertically
        group = VGroup(title, code_block)
        group.arrange(DOWN, buff=0.5)
        
        # Scale entire group to fit screen
        group.scale(0.7)
        
        # Move slightly up from center
        group.move_to(ORIGIN).shift(UP * 0.2)
        
        # Animation sequence
        self.play(
            Write(title)
        )
        self.wait(0.5)
        
        self.play(
            Create(code_block)
        )
        self.wait(3) 