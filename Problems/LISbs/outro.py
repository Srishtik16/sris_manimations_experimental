from manim import *

class OutroScene(Scene):
    def construct(self):
        # Title
        title = Text("Summary", font_size=36)
        title.to_edge(UP, buff=0.3)
        
        # Create summary points
        summary = VGroup(
            Text("Key Points:", font_size=28, color=BLUE),
            Text("• Maintain dp[] of smallest ending elements", font_size=24),
            Text("• If number > dp[-1]: append to dp[]", font_size=24),
            Text("• Else: replace first element ≥ number", font_size=24),
            Text("• Use binary search (bisect_left) to find position", font_size=24),
            Text("• Length of dp[] = Length of LIS", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        summary.next_to(title, DOWN, buff=0.8)
        
        # Create complexity box
        complexity = VGroup(
            Text("Time Complexity:", font_size=28, color=YELLOW),
            Text("O(n log n)", font_size=32, color=GREEN)
        ).arrange(RIGHT, buff=0.5)
        complexity.next_to(summary, DOWN, buff=0.8)
        
        # Create complexity explanation
        complexity_explain = VGroup(
            Text("• n iterations × log n (binary search)", font_size=24),
            Text("• Much faster than O(n²) approach!", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        complexity_explain.next_to(complexity, DOWN, buff=0.4)
        
        # Create final prompt
        prompt = Text("Now it's your turn to implement!", font_size=32, color=BLUE)
        prompt.next_to(complexity_explain, DOWN, buff=1.0)
        
        # Animations
        # Show title
        self.play(Write(title))
        self.wait(0.5)
        
        # Show summary points one by one
        for point in summary:
            self.play(Write(point))
            self.wait(0.3)
        
        # Show complexity
        self.play(
            Write(complexity[0]),
            Write(complexity[1])
        )
        self.wait(0.5)
        
        # Show complexity explanation
        for line in complexity_explain:
            self.play(Write(line))
            self.wait(0.3)
        
        # Show final prompt with bounce effect
        self.play(Write(prompt))
        self.play(
            prompt.animate.scale(1.1),
            rate_func=there_and_back
        )
        self.wait(1) 