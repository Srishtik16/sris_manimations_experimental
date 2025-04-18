from manim import *

class OptimizedComputationScene(Scene):
    def construct(self):
        # Title
        title = Text("Optimized Z-Algorithm with [l, r] Window", font_size=36, color=BLUE)
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

        # Initialize l and r
        l, r = 0, 0
        window_rect = Rectangle(
            width=0.6, height=0.6,
            color=YELLOW,
            fill_opacity=0.2
        )
        window_rect.move_to(boxes[0].get_center())
        
        # Show initial window
        self.play(Create(window_rect))
        
        # Optimized computation
        for i in range(1, n):
            # Highlight current position
            current_highlight = SurroundingRectangle(boxes[i], color=YELLOW, buff=0.05)
            self.play(Create(current_highlight))
            
            # Show code condition
            if i > r:
                condition_text = Text("i > r: Naive match", font_size=24, color=RED)
            else:
                condition_text = Text("i ≤ r: Reuse Z[i-l]", font_size=24, color=GREEN)
            condition_text.next_to(z_array_group, DOWN, buff=0.8)
            self.play(Write(condition_text))
            
            if i > r:
                # Naive match
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
                    
                    self.play(Create(prefix_arrow), run_time=0.3)
                    z_i += 1
                    
                    # Update Z[i] value
                    z_array[i][1].become(Text(str(z_i), font_size=20, color=GREEN))
                    z_array[i][1].move_to(z_array[i][0].get_center())
                    self.play(
                        z_array[i][1].animate.set_color(GREEN),
                        run_time=0.2
                    )
                    
                    self.play(FadeOut(prefix_arrow), run_time=0.2)
                
                # Update window
                l, r = i, i + z_i
                new_window = Rectangle(
                    width=(r - l) * 0.65,
                    height=0.6,
                    color=YELLOW,
                    fill_opacity=0.2
                )
                new_window.move_to(boxes[l].get_center() + RIGHT * (r - l - 1) * 0.325)
                
                self.play(
                    Transform(window_rect, new_window),
                    run_time=0.5
                )
            else:
                # Reuse Z[i-l]
                z_i = min(r - i, int(z_array[i - l][1].get_text()))
                z_array[i][1].become(Text(str(z_i), font_size=20, color=BLUE))
                z_array[i][1].move_to(z_array[i][0].get_center())
                
                # Show reuse connection
                reuse_arrow = Arrow(
                    z_array[i - l][0].get_center(),
                    z_array[i][0].get_center(),
                    color=BLUE,
                    buff=0.05,
                    stroke_width=1.5
                )
                
                self.play(
                    Create(reuse_arrow),
                    z_array[i][1].animate.set_color(BLUE),
                    run_time=0.5
                )
                
                # Try to extend
                while i + z_i < n and string[z_i] == string[i + z_i]:
                    # Show comparison
                    prefix_arrow = Arrow(
                        boxes[z_i].get_center(),
                        boxes[i + z_i].get_center() - RIGHT * 0.3,
                        color=GREEN,
                        buff=0.05,
                        stroke_width=1.5
                    )
                    
                    self.play(Create(prefix_arrow), run_time=0.3)
                    z_i += 1
                    
                    # Update Z[i] value
                    z_array[i][1].become(Text(str(z_i), font_size=20, color=GREEN))
                    z_array[i][1].move_to(z_array[i][0].get_center())
                    self.play(
                        z_array[i][1].animate.set_color(GREEN),
                        run_time=0.2
                    )
                    
                    self.play(FadeOut(prefix_arrow), run_time=0.2)
                
                # Update window if extended
                if i + z_i > r:
                    l, r = i, i + z_i
                    new_window = Rectangle(
                        width=(r - l) * 0.65,
                        height=0.6,
                        color=YELLOW,
                        fill_opacity=0.2
                    )
                    new_window.move_to(boxes[l].get_center() + RIGHT * (r - l - 1) * 0.325)
                    
                    self.play(
                        Transform(window_rect, new_window),
                        run_time=0.5
                    )
                
                self.play(FadeOut(reuse_arrow), run_time=0.3)
            
            # Clean up
            self.play(
                FadeOut(current_highlight),
                FadeOut(condition_text),
                run_time=0.3
            )
            
            # Pause between positions
            self.wait(0.5)
        
        self.wait(2) 