from manim import *

class SummaryScene(Scene):
    def construct(self):
        # Title
        title = Text("Z-Algorithm: Key Takeaways", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # Key points
        points = [
            "1. Z[i] = length of prefix match starting at i",
            "2. [l, r] window optimizes comparison",
            "3. Time complexity: O(n)",
            "4. Pattern matching: P + $ + T → Z → check Z[i] == len(P)"
        ]

        # Create and animate points
        point_texts = []
        for point in points:
            text = Text(point, font_size=28, color=WHITE)
            point_texts.append(text)
        
        # Arrange points vertically with more spacing
        points_group = VGroup(*point_texts)
        points_group.arrange(DOWN, aligned_edge=LEFT, buff=0.8)
        points_group.next_to(title, DOWN, buff=1.0)
        
        # Animate points one by one
        for point in point_texts:
            self.play(Write(point))
            self.wait(0.5)

        # Clear previous content before showing complexity box
        self.play(
            FadeOut(title),
            FadeOut(points_group)
        )
        self.wait(0.5)

        # Time complexity explanation
        complexity_title = Text("Time Complexity", font_size=36, color=GREEN)
        complexity_title.to_edge(UP, buff=0.5)
        
        complexity_text = Text(
            "O(n) time complexity\n"
            "• Each character compared at most twice\n"
            "• Window optimization reduces comparisons",
            font_size=24,
            color=WHITE
        )
        
        # Create box based on text size
        complexity_box = Rectangle(
            width=complexity_text.width + 1.0,
            height=complexity_text.height + 0.5,
            color=GREEN,
            fill_opacity=0.2
        )
        complexity_box.next_to(complexity_title, DOWN, buff=1.0)
        complexity_text.move_to(complexity_box.get_center())
        
        self.play(
            Write(complexity_title),
            run_time=0.5
        )
        self.play(
            Create(complexity_box),
            Write(complexity_text),
            run_time=1.5
        )
        self.wait(1)

        # Clear previous content before showing pattern matching
        self.play(
            FadeOut(complexity_title),
            FadeOut(complexity_box),
            FadeOut(complexity_text)
        )
        self.wait(0.5)

        # Pattern matching summary
        pattern_title = Text("Pattern Matching", font_size=36, color=YELLOW)
        pattern_title.to_edge(UP, buff=0.5)
        
        pattern_text = Text(
            "Pattern Matching Steps:\n"
            "1. Create S = P + $ + T\n"
            "2. Compute Z-array\n"
            "3. Find i where Z[i] == len(P)",
            font_size=24,
            color=WHITE
        )
        
        # Create box based on text size
        pattern_box = Rectangle(
            width=pattern_text.width + 1.0,
            height=pattern_text.height + 0.5,
            color=YELLOW,
            fill_opacity=0.2
        )
        pattern_box.next_to(pattern_title, DOWN, buff=1.0)
        pattern_text.move_to(pattern_box.get_center())
        
        self.play(
            Write(pattern_title),
            run_time=0.5
        )
        self.play(
            Create(pattern_box),
            Write(pattern_text),
            run_time=1.5
        )
        self.wait(1)

        # Clear previous content before showing final call
        self.play(
            FadeOut(pattern_title),
            FadeOut(pattern_box),
            FadeOut(pattern_text)
        )
        self.wait(0.5)

        # Final call to action
        call_to_action = Text(
            "Try implementing it yourself!",
            font_size=32,
            color=YELLOW
        )
        call_to_action.move_to(ORIGIN)
        
        self.play(Write(call_to_action))
        
        # Bounce effect
        self.play(
            call_to_action.animate.scale(1.1),
            rate_func=there_and_back,
            run_time=1.5
        )
        
        self.wait(2) 