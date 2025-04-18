from manim import *
from CustomArray import CreateArray

class DPIterationScene(Scene):
    def construct(self):
        # Title
        title = Text("DP Iteration Process", color=BLUE, font_size=44)
        title.to_edge(UP, buff=0.5)
        
        # Create arrays (smaller size)
        input_array = [3, 1, 4, 2, 5]
        array_vis = CreateArray(input_array)
        array_vis.scale(0.8)
        array_vis.next_to(title, DOWN, buff=1)
        
        # Create DP array
        dp_values = [1] * len(input_array)
        dp_array = CreateArray(dp_values)
        dp_array.scale(0.8)
        dp_array.next_to(array_vis, DOWN, buff=1.5)
        
        # Create index labels
        indices = VGroup()
        dp_indices = VGroup()
        for i in range(len(input_array)):
            # Input array indices
            index = Text(str(i), font_size=24)
            # Position index at the center of each cell
            cell_width = array_vis[0].width / len(input_array)
            x_pos = array_vis[0].get_left() + (i + 0.5) * cell_width
            index.move_to(array_vis[0].get_bottom() + DOWN * 0.3)
            index.shift(RIGHT * (x_pos - array_vis[0].get_left() - array_vis[0].width/2))
            indices.add(index)
            
            # DP array indices
            dp_index = Text(f"dp[{i}]", font_size=24)
            # Position index at the center of each cell
            x_pos = dp_array[0].get_left() + (i + 0.5) * cell_width
            dp_index.move_to(dp_array[0].get_bottom() + DOWN * 0.3)
            dp_index.shift(RIGHT * (x_pos - dp_array[0].get_left() - dp_array[0].width/2))
            dp_indices.add(dp_index)
        
        # Labels
        input_label = Text("Input Array:", font_size=32, color=YELLOW)
        input_label.next_to(array_vis, LEFT, buff=0.5)
        
        dp_label = Text("DP Array:", font_size=32, color=YELLOW)
        dp_label.next_to(dp_array, LEFT, buff=0.5)
        
        # Show initial setup
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
        
        # Comparison box template
        comparison_box = VGroup(
            Text("Comparing:", font_size=28),
            Text("", font_size=24),  # Will be updated for each comparison
            Text("", font_size=24),  # Result of comparison
        ).arrange(DOWN, buff=0.2)
        comparison_box.to_edge(RIGHT, buff=1)
        
        # Update box template
        update_box = VGroup(
            Text("Update:", font_size=28),
            Text("", font_size=24),  # Will be updated for each dp[i] update
        ).arrange(DOWN, buff=0.2)
        update_box.next_to(comparison_box, DOWN, buff=1)
        
        # Main iteration
        for i in range(len(input_array)):
            # Highlight current i
            self.play(
                array_vis[2][i].animate.set_color(RED),  # Highlight current number
                run_time=0.5
            )
            
            max_dp = 1
            for j in range(i):
                # Highlight j
                self.play(
                    array_vis[2][j].animate.set_color(YELLOW),
                    run_time=0.3
                )
                
                # Show comparison
                comparison_text = f"arr[{j}]({input_array[j]}) < arr[{i}]({input_array[i]})?"
                result = "✓" if input_array[j] < input_array[i] else "✗"
                result_color = GREEN if input_array[j] < input_array[i] else RED
                
                comparison = VGroup(
                    Text("Comparing:", font_size=28),
                    Text(comparison_text, font_size=24),
                    Text(result, font_size=28, color=result_color)
                ).arrange(DOWN, buff=0.2)
                comparison.move_to(comparison_box)
                
                self.play(
                    FadeIn(comparison),
                    run_time=0.5
                )
                
                if input_array[j] < input_array[i]:
                    # Show potential update
                    new_dp = dp_values[j] + 1
                    update_text = f"dp[{i}] = max({dp_values[i]}, {dp_values[j]} + 1)"
                    
                    update = VGroup(
                        Text("Update:", font_size=28),
                        Text(update_text, font_size=24)
                    ).arrange(DOWN, buff=0.2)
                    update.move_to(update_box)
                    
                    self.play(FadeIn(update))
                    
                    if new_dp > max_dp:
                        max_dp = new_dp
                        # Update dp value
                        dp_values[i] = max_dp
                        new_dp_number = Text(str(max_dp), font_size=24)
                        new_dp_number.move_to(dp_array[2][i])
                        
                        self.play(
                            Transform(dp_array[2][i], new_dp_number),
                            Flash(dp_array[2][i], color=GREEN, flash_radius=0.3),
                            run_time=0.5
                        )
                    
                    self.play(FadeOut(update))
                
                # Clean up comparison
                self.play(
                    FadeOut(comparison),
                    array_vis[2][j].animate.set_color(WHITE),
                    run_time=0.3
                )
            
            # Reset i highlight
            self.play(
                array_vis[2][i].animate.set_color(WHITE),
                run_time=0.5
            )
        
        self.wait(1)
        
        # Store elements for future reference
        self.input_array = array_vis
        self.dp_array = dp_array
        self.indices = indices
        self.dp_indices = dp_indices 