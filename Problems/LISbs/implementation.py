from manim import *

class ImplementationScene(Scene):
    def construct(self):
        # Title
        title = Text("Implementation", font_size=36)
        subtitle = Text("Using Binary Search with bisect_left", font_size=24, color=BLUE)
        title.to_edge(UP, buff=0.3)
        subtitle.next_to(title, DOWN, buff=0.2)
        
        # Create the code
        code = '''from bisect import bisect_left

def longest_increasing_subsequence(nums):
    if not nums:
        return 0
        
    # Initialize dp array with first number
    dp = [nums[0]]
    
    # Process each number
    for num in nums[1:]:
        if num > dp[-1]:
            # Append if larger than all elements
            dp.append(num)
        else:
            # Find position to replace using binary search
            pos = bisect_left(dp, num)
            dp[pos] = num
            
    return len(dp)  # Length of LIS'''

        code_text = Code(
            code_string=code,
            tab_width=4,
            language="python"
        )
        
        # Position code slightly above center
        code_text.next_to(title, DOWN, buff=0.1)
        code_text.scale(0.6)
        
        # Initial animation
        self.play(
            Write(title),
            Write(subtitle)
        )
        self.wait(0.5)
        
        # Show code with line by line highlight
        self.play(Create(code_text.background))
        self.play(Write(code_text))
        self.wait(1.0)