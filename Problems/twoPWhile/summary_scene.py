from manim import *

class SummaryScene(Scene):
    def construct(self):
        # Title
        title = Text("Summary: Longest Substring Without Repeating Characters", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # Final Result
        result_text = Text("Final Result:", font_size=32, color=WHITE)
        result_text.next_to(title, DOWN, buff=0.6)
        self.play(Write(result_text))

        # Example string and result
        example = Text('"abc"', font_size=32, color=YELLOW)
        max_len = Text("maxLen = 3", font_size=32, color=GREEN)
        example.next_to(result_text, DOWN, buff=0.3)
        max_len.next_to(example, DOWN, buff=0.2)
        self.play(Write(example))
        self.play(Write(max_len))
        self.wait(1)

        # Time Complexity
        complexity_title = Text("Time Complexity:", font_size=32, color=WHITE)
        complexity = Text("O(n)", font_size=32, color=GREEN)
        complexity_title.next_to(max_len, DOWN, buff=0.6)
        complexity.next_to(complexity_title, DOWN, buff=0.2)
        complexity.scale(0.8)
        self.play(Write(complexity_title))
        self.play(Write(complexity))
        self.wait(1)

        # Key Points
        key_points_title = Text("Key Points:", font_size=32, color=WHITE)
        key_points_title.next_to(complexity, DOWN, buff=0.5)
        key_points_title.scale(0.8)
        self.play(Write(key_points_title))

        points = [
            "• Sliding window technique with two pointers",
            "• Set to track unique characters",
            "• Expand window when no duplicates",
            "• Shrink window when duplicates found"
        ]

        key_points = VGroup(*[Text(point, font_size=28, color=WHITE) for point in points])
        key_points.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        key_points.next_to(key_points_title, DOWN, buff=0.15)
        key_points.scale(0.6)
        for point in key_points:
            self.play(Write(point))
            self.wait(0.3)

        self.wait(1)