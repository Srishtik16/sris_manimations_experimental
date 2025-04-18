from manim import *

class ZArrayMeaningScene(Scene):
    def construct(self):
        # Title
        title = Text("Understanding Z[i] Values", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # Example string
        string = "aabxaab"
        string_length = len(string)
        
        # Create boxes with characters inside
        boxes = []
        for i, char in enumerate(string):
            box = Square(side_length=0.6, color=WHITE)
            char_text = Text(char, font_size=20, color=WHITE)
            char_text.move_to(box.get_center())
            box_group = VGroup(box, char_text)
            boxes.append(box_group)
        
        # Arrange boxes horizontally with less spacing
        string_group = VGroup(*boxes)
        string_group.arrange(RIGHT, buff=0.05)
        string_group.next_to(title, DOWN, buff=0.8)
        
        # Add indices below boxes
        indices = []
        for i in range(string_length):
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

        # Focus on i = 4
        i = 4
        question = Text("How much of the prefix repeats starting from here?", font_size=24, color=YELLOW)
        question.next_to(string_group, DOWN, buff=0.8)
        self.play(Write(question))
        
        # Highlight the current position
        current_box = boxes[i]
        current_highlight = SurroundingRectangle(current_box, color=YELLOW, buff=0.05)
        self.play(Create(current_highlight))
        
        # Show prefix matching
        prefix = string[:i]
        prefix_boxes = boxes[:i]
        
        # Create arrows for matching
        arrows = []
        z_value = 0
        for j in range(i):
            if j + i < string_length and string[j] == string[j + i]:
                arrow = Arrow(
                    prefix_boxes[j].get_center(),
                    boxes[j + i].get_center() - RIGHT * 0.3,
                    color=GREEN,
                    buff=0.05,
                    stroke_width=1.5
                )
                if j + i == 4:
                    arrows.append(arrow)
                z_value += 1
        
        # Animate the matching
        self.play(
            *[Create(arrow) for arrow in arrows],
            run_time=1.5
        )
        
        # Show Z[i] value
        z_text = Text(f"Z[{i}] = {z_value}", font_size=28, color=GREEN)
        z_text.next_to(question, DOWN, buff=0.8)
        self.play(Write(z_text))
        
        # Create Z-array row
        z_array = []
        for i in range(string_length):
            z_box = Square(side_length=0.6, color=WHITE)
            z_text = Text("?", font_size=20, color=WHITE)
            z_text.move_to(z_box.get_center())
            z_array.append(VGroup(z_box, z_text))
        
        z_array_group = VGroup(*z_array)
        z_array_group.arrange(RIGHT, buff=0.05)
        z_array_group.next_to(z_text, DOWN, buff=0.8)
        
        # Label for Z-array
        z_label = Text("Z-array:", font_size=24, color=WHITE)
        z_label.next_to(z_array_group, LEFT, buff=0.3)
        
        self.play(
            Write(z_label),
            *[Create(z_box) for z_box, _ in z_array],
            *[Write(z_text) for _, z_text in z_array],
            run_time=1.5
        )
        
        # Update Z[4] value
        z_array[4][1].become(Text(str(z_value), font_size=20, color=GREEN))
        z_array[4][1].move_to(z_array[4][0].get_center())
        self.play(
            z_array[4][1].animate.set_color(GREEN),
            run_time=0.5
        )
        
        self.wait(1) 