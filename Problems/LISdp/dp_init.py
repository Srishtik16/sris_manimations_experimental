from manim import *
from CustomArray import CreateArray

class DPInitScene(Scene):
    def construct(self):
        # Title
        title = Text("DP Array Initialization", color=BLUE, font_size=44)
        title.to_edge(UP, buff=0.5)
        
        # Create input array (smaller size)
        input_array = [3, 1, 4, 2, 5]
        array_vis = CreateArray(input_array)
        array_vis.scale(0.8)
        array_vis.to_edge(UP, buff=2)
        
        # Create index labels for input array
        input_indices = VGroup()
        for i in range(len(input_array)):
            index = Text(str(i), font_size=24)
            # Position index at the center of each cell
            cell_width = array_vis[0].width / len(input_array)
            x_pos = array_vis[0].get_left() + (i + 0.5) * cell_width
            index.move_to(array_vis[0].get_bottom() + DOWN * 0.3)
            index.shift(RIGHT * (x_pos - array_vis[0].get_left() - array_vis[0].width/2))
            input_indices.add(index)
        
        # Create DP array (all 1s initially)
        dp_array = CreateArray([1] * len(input_array))
        dp_array.scale(0.8)
        dp_array.next_to(input_indices, DOWN, buff=0.8)
        
        # Create index labels for DP array
        dp_indices = VGroup()
        for i in range(len(input_array)):
            index = Text(f"dp[{i}]", font_size=24)
            # Position index at the center of each cell
            cell_width = dp_array[0].width / len(input_array)
            x_pos = dp_array[0].get_left() + (i + 0.5) * cell_width
            index.move_to(dp_array[0].get_bottom() + DOWN * 0.3)
            index.shift(RIGHT * (x_pos - dp_array[0].get_left() - dp_array[0].width/2))
            dp_indices.add(index)
        
        # Create DP table label
        dp_label = Text("DP Table:", font_size=32, color=YELLOW)
        dp_label.next_to(dp_array, LEFT, buff=0.5)
        
        # Create explanation text
        explanation = Text("dp[i] = length of LIS ending at index i", 
                         font_size=36, color=BLUE)
        explanation.next_to(dp_indices, DOWN, buff=0.8)
        
        # Animations
        # 1. Show input array with indices
        self.play(
            array_vis.create_animation(),
            run_time=1.5
        )
        self.play(Write(input_indices))
        self.wait(0.5)
        
        # 2. Show DP array initialization
        self.play(
            Write(dp_label),
            dp_array.create_animation(),
            run_time=1.5
        )
        self.play(Write(dp_indices))
        self.wait(0.5)
        
        # 3. Show explanation
        self.play(
            Write(explanation),
            run_time=1
        )
        self.wait(1)
        
        # Store elements for future reference
        self.input_array = array_vis
        self.dp_array = dp_array
        self.input_indices = input_indices
        self.dp_indices = dp_indices
        self.explanation = explanation 