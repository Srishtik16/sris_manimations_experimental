from manim import *

class NaiveComputationScene(Scene):
    def construct(self):
        # Title
        title = Text("Naive Z-Function Computation", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # Example string
        string = "aabxaab"
        n = len(string)
        
        # Create boxes with characters inside
        boxes = []
        for i, char in enumerate(string):
            box = Square(side_length=0.6, color=WHITE)
            char_text = Text(char, font_size=20, color=WHITE)
            char_text.move_to(box.get_center())
            box_group = VGroup(box, char_text)
            boxes.append(box_group)
        
        # Arrange boxes horizontally
        string_group = VGroup(*boxes)
        string_group.arrange(RIGHT, buff=0.05)
        string_group.next_to(title, DOWN, buff=0.8)
        
        # Add indices below boxes
        indices = []
        for i in range(n):
            index = Text(str(i), font_size=16, color=GRAY)
            index.next_to(boxes[i], DOWN, buff=0.1)
            indices.append(index)
        
        # Animate the string and indices
        self.play(
            *[Create(box) for box in boxes],
            *[Write(index) for index in indices],
            run_time=1.5
        )
        self.wait(0.5)

        # Create Z-array row
        z_array = []
        for i in range(n):
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

        # Naive computation
        for i in range(1, n):
            # Highlight current position
            current_highlight = SurroundingRectangle(boxes[i], color=YELLOW, buff=0.05)
            self.play(Create(current_highlight))
            
            z_i = 0
            while i + z_i < n and string[z_i] == string[i + z_i]:
                # Show comparison
                prefix_arrow = Arrow(
                    boxes[z_i].get_center(),
                    boxes[i + z_i].get_center() - RIGHT * 0.3,
                    color=GREEN,
                    buff=0.05,
                    stroke_width=1.5
                )
                
                # Show match indicator
                match_text = Text("✓", font_size=20, color=GREEN)
                match_text.next_to(prefix_arrow, UP, buff=0.1)
                
                self.play(
                    Create(prefix_arrow),
                    Write(match_text),
                    run_time=0.5
                )
                
                z_i += 1
                
                # Update Z[i] value
                z_array[i][1].become(Text(str(z_i), font_size=20, color=GREEN))
                z_array[i][1].move_to(z_array[i][0].get_center())
                self.play(
                    z_array[i][1].animate.set_color(GREEN),
                    run_time=0.3
                )
                
                # Remove match indicator
                self.play(
                    FadeOut(prefix_arrow),
                    FadeOut(match_text),
                    run_time=0.3
                )
            
            # Show no more matches
            if i + z_i < n:
                no_match_arrow = Arrow(
                    boxes[z_i].get_center(),
                    boxes[i + z_i].get_center() - RIGHT * 0.3,
                    color=RED,
                    buff=0.05,
                    stroke_width=1.5
                )
                
                no_match_text = Text("X", font_size=20, color=RED)
                no_match_text.next_to(no_match_arrow, UP, buff=0.1)
                
                self.play(
                    Create(no_match_arrow),
                    Write(no_match_text),
                    run_time=0.5
                )
                
                self.play(
                    FadeOut(no_match_arrow),
                    FadeOut(no_match_text),
                    run_time=0.3
                )
            
            # Remove current highlight
            self.play(FadeOut(current_highlight))
            
            # Pause between positions
            self.wait(0.5)
        
        self.wait(2) 