from manim import *
from CustomArray import CreateArray

class PointerScene(Scene):
    def construct(self):
        # Title
        title = Text("Two Pointer Approach", font_size=40, color=BLUE)
        title.to_edge(UP, buff=0.5)
        
        # Create input array
        input_array = ['a', 'b', 'c', 'a', 'b', 'c', 'b', 'b']
        array_vis = CreateArray(input_array)
        
        # Position array below title
        array_vis.next_to(title, DOWN, buff=1)
        
        # Create index labels
        indices = VGroup(*[
            Text(str(i), font_size=24)
            for i in range(len(input_array))
        ]).arrange(RIGHT, buff=0.82)
        indices.next_to(array_vis, DOWN, buff=0.3)
        
        # Create pointers with different vertical positions
        left_pointer = Arrow(
            start=DOWN * 0.5,
            end=UP * 0.5,
            color=YELLOW,
            max_tip_length_to_length_ratio=0.15,
            stroke_width=3
        )
        right_pointer = Arrow(
            start=DOWN * 0.7,  # Slightly lower start for r pointer
            end=UP * 0.3,      # Slightly lower end for r pointer
            color=GREEN,
            max_tip_length_to_length_ratio=0.15,
            stroke_width=3
        )
        
        # Create pointer labels
        l_label = Text("l", font_size=28, color=YELLOW)
        r_label = Text("r", font_size=28, color=GREEN)
        
        # Position pointers at index 0 and 1
        left_pointer.next_to(array_vis[0], DOWN, buff=0.8)
        right_pointer.next_to(array_vis[1], DOWN, buff=1.0)  # Slightly lower
        
        # Position labels
        l_label.next_to(left_pointer, DOWN, buff=0.1)
        r_label.next_to(right_pointer, DOWN, buff=0.1)
        
        # Create pointer groups
        pointer_group_l = VGroup(left_pointer, l_label)
        pointer_group_r = VGroup(right_pointer, r_label)
        
        # Ensure correct horizontal positioning
        pointer_group_l.move_to(array_vis[0].get_center() + DOWN * 1.2)
        pointer_group_r.move_to(array_vis[1].get_center() + DOWN * 1.5)  # Slightly lower
        
        # Animations
        # 1. Show title
        self.play(Write(title))
        self.wait(0.5)
        
        # 2. Create array
        self.play(array_vis.create_animation())
        self.wait(0.5)
        
        # 3. Show indices
        self.play(Write(indices))
        self.wait(0.5)
        
        # 4. Show pointers one at a time
        self.play(Create(pointer_group_l))
        self.wait(0.3)
        self.play(Create(pointer_group_r))
        self.wait(0.5)
        
        # Store the array and pointers as instance variables for later use
        self.array_vis = array_vis
        self.pointer_group_l = pointer_group_l
        self.pointer_group_r = pointer_group_r
        self.indices = indices 