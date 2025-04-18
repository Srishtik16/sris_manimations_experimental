from manim import *

class ArrayDisplayScene(Scene):
    def construct(self):
        # Title
        title = Text("Initial Array", font_size=36)
        title.to_edge(UP, buff=0.3)
        
        # Input array
        nums = [2, 0, 2, 1, 1, 0]
        
        # Create boxes and labels
        boxes = VGroup()
        num_labels = VGroup()
        index_labels = VGroup()
        
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
            
            # Create index label
            index_label = Text(
                str(i),
                font_size=20,
                color=WHITE
            )
            index_label.next_to(box, DOWN, buff=0.2)
            
            # Position box
            box.shift(RIGHT * i * 1.2)
            num_label.shift(RIGHT * i * 1.2)
            index_label.shift(RIGHT * i * 1.2)
            
            boxes.add(box)
            num_labels.add(num_label)
            index_labels.add(index_label)
        
        # Center the group
        boxes_group = VGroup(boxes, num_labels, index_labels)
        boxes_group.center()
        boxes_group.shift(DOWN * 0.5)
        
        # Animations
        self.play(Write(title))
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
        
        self.play(
            LaggedStart(
                *[Write(label) for label in index_labels],
                lag_ratio=0.2
            ),
            run_time=1.5
        )
        
        self.wait(2)
        
        # Clear the scene
        self.play(
            FadeOut(title),
            FadeOut(boxes),
            FadeOut(num_labels),
            FadeOut(index_labels)
        ) 