from manim import *

class TailIntuitionScene(Scene):
    def construct(self):
        # Title
        title = Text("Understanding dp[] Array", font_size=36)
        subtitle = Text("Storing smallest ending elements for subsequences of length i+1", font_size=24, color=BLUE)
        title.to_edge(UP, buff=0.3)
        subtitle.next_to(title, DOWN, buff=0.2)
        
        # Create arrays section - shift everything right to center it
        arrays_group = VGroup()
        
        # Create input array
        input_array = [3, 1, 4, 1, 5]
        input_label = Text("Input:", font_size=28)
        input_squares = VGroup(*[
            Square(side_length=0.7).set_fill(color=BLUE_E, opacity=0.3) 
            for _ in input_array
        ]).arrange(RIGHT, buff=0.1)
        input_nums = VGroup(*[
            Text(str(n), font_size=22) for n in input_array
        ])
        for num, square in zip(input_nums, input_squares):
            num.move_to(square)
        input_group = VGroup(input_squares, input_nums)
        input_row = VGroup(input_label, input_group).arrange(RIGHT, buff=0.5)
        
        # Create initial empty dp array
        dp_label = Text("dp[]:", font_size=28)
        empty_dp = Text("", font_size=28, color=YELLOW)
        dp_row = VGroup(dp_label, empty_dp).arrange(RIGHT, buff=0.5)
        
        # Arrange arrays vertically
        arrays_group.add(input_row, dp_row)
        arrays_group.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        
        # Center the arrays section horizontally
        arrays_group.move_to(ORIGIN).shift(UP * 0.5)
        
        # Initial animation
        self.play(
            Write(title),
            Write(subtitle)
        )
        self.wait(0.5)
        
        self.play(
            Write(input_row)
        )
        self.wait(0.5)
        
        self.play(
            Write(dp_row)
        )
        self.wait(0.5)
        
        # Explanation text - make it more compact and centered
        explanation = VGroup(
            Text("• dp[i] stores the smallest ending element", font_size=22),
            Text("  of a subsequence of length i+1", font_size=22),
            Text("• If number > all elements: append", font_size=22),
            Text("• Otherwise: replace first element ≥ number", font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Center explanation below dp array
        explanation.next_to(dp_row, DOWN, buff=0.8)
        explanation.shift(RIGHT * 0.5)  # Slight right shift to center with arrays
        
        self.play(Write(explanation))
        self.wait(1)
        
        # Process each number
        current_dp = []
        dp_squares = VGroup()
        dp_nums = VGroup()
        
        for i, num in enumerate(input_array):
            # Highlight current number
            self.play(input_squares[i].animate.set_fill(color=YELLOW, opacity=0.6))
            
            # Create arrow - adjust start and end points
            arrow = Arrow(
                input_squares[i].get_bottom(),
                dp_label.get_right() + RIGHT * (len(current_dp) * 0.8 + 0.5),  # Adjust spacing
                buff=0.2,
                color=YELLOW
            )
            
            if not current_dp or num > current_dp[-1]:
                # Append case
                current_dp.append(num)
                callout = Text("Append: new longest subsequence", font_size=20, color=GREEN)
                callout.next_to(arrow, DOWN, buff=0.3)  # Position below arrow
                callout.shift(RIGHT * 3.0)
                
                new_square = Square(side_length=0.7).set_fill(color=GREEN_E, opacity=0.3)
                new_num = Text(str(num), font_size=22)
                
                if dp_squares:
                    new_square.next_to(dp_squares[-1], RIGHT, buff=0.1)
                else:
                    new_square.next_to(dp_label, RIGHT, buff=0.5)
                
                new_num.move_to(new_square)
                dp_squares.add(new_square)
                dp_nums.add(new_num)
                
                self.play(
                    Create(arrow),
                    Write(callout),
                    Create(new_square),
                    Write(new_num)
                )
                
            else:
                # Replace case
                replace_idx = 0
                for j, dp_num in enumerate(current_dp):
                    if dp_num >= num:
                        replace_idx = j
                        break
                
                current_dp[replace_idx] = num
                callout = Text("Replace: smaller ending element", font_size=20, color=RED)
                callout.next_to(arrow, DOWN, buff=0.3)  # Position below arrow
                callout.shift(RIGHT * 3.0)
                
                old_num = dp_nums[replace_idx]
                new_num = Text(str(num), font_size=22)
                new_num.move_to(old_num)
                
                self.play(
                    Create(arrow),
                    Write(callout),
                    Transform(old_num, new_num)
                )
            
            self.wait(0.5)
            self.play(
                FadeOut(arrow),
                FadeOut(callout),
                input_squares[i].animate.set_fill(color=BLUE_E, opacity=0.3)
            )
            self.wait(0.5)
        
        # Final state highlight - position below explanation
        final_result = Text(f"Final length: {len(current_dp)}", font_size=28, color=GREEN)
        final_result.next_to(explanation, DOWN, buff=0.6)
        self.play(Write(final_result))
        self.wait(1) 