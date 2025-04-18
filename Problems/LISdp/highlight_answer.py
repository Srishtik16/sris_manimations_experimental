from manim import *
from CustomArray import CreateArray

class HighlightAnswerScene(Scene):
    def construct(self):
        # Title
        title = Text("Finding Maximum LIS Length", color=BLUE, font_size=44)
        title.to_edge(UP, buff=0.5)
        
        # Create final DP array state
        input_array = [3, 1, 4, 2, 5]
        dp_values = [1, 1, 2, 2, 3]  # Final DP values
        
        # Create arrays
        array_vis = CreateArray(input_array)
        dp_array = CreateArray(dp_values)
        
        # Scale and position arrays
        array_vis.scale(0.8)
        dp_array.scale(0.8)
        array_vis.next_to(title, DOWN, buff=1)
        dp_array.next_to(array_vis, DOWN, buff=1.5)
        
        # Create labels
        input_label = Text("Input Array:", font_size=32, color=YELLOW)
        dp_label = Text("DP Array:", font_size=32, color=YELLOW)
        input_label.next_to(array_vis, LEFT, buff=0.5)
        dp_label.next_to(dp_array, LEFT, buff=0.5)
        
        # Create indices
        indices = VGroup()
        dp_indices = VGroup()
        for i in range(len(input_array)):
            # Input array indices
            index = Text(str(i), font_size=24)
            cell_width = array_vis[0].width / len(input_array)
            x_pos = array_vis[0].get_left() + (i + 0.5) * cell_width
            index.move_to(array_vis[0].get_bottom() + DOWN * 0.3)
            index.shift(RIGHT * (x_pos - array_vis[0].get_left() - array_vis[0].width/2))
            indices.add(index)
            
            # DP array indices
            dp_index = Text(f"dp[{i}]", font_size=24)
            x_pos = dp_array[0].get_left() + (i + 0.5) * cell_width
            dp_index.move_to(dp_array[0].get_bottom() + DOWN * 0.3)
            dp_index.shift(RIGHT * (x_pos - dp_array[0].get_left() - dp_array[0].width/2))
            dp_indices.add(dp_index)
        
        # Show arrays
        self.play(
            Write(title),
            array_vis.create_animation(),
            Write(input_label),
            Write(indices),
            run_time=2
        )
        self.play(
            dp_array.create_animation(),
            Write(dp_label),
            Write(dp_indices),
            run_time=2
        )
        self.wait(1)
        
        # Find maximum value
        max_val = max(dp_values)
        max_indices = [i for i, x in enumerate(dp_values) if x == max_val]
        
        # Highlight scanning process
        scan_text = Text("Scanning dp[] for maximum value...", font_size=32)
        scan_text.next_to(dp_array, DOWN, buff=1.5)
        self.play(Write(scan_text))
        
        # Scan animation
        for i in range(len(dp_values)):
            self.play(
                dp_array[2][i].animate.set_color(YELLOW),
                run_time=0.3
            )
            if i in max_indices:
                self.play(
                    dp_array[2][i].animate.set_color(GREEN),
                    Flash(dp_array[2][i], color=GREEN, flash_radius=0.3),
                    run_time=0.5
                )
            else:
                self.play(
                    dp_array[2][i].animate.set_color(WHITE),
                    run_time=0.3
                )
        
        # Show final answer
        self.play(FadeOut(scan_text))
        
        result_text = Text(f"Length of Longest Increasing Subsequence = {max_val}", 
                         font_size=36, color=GREEN)
        result_text.next_to(dp_array, DOWN, buff=1.5)
        
        self.play(
            Write(result_text),
            run_time=1
        )
        self.wait(1)
        
        # Store elements for future reference
        self.input_array = array_vis
        self.dp_array = dp_array
        self.result_text = result_text 