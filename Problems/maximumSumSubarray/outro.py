from manim import *

class OutroScene(Scene):
    def construct(self):
        # Create title
        title = Text("Key Takeaways", color=BLUE, font_size=40)
        title.to_edge(UP, buff=1)
        
        # Create summary points
        points = VGroup()
        
        point1 = Text("• Kadane's Algorithm maintains two sums:", font_size=28)
        point1_sub = VGroup(
            Text("   - Current Sum: tracks ongoing subarray", font_size=24, color=YELLOW),
            Text("   - Maximum Sum: keeps best result seen", font_size=24, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        point2 = Text("• At each step, makes a decision:", font_size=28)
        point2_sub = VGroup(
            Text("   - Continue with current subarray", font_size=24, color=BLUE),
            Text("   - Start fresh from current element", font_size=24, color=BLUE)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        point3 = Text("• Key features:", font_size=28)
        point3_sub = VGroup(
            Text("   - Linear time complexity O(n)", font_size=24, color=GRAY),
            Text("   - Constant space complexity O(1)", font_size=24, color=GRAY)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        points.add(point1, point1_sub, point2, point2_sub, point3, point3_sub)
        points.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        points.next_to(title, DOWN, buff=0.8)
        
        # Create takeaways group
        takeaways = VGroup(title, points)
        
        # Create encouraging message
        message = Text("Try implementing it yourself!", color=GREEN, font_size=36)
        message.move_to(ORIGIN)  # Center in the screen
        
        # Animation sequence
        self.play(
            Write(title)
        )
        self.wait(0.5)
        
        # Animate points one by one
        for point in points:
            self.play(
                Write(point)
            )
            self.wait(0.5)
        
        # Wait to read the takeaways
        self.wait(2)
        
        # Fade out takeaways and show message
        self.play(
            FadeOut(takeaways)
        )
        self.wait(0.5)
        
        self.play(
            Write(message)
        )
        self.wait(2) 