from manim import *

class CodeRevealScene(Scene):
    def construct(self):
        # Title
        title = Text("Implementation", color=BLUE, font_size=36)
        title.to_edge(UP, buff=0.3)
        
        # Create the complete code
        code = '''def longest_increasing_subsequence(arr):
    n = len(arr)
    # Initialize dp array with 1s
    dp = [1] * n
    
    # Compute LIS values for all indexes
    for i in range(n):
        # Check all previous elements
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum value in dp[]
    return max(dp)

# Example usage
arr = [3, 1, 4, 2, 5]
result = longest_increasing_subsequence(arr)
print(f"Length of LIS is {result}")  # Output: 3'''

        code_text = Code(
            code_string=code,
            tab_width=4,
            language="python"
        )
        code_text.scale(0.8)
        
        # Position code on the left side
        code_text.to_edge(LEFT, buff=0.5)
        code_text.next_to(title, DOWN, buff=0.4)
        
        # Animations
        # 1. Show title
        self.play(Write(title))
        self.wait(0.5)
        
        # 2. Reveal code
        self.play(Write(code_text))
        self.wait(1.5)
        
        # Store elements for future reference
        self.title = title
        self.code_text = code_text
