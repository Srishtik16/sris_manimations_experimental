from manim import *

class SummaryScene(Scene):
    def construct(self):
        # Title
        title = Text("Fenwick Tree Summary", color=BLUE, font_size=36)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title))
        self.wait(0.5)
        
        # Create summary table
        table = VGroup()
        
        # Headers
        headers = VGroup(
            Text("Operation", color=YELLOW, font_size=28),
            Text("Function", color=YELLOW, font_size=28),
            Text("Purpose", color=YELLOW, font_size=28)
        ).arrange(RIGHT, buff=1.0)
        headers.next_to(title, DOWN, buff=0.8)
        
        # Update row
        update_row = VGroup(
            Text("Update", color=BLUE, font_size=24),
            Text("add(i, delta)", color=WHITE, font_size=24),
            Text("Update BIT at index i", color=WHITE, font_size=24)
        ).arrange(RIGHT, buff=1.0)
        update_row.next_to(headers, DOWN, buff=0.4)
        
        # Query row
        query_row = VGroup(
            Text("Query", color=RED, font_size=24),
            Text("prefix_sum(r)", color=WHITE, font_size=24),
            Text("Get sum from 0 to r", color=WHITE, font_size=24)
        ).arrange(RIGHT, buff=1.0)
        query_row.next_to(update_row, DOWN, buff=0.4)
        
        # Add all elements to table
        table.add(headers, update_row, query_row)
        
        # Animate table
        self.play(Write(headers))
        self.wait(0.3)
        self.play(Write(update_row))
        self.wait(0.3)
        self.play(Write(query_row))
        self.wait(0.5)
        
        # Time complexity
        complexity = Text("Time Complexity: O(log n)", color=GREEN, font_size=32)
        complexity.next_to(table, DOWN, buff=0.8)
        
        self.play(Write(complexity))
        self.wait(0.5)
        
        # Final thoughts
        final_thoughts = VGroup(
            Text("A powerful tool for:", color=YELLOW, font_size=28),
            Text("• Prefix sums", color=WHITE, font_size=24),
            Text("• Range queries", color=WHITE, font_size=24),
            Text("• Dynamic updates", color=WHITE, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        final_thoughts.next_to(complexity, DOWN, buff=0.8)
        
        self.play(Write(final_thoughts))
        self.wait(1)
        
        # Coding encouragement
        coding_text = Text("Try implementing it yourself!", color=BLUE, font_size=28)
        coding_text.next_to(final_thoughts, DOWN, buff=0.8)
        
        self.play(Write(coding_text))
        self.wait(1)
        
        # Outro
        outro = Text("Follow for more algorithms!", color=YELLOW, font_size=36)
        outro.next_to(coding_text, DOWN, buff=1.0)
        
        self.play(Write(outro))
        self.wait(2)
        
        # Fade out everything
        self.play(FadeOut(VGroup(
            title, table, complexity,
            final_thoughts, coding_text, outro
        )))
        self.wait(0.5) 