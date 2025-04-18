from manim import *

class FinalAnswerScene(Scene):
    def construct(self):
        # Title
        title = Text("Finding LIS Length", font_size=36)
        subtitle = Text("Using length of dp[] array", font_size=24, color=BLUE)
        title.to_edge(UP, buff=0.3)
        subtitle.next_to(title, DOWN, buff=0.2)
        
        # Create final dp array
        dp_array = [1, 4, 5]  # Final state of dp array
        dp_label = Text("dp[]:", font_size=28)
        dp_squares = VGroup(*[
            Square(side_length=0.7).set_fill(color=BLUE_E, opacity=0.3) 
            for _ in dp_array
        ]).arrange(RIGHT, buff=0.1)
        dp_nums = VGroup(*[
            Text(str(n), font_size=22) for n in dp_array
        ])
        for num, square in zip(dp_nums, dp_squares):
            num.move_to(square)
        dp_group = VGroup(dp_squares, dp_nums)
        dp_row = VGroup(dp_label, dp_group).arrange(RIGHT, buff=0.5)
        
        # Position dp array
        dp_row.move_to(ORIGIN)
        dp_row.next_to(subtitle, DOWN, buff=1.0)
        
        # Initial animation
        self.play(
            Write(title),
            Write(subtitle)
        )
        self.wait(0.5)
        
        # Show dp array
        self.play(Write(dp_row))
        self.wait(0.5)
        
        # Highlight dp array
        highlight = SurroundingRectangle(dp_group, color=GREEN, buff=0.2)
        self.play(Create(highlight))
        self.wait(0.5)
        
        # Show length
        length_text = Text("Length of LIS = 3", font_size=32, color=GREEN)
        length_text.next_to(dp_row, DOWN, buff=1.0)
        self.play(Write(length_text))
        self.wait(1)
        
        # Important note about dp array
        note_title = Text("Important Note:", font_size=28, color=YELLOW)
        note_title.next_to(length_text, DOWN, buff=0.8)
        
        notes = VGroup(
            Text("• dp[] doesn't store the actual LIS", font_size=24),
            Text("• It only helps find the length efficiently", font_size=24),
            Text("• Each dp[i] stores smallest ending element", font_size=24),
            Text("  for a subsequence of length i+1", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        notes.next_to(note_title, DOWN, buff=0.4)
        
        self.play(Write(note_title))
        for note in notes:
            self.play(Write(note))
            self.wait(0.3)
        
        # Final emphasis
        final_box = SurroundingRectangle(length_text, color=YELLOW, buff=0.2)
        self.play(Create(final_box))
        self.wait(1) 