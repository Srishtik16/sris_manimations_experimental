from manim import *

class SummaryScene(Scene):
    def construct(self):
        # Title
        title = Text("Summary", color=BLUE, font_size=44)
        title.to_edge(UP, buff=0.5)
        
        # Create summary points
        points = VGroup(
            Text("• dp[i] = length of LIS ending at index i", font_size=32),
            Text("• For each i, check all j < i where arr[j] < arr[i]", font_size=32),
            Text("• Update: dp[i] = max(dp[i], dp[j] + 1)", font_size=32),
            Text("• Final answer: max(dp[])", font_size=32),
            Text("• Time Complexity: O(n²)", font_size=32, color=YELLOW)
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        points.next_to(title, DOWN, buff=1)
        # Create final prompt
        prompt = Text("Your turn to try!", 
                     color=GREEN, 
                     font_size=40)
        prompt.next_to(points, DOWN, buff=0.8)
        
        # Animations
        # 1. Show title
        self.play(Write(title))
        self.wait(0.5)
        
        # 2. Show points one by one
        for point in points:
            self.play(
                Write(point),
                run_time=1
            )
            self.wait(0.3)
        
        # 3. Show final prompt with bounce effect
        self.wait(1)
        
        # 4. Show final prompt with bounce effect
        self.play(
            GrowFromCenter(prompt),
            run_time=1
        )
        self.play(
            prompt.animate.scale(1.1),
            run_time=0.2
        )
        self.play(
            prompt.animate.scale(1/1.1),
            run_time=0.2
        )
        self.wait(1)
        
        # Store elements for future reference
        self.title = title
        self.points = points
        self.prompt = prompt 