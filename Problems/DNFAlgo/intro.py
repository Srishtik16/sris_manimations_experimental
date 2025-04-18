from manim import *

class IntroScene(Scene):
    def construct(self):
        # Title
        title = Text("Sort Colors (Dutch National Flag Problem)", font_size=36)
        title.to_edge(UP, buff=0.3)
        
        # Input array
        nums = [2, 0, 2, 1, 1, 0]
        
        # Create boxes and labels
        boxes = VGroup()
        num_labels = VGroup()
        
        # Colors for numbers
        colors = {
            0: BLUE,    # Blue for 0
            1: WHITE,   # White for 1
            2: RED      # Red for 2
        }
        
        # Create boxes and labels
        for i, num in enumerate(nums):
            # Create box
            box = Square(
                side_length=1,
                color=colors[num],
                fill_opacity=0.5,
                stroke_width=2
            )
            
            # Create number label
            num_label = Text(
                str(num),
                font_size=24,
                color=BLACK if num == 1 else WHITE
            )
            num_label.move_to(box.get_center())
            
            # Position box
            box.shift(RIGHT * i * 1.2)
            num_label.shift(RIGHT * i * 1.2)
            
            boxes.add(box)
            num_labels.add(num_label)
        
        # Center the group
        boxes_group = VGroup(boxes, num_labels)
        boxes_group.center()
        boxes_group.shift(DOWN * 0.5)
        
        # Create array label
        array_label = Text(
            "nums = [2, 0, 2, 1, 1, 0]",
            font_size=24
        )
        array_label.next_to(boxes_group, UP, buff=0.5)
        
        # Problem statement
        problem_statement = Text(
            "Sort the array containing only 0s, 1s, and 2s in-place.",
            font_size=28
        )
        problem_statement.next_to(boxes_group, DOWN, buff=1.0)
        
        # Animations
        self.play(Write(title))
        self.wait(0.5)
        
        # Show array label
        self.play(Write(array_label))
        self.wait(0.5)
        
        # Show boxes and labels
        self.play(
            LaggedStart(
                *[FadeIn(box) for box in boxes],
                lag_ratio=0.2
            ),
            run_time=1.5
        )
        
        self.play(
            LaggedStart(
                *[Write(label) for label in num_labels],
                lag_ratio=0.2
            ),
            run_time=1.5
        )
        
        # Show problem statement
        self.play(Write(problem_statement))
        self.wait(2)
        
        # Clear the scene
        self.play(
            FadeOut(title),
            FadeOut(array_label),
            FadeOut(boxes),
            FadeOut(num_labels),
            FadeOut(problem_statement),
            FadeOut(boxes_group)
        )