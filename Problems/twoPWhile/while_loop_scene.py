from manim import *

class WhileLoopScene(Scene):
    def construct(self):
        # Title
        title = Text("Two Pointer Execution", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.3)
        
        # Input string
        s = "abcabcbb"
        
        # Create array visualization
        squares = VGroup(*[
            Square(side_length=0.8).set_stroke(color=BLUE).set_fill(color=BLUE_E, opacity=0.2)
            for _ in s
        ]).arrange(RIGHT, buff=0.1)
        
        # Add characters
        chars = VGroup(*[
            Text(char, font_size=30) for char in s
        ])
        for char, square in zip(chars, squares):
            char.move_to(square.get_center())
        
        # Add indices
        indices = VGroup(*[
            Text(str(i), font_size=24).next_to(square, DOWN, buff=0.3)
            for i, square in enumerate(squares)
        ])
        
        # Group array elements
        array_group = VGroup(squares, chars, indices)
        array_group.next_to(title, DOWN, buff=0.8)
        
        # MaxLen counter
        max_len = 0
        max_len_text = Text(f"maxLen = {max_len}", font_size=32, color=YELLOW)
        max_len_text.to_edge(UP + RIGHT, buff=0.5)
        
        # Create seen set display
        seen_text = Text("seen = {", font_size=28, color=BLUE).to_edge(LEFT, buff=1)
        seen_brace = Text("}", font_size=28, color=BLUE)
        seen_brace.next_to(seen_text, RIGHT, buff=2)
        seen_elements = VGroup()
        
        seen_group = VGroup(seen_text, seen_brace)
        seen_group.next_to(array_group, DOWN, buff=2.0)
        
        # Create pointers
        pointer_l = Arrow(start=DOWN, end=UP, color=YELLOW, max_tip_length_to_length_ratio=0.2)
        pointer_r = Arrow(start=DOWN, end=UP, color=GREEN, max_tip_length_to_length_ratio=0.2)
        label_l = Text("l", font_size=24, color=YELLOW)
        label_r = Text("r", font_size=24, color=GREEN)
        
        # Initial pointer positions
        l, r = 0, 0
        pointer_l.next_to(squares[l], DOWN, buff=0.1)
        pointer_r.next_to(squares[r], DOWN, buff=0.1)
        label_l.next_to(pointer_l, DOWN, buff=0.1)
        label_r.next_to(pointer_r, DOWN, buff=0.1)
        
        pointer_group_l = VGroup(pointer_l, label_l)
        pointer_group_r = VGroup(pointer_r, label_r)
        
        # Show initial setup
        self.play(
            Write(title),
            Write(max_len_text)
        )
        
        # Show array
        self.play(
            Create(squares),
            Write(chars),
            Write(indices)
        )
        self.wait(0.5)
        
        # Show seen set
        self.play(Write(seen_group))
        self.wait(0.5)
        
        # Show pointers
        self.play(
            Create(pointer_group_l),
            Create(pointer_group_r)
        )
        self.wait(0.5)
        
        # Execute the algorithm
        seen = set()
        max_len = 0
        n = len(s)
        
        while r < n:
            # Highlight current character
            current_square = squares[r].copy().set_fill(color=YELLOW, opacity=0.3)
            self.play(FadeIn(current_square))
            
            if s[r] not in seen:
                # Add to seen set
                new_char = Text(s[r], font_size=28, color=WHITE)
                if len(seen_elements) == 0:
                    new_char.next_to(seen_text, RIGHT, buff=0.2)
                else:
                    new_char.next_to(seen_elements[-1], RIGHT, buff=0.2)
                seen_elements.add(new_char)
                
                self.play(Write(new_char))
                seen.add(s[r])
                
                # Update maxLen
                max_len = max(max_len, r - l + 1)
                new_max_text = Text(f"maxLen = {max_len}", font_size=32, color=YELLOW)
                new_max_text.move_to(max_len_text)
                self.play(
                    FadeOut(max_len_text),
                    FadeIn(new_max_text)
                )
                max_len_text = new_max_text
                
                # Move r pointer
                r += 1
                if r < n:
                    self.play(
                        pointer_group_r.animate.next_to(squares[r], DOWN, buff=0.1)
                    )
            else:
                # Remove from seen set
                to_remove = None
                for elem in seen_elements:
                    if elem.text == s[l]:
                        to_remove = elem
                        break
                
                if to_remove:
                    seen_elements.remove(to_remove)
                    self.play(FadeOut(to_remove))
                    
                    # Rearrange remaining elements
                    if len(seen_elements) > 0:
                        self.play(
                            *[elem.animate.next_to(
                                seen_text if i == 0 else seen_elements[i-1],
                                RIGHT, buff=0.2
                            ) for i, elem in enumerate(seen_elements)]
                        )
                
                seen.remove(s[l])
                l += 1
                self.play(
                    pointer_group_l.animate.next_to(squares[l], DOWN, buff=0.1)
                )
            
            self.play(FadeOut(current_square))
            self.wait(0.3)
        
        # Show final result
        result_text = Text(f"Longest substring without repeating characters: {max_len}",
                         font_size=32, color=GREEN)
        result_text.next_to(seen_group, DOWN, buff=1.0)
        self.play(Write(result_text))
        self.wait(2) 