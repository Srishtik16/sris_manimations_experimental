from manim import *
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from CustomArray import CreateArray

class SummaryScene(Scene):
    def construct(self):
        # Create title
        title = Text("Approach Comparison", font_size=40)
        title.to_edge(UP, buff=0.7)  # Reduced top buffer

        # Create table with consistent spacing
        table_data = [
            ["Time Complexity", "O(n²)", "O(n)"],
            ["Space Complexity", "O(1)", "O(1)"],
            ["Caveat", "Works everywhere", "Only on sorted arrays"],
        ]
        
        # Create table with fixed column widths
        table = Table(
            table_data,
            col_labels=[Text("Criteria"), Text("Brute Force"), Text("Two Pointers")],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
            h_buff=0.6,  # Reduced horizontal buffer
            v_buff=0.4   # Reduced vertical buffer
        ).scale(0.7)  # Reduced overall scale
        
        # Position table in center
        table.next_to(title, DOWN, buff=0.5)  # Reduced buffer from title
        
        # Style the headers and entries
        headers = table.get_col_labels()
        headers[0].set_color(YELLOW)
        headers[1].set_color(BLUE)
        headers[2].set_color(GREEN)
        
        # Style all entries at once
        for i in range(3):  # rows
            for j in range(3):  # columns
                entry = table.get_entries((i+1, j))
                if j == 0:  # Criteria column
                    entry.set_color(WHITE)
                elif j == 1:  # Brute Force column
                    entry.set_color(BLUE)
                else:  # Two Pointers column
                    entry.set_color(GREEN)
        
        # Create motivation text
        motivation = Text("Now it's your turn!", color=BLUE, font_size=36)
        motivation.next_to(table, DOWN, buff=0.7)
        
        # Animations
        # 1. Show title
        self.play(Write(title))
        self.wait(0.5)
        
        # 2. Show entire table at once
        self.play(Create(table))
        self.wait(1)
        
        # 3. Show motivation
        self.play(
            Write(motivation),
            motivation.animate.scale(1.1)
        )
        self.play(
            motivation.animate.scale(1/1.1)
        )
        self.wait(1)
        
        # Final fadeout
        self.play(
            *[FadeOut(mob) for mob in [
                title, table, motivation
            ]]
        )
        self.wait(0.5) 