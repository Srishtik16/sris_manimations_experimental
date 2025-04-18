from manim import *

class BinarySearchScene(Scene):
    def construct(self):
        # Title
        title = Text("Building LIS using Binary Search", font_size=36)
        subtitle = Text("Finding insertion position efficiently", font_size=24, color=BLUE)
        title.to_edge(UP, buff=0.3)
        subtitle.next_to(title, DOWN, buff=0.2)
        
        # Create arrays section
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
        input_row = VGroup(input_label, input_group := VGroup(input_squares, input_nums)).arrange(RIGHT, buff=0.5)
        
        # Create dp array
        dp_label = Text("dp[]:", font_size=28)
        empty_dp = Text("", font_size=28, color=YELLOW)
        dp_row = VGroup(dp_label, empty_dp).arrange(RIGHT, buff=0.5)
        
        # Arrange arrays vertically
        arrays_group.add(input_row, dp_row)
        arrays_group.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        arrays_group.move_to(ORIGIN).shift(UP * 0.5)
        
        # Initial animation
        self.play(
            Write(title),
            Write(subtitle)
        )
        self.wait(0.5)
        
        self.play(Write(input_row))
        self.play(Write(dp_row))
        self.wait(0.5)
        
        # Process each number using binary search
        current_dp = []
        dp_squares = VGroup()
        dp_nums = VGroup()
        
        def create_binary_search_visual(arr, target, left, right):
            # Create visualization of binary search range
            highlight_group = VGroup()
            for i in range(left, right + 1):
                square = dp_squares[i].copy()
                square.set_fill(YELLOW_E, opacity=0.3)
                highlight_group.add(square)
            return highlight_group
        
        for i, num in enumerate(input_array):
            # Highlight current number
            self.play(input_squares[i].animate.set_fill(color=YELLOW, opacity=0.6))
            
            if not current_dp:
                # Empty dp case
                current_dp.append(num)
                new_square = Square(side_length=0.7).set_fill(color=GREEN_E, opacity=0.3)
                new_num = Text(str(num), font_size=22)
                
                new_square.next_to(dp_label, RIGHT, buff=0.5)
                new_num.move_to(new_square)
                
                dp_squares.add(new_square)
                dp_nums.add(new_num)
                
                callout = Text("First element: Insert", font_size=20, color=GREEN)
                callout.next_to(new_square, DOWN, buff=0.2)
                
                self.play(
                    Create(new_square),
                    Write(new_num),
                    Write(callout)
                )
                self.wait(0.5)
                self.play(FadeOut(callout))
            
            else:
                # Binary search visualization
                left, right = 0, len(current_dp) - 1
                insert_pos = len(current_dp)  # Default to append position
                
                binary_title = Text("Binary Search", font_size=24, color=YELLOW)
                binary_title.next_to(dp_row, RIGHT, buff=4.0)
                self.play(Write(binary_title))
                
                while left <= right:
                    mid = (left + right) // 2
                    
                    # Highlight current search range
                    search_range = create_binary_search_visual(current_dp, num, left, right)
                    mid_highlight = dp_squares[mid].copy()
                    mid_highlight.set_fill(RED_E, opacity=0.5)
                    
                    search_info = VGroup(
                        Text(f"left: {left}", font_size=20),
                        Text(f"mid: {mid}", font_size=20),
                        Text(f"right: {right}", font_size=20)
                    ).arrange(DOWN, aligned_edge=LEFT)
                    search_info.next_to(binary_title, DOWN, buff=0.3)
                    
                    self.play(
                        FadeIn(search_range),
                        FadeIn(mid_highlight),
                        Write(search_info)
                    )
                    
                    if current_dp[mid] >= num:
                        right = mid - 1
                        insert_pos = mid
                        comparison = Text("dp[mid] ≥ num: search left", font_size=20)
                    else:
                        left = mid + 1
                        comparison = Text("dp[mid] < num: search right", font_size=20)
                    
                    comparison.next_to(search_info, DOWN, buff=0.3)
                    self.play(Write(comparison))
                    self.wait(0.5)
                    
                    self.play(
                        FadeOut(search_range),
                        FadeOut(mid_highlight),
                        FadeOut(search_info),
                        FadeOut(comparison)
                    )
                
                self.play(FadeOut(binary_title))
                
                # Update dp array
                if insert_pos == len(current_dp):
                    # Append case
                    current_dp.append(num)
                    new_square = Square(side_length=0.7).set_fill(color=GREEN_E, opacity=0.3)
                    new_num = Text(str(num), font_size=22)
                    
                    new_square.next_to(dp_squares[-1], RIGHT, buff=0.1)
                    new_num.move_to(new_square)
                    
                    dp_squares.add(new_square)
                    dp_nums.add(new_num)
                    
                    callout = Text("Append: new longest subsequence", font_size=20, color=GREEN)
                    callout.next_to(new_square, DOWN, buff=0.2)
                    
                    self.play(
                        Create(new_square),
                        Write(new_num),
                        Write(callout)
                    )
                else:
                    # Replace case
                    current_dp[insert_pos] = num
                    old_num = dp_nums[insert_pos]
                    new_num = Text(str(num), font_size=22)
                    new_num.move_to(old_num)
                    
                    callout = Text("Replace: smaller ending element", font_size=20, color=RED)
                    callout.next_to(dp_squares[insert_pos], DOWN, buff=0.2)
                    
                    self.play(
                        Transform(old_num, new_num),
                        Write(callout)
                    )
                
                self.wait(0.5)
                self.play(FadeOut(callout))
            
            # Reset input highlight
            self.play(input_squares[i].animate.set_fill(color=BLUE_E, opacity=0.3))
            self.wait(0.5)
        
        # Final state
        final_result = Text(f"Final LIS length: {len(current_dp)}", font_size=28, color=GREEN)
        final_result.next_to(arrays_group, DOWN, buff=0.8)
        self.play(Write(final_result))
        self.wait(1) 