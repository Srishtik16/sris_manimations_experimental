from manim import *

class SegmentTreeUseScene(Scene):
    def construct(self):
        # Title
        title = Text("Using Segment Tree for LIS", font_size=36)
        subtitle = Text("Efficient range queries and updates", font_size=24, color=BLUE)
        title.to_edge(UP, buff=0.3)
        subtitle.next_to(title, DOWN, buff=0.2)
        
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
        
        # Create dp array
        dp_label = Text("dp[]:", font_size=28)
        dp_squares = VGroup(*[
            Square(side_length=0.7).set_fill(color=GREEN_E, opacity=0.3) 
            for _ in input_array
        ]).arrange(RIGHT, buff=0.1)
        dp_nums = VGroup(*[
            Text("0", font_size=22) for _ in input_array
        ])
        for num, square in zip(dp_nums, dp_squares):
            num.move_to(square)
        dp_group = VGroup(dp_squares, dp_nums)
        dp_row = VGroup(dp_label, dp_group).arrange(RIGHT, buff=0.5)
        
        # Create value to index mapping
        sorted_unique = sorted(set(input_array))
        value_to_index = {val: idx for idx, val in enumerate(sorted_unique)}
        
        # Create segment tree array (simplified visualization)
        st_label = Text("Segment Tree:", font_size=28)
        st_squares = VGroup(*[
            Square(side_length=0.7).set_fill(color=YELLOW_E, opacity=0.3) 
            for _ in range(len(sorted_unique))
        ]).arrange(RIGHT, buff=0.1)
        st_nums = VGroup(*[
            Text("0", font_size=22) for _ in range(len(sorted_unique))
        ])
        for num, square in zip(st_nums, st_squares):
            num.move_to(square)
        st_group = VGroup(st_squares, st_nums)
        st_row = VGroup(st_label, st_group).arrange(RIGHT, buff=0.5)
        
        # Arrange arrays vertically
        arrays_group = VGroup(input_row, dp_row, st_row)
        arrays_group.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        arrays_group.move_to(ORIGIN).shift(UP * 0.5)
        
        # Initial animation
        self.play(
            Write(title),
            Write(subtitle)
        )
        self.wait(0.5)
        
        # Show arrays
        self.play(Write(input_row))
        self.play(Write(dp_row))
        self.play(Write(st_row))
        self.wait(0.5)
        
        # Show key operations
        operations = VGroup(
            Text("Key Operations:", font_size=28, color=YELLOW),
            Text("1. query(0, a[i]-1) → get max in range", font_size=24),
            Text("2. update(a[i], dp[i]) → set max at pos", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        operations.next_to(dp_row, RIGHT, buff=0.2)
        operations.scale(0.7)
        
        self.play(Write(operations))
        self.wait(1)
        self.play(FadeOut(operations))
        
        # Process each number
        for i, num in enumerate(input_array):
            # Highlight current number
            self.play(input_squares[i].animate.set_fill(color=YELLOW, opacity=0.6))
            
            # Show query operation
            if i > 0:
                # Create query explanation
                query_explanation = VGroup(
                    Text("Query Operation:", font_size=24, color=YELLOW),
                    Text(f"Find max dp[] in range [0, {num}-1]", font_size=20),
                    Text(f"query(0, {num}-1)", font_size=20, color=GREEN)
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
                query_explanation.next_to(arrays_group, RIGHT, buff=0.5)
                
                # Show query range in segment tree
                st_idx = value_to_index[num]

                if st_idx > 0:
                    query_range = SurroundingRectangle(
                        VGroup(*st_squares[:st_idx]), 
                        color=GREEN, 
                        buff=0.2
                    )
                else: 
                    query_range = SurroundingRectangle(color=BLACK)
                self.play(
                    Write(query_explanation),
                    Create(query_range)
                )
                self.wait(0.5)
                
                # Show max value found
                max_val = max([int(n.text) for n in dp_nums[:st_idx]] or [0])
                max_text = Text(f"max = {max_val}", font_size=20, color=GREEN)
                max_text.next_to(query_explanation, DOWN, buff=0.5)
                
                self.play(Write(max_text))
                self.wait(0.5)
                
                # Calculate new dp value
                new_dp = max_val + 1
                dp_nums[i].text = str(new_dp)
                new_dp_text = Text(f"dp[i] = {new_dp}", font_size=20, color=GREEN)
                new_dp_text.next_to(max_text, DOWN, buff=0.2)
                
                self.play(Write(new_dp_text))
                self.wait(0.5)
                
                # Update dp array
                new_num = Text(str(new_dp), font_size=22)
                new_num.move_to(dp_nums[i])
                
                self.play(
                    Transform(dp_nums[i], new_num),
                    FadeOut(query_range),
                    FadeOut(query_explanation),
                    FadeOut(max_text),
                    FadeOut(new_dp_text)
                )
            else:
                # First element case
                new_num = Text("1", font_size=22)
                new_num.move_to(dp_nums[i])
                dp_nums[i].text = "1"
                
                first_text = Text("First element: dp[0] = 1", font_size=20, color=GREEN)
                first_text.next_to(dp_squares[i], DOWN, buff=0.2)
                
                self.play(
                    Transform(dp_nums[i], new_num),
                    Write(first_text)
                )
                self.wait(0.5)
                self.play(FadeOut(first_text))
            
            # Show update operation
            st_idx = value_to_index[num]
            update_explanation = VGroup(
                Text("Update Operation:", font_size=24, color=YELLOW),
                Text("Update segment tree with new dp[i]", font_size=20),
                Text(f"update({num}, {int(dp_nums[i].text)})", font_size=20, color=GREEN)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            update_explanation.next_to(arrays_group, RIGHT, buff=0.5)
            
            # Update segment tree
            new_st_num = Text(str(int(dp_nums[i].text)), font_size=22)
            new_st_num.move_to(st_nums[st_idx])
            
            self.play(
                Write(update_explanation),
                Transform(st_nums[st_idx], new_st_num)
            )
            self.wait(0.5)
            
            # Reset input highlight
            self.play(
                input_squares[i].animate.set_fill(color=BLUE_E, opacity=0.3),
                FadeOut(update_explanation)
            )
            self.wait(0.5)
        
        # Show final state
        final_text = Text("Final LIS length = max(dp[]) = 3", font_size=28, color=GREEN)
        final_text.next_to(arrays_group, DOWN, buff=1.0)
        self.play(Write(final_text))
        self.wait(1)