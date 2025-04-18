from manim import *

class PatternMatchingScene(Scene):
    def construct(self):
        # Title
        title = Text("Pattern Matching with Z-Algorithm", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # Input strings
        pattern = "abc"
        text = "xabcabcabc"
        combined = "abc$xabcabcabc"
        pattern_len = len(pattern)
        
        # Create input display
        p_label = Text("P = ", font_size=24, color=WHITE)
        p_text = Text(f'"{pattern}"', font_size=24, color=YELLOW)
        p_group = VGroup(p_label, p_text).arrange(RIGHT, buff=0.2)
        
        t_label = Text("T = ", font_size=24, color=WHITE)
        t_text = Text(f'"{text}"', font_size=24, color=YELLOW)
        t_group = VGroup(t_label, t_text).arrange(RIGHT, buff=0.2)
        
        s_label = Text("S = ", font_size=24, color=WHITE)
        s_text = Text(f'"{combined}"', font_size=24, color=YELLOW)
        s_group = VGroup(s_label, s_text).arrange(RIGHT, buff=0.2)
        
        # Arrange input groups
        input_groups = VGroup(p_group, t_group, s_group)
        input_groups.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        input_groups.next_to(title, DOWN, buff=0.8)
        
        # Animate input display
        self.play(
            Write(p_group),
            Write(t_group),
            Write(s_group),
            run_time=1.5
        )
        self.wait(0.5)

        # Create boxes for combined string
        boxes = []
        for i, char in enumerate(combined):
            box = Square(side_length=0.6, color=WHITE)
            char_text = Text(char, font_size=20, color=WHITE)
            char_text.move_to(box.get_center())
            box_group = VGroup(box, char_text)
            boxes.append(box_group)
        
        # Arrange boxes horizontally
        string_group = VGroup(*boxes)
        string_group.arrange(RIGHT, buff=0.05)
        string_group.next_to(input_groups, DOWN, buff=0.8)
        
        # Add indices below boxes
        indices = []
        for i in range(len(combined)):
            index = Text(str(i), font_size=16, color=GRAY)
            index.next_to(boxes[i], DOWN, buff=0.1)
            indices.append(index)
        
        # Animate string and indices
        self.play(
            *[Create(box) for box in boxes],
            *[Write(index) for index in indices],
            run_time=1.5
        )
        self.wait(0.5)

        # Create Z-array row
        z_array = []
        for i in range(len(combined)):
            z_box = Square(side_length=0.6, color=WHITE)
            z_text = Text("0", font_size=20, color=WHITE)
            z_text.move_to(z_box.get_center())
            z_array.append(VGroup(z_box, z_text))
        
        z_array_group = VGroup(*z_array)
        z_array_group.arrange(RIGHT, buff=0.05)
        z_array_group.next_to(string_group, DOWN, buff=0.8)
        
        # Label for Z-array
        z_label = Text("Z-array:", font_size=24, color=WHITE)
        z_label.next_to(z_array_group, LEFT, buff=0.3)
        
        self.play(
            Write(z_label),
            *[Create(z_box) for z_box, _ in z_array],
            *[Write(z_text) for _, z_text in z_array],
            run_time=1.5
        )

        # Compute Z-array (simplified for animation)
        z_values = [0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0]  # Precomputed values
        
        # Animate Z-array computation
        for i in range(1, len(combined)):
            # Update Z[i] value
            z_array[i][1].become(Text(str(z_values[i]), font_size=20, color=GREEN))
            z_array[i][1].move_to(z_array[i][0].get_center())
            self.play(
                z_array[i][1].animate.set_color(GREEN),
                run_time=0.2
            )
        
        self.wait(0.5)

        # Show pattern length
        pattern_len_text = Text(f"len(P) = {pattern_len}", font_size=24, color=YELLOW)
        pattern_len_text.next_to(z_array_group, DOWN, buff=0.8)
        self.play(Write(pattern_len_text))
        
        # Find and highlight matches
        match_positions = []
        for i in range(len(combined)):
            if z_values[i] == pattern_len:
                # Highlight Z-value
                z_highlight = SurroundingRectangle(z_array[i][0], color=GREEN, buff=0.05)
                self.play(Create(z_highlight))
                
                # Calculate position in original text
                text_pos = i - pattern_len - 1  # Adjust for pattern and delimiter
                if text_pos >= 0:
                    # Highlight in original text
                    text_highlight = SurroundingRectangle(boxes[i][0], color=GREEN, buff=0.05)
                    self.play(Create(text_highlight))
                    
                    # Show match position
                    match_text = Text(f"Match at pos {text_pos}", font_size=20, color=GREEN)
                    match_text.next_to(text_highlight, UP, buff=0.2)
                    self.play(Write(match_text))
                    
                    match_positions.append((text_highlight, match_text))
                
                self.play(FadeOut(z_highlight))
        
        self.wait(1)
        
        # Clean up highlights
        for highlight, text in match_positions:
            self.play(
                FadeOut(highlight),
                FadeOut(text),
                run_time=0.3
            )
        
        self.wait(1) 