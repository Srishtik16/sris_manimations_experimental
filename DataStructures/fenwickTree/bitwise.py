from manim import *

class BitwiseScene(Scene):
    def create_binary_number(self, num, label="", include_index=True):
        binary = format(num, '04b')
        
        # Create binary digits group
        digits = VGroup()
        for i, bit in enumerate(binary):
            # Create box
            box = Square(side_length=0.5, color=WHITE)
            # Create number
            number = Text(bit, font_size=20)
            number.move_to(box.get_center())
            # Create power of 2
            if include_index:
                power = Text(f"2^{3-i}", font_size=16, color=GRAY)
                power.next_to(box, DOWN, buff=0.1)
                digits.add(VGroup(box, number, power))
            else:
                digits.add(VGroup(box, number))
        
        digits.arrange(RIGHT, buff=0.1)
        
        # Add label if provided
        if label:
            label_text = Text(label, font_size=24, color=YELLOW)
            label_text.next_to(digits, LEFT, buff=0.3)
            return VGroup(label_text, digits)
        
        return digits
    
    def highlight_trailing_zeros(self, binary_group, color=RED):
        digits = binary_group[-1]  # Get the digits part
        highlighted = []
        
        # Start from the right (least significant bit)
        for digit in reversed(digits):
            if digit[1].text == "0":  # Check the Text object's content
                highlighted.append(
                    digit.animate.set_color(color)
                )
            else:
                break
                
        return highlighted
    
    def construct(self):
        title = Text("Understanding Bitwise Operations", color=BLUE, font_size=36)
        title.to_edge(UP, buff=0.3)
        
        self.play(Write(title))
        self.wait(0.5)
        
        # Example 1: i |= (i + 1) for update
        subtitle1 = Text("Update Operation: i |= (i + 1)", color=GREEN, font_size=28)
        subtitle1.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(subtitle1))
        self.wait(0.5)
        
        # Show example for i = 5
        i = 5
        i_binary = self.create_binary_number(i, "i = 5")
        i_plus_1 = self.create_binary_number(i + 1, "i + 1 = 6")
        i_result = self.create_binary_number(i | (i + 1), "Result = 7")
        
        example1 = VGroup(i_binary, i_plus_1, i_result)
        example1.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        example1.next_to(subtitle1, DOWN, buff=0.4)
        
        # Show initial number
        self.play(FadeIn(i_binary))
        self.wait(0.5)
        
        # Show i + 1
        self.play(FadeIn(i_plus_1))
        self.wait(0.5)
        
        # Highlight the bits that will be OR'ed
        explanation1 = Text(
            "OR operation sets the least significant zero to 1",
            font_size=20,
            color=YELLOW
        ).next_to(example1, DOWN, buff=0.3)
        
        self.play(Write(explanation1))
        self.wait(0.5)
        
        # Show result
        self.play(FadeIn(i_result))
        self.wait(1)
        
        # Clear first example
        self.play(
            FadeOut(VGroup(subtitle1, example1, explanation1))
        )
        self.wait(0.5)
        
        # Clear title for next scene
        self.play(FadeOut(title))
        self.wait(0.5)

class BitwiseScene2(Scene):
    def create_binary_number(self, num, label="", include_index=True):
        binary = format(num, '04b')
        
        # Create binary digits group
        digits = VGroup()
        for i, bit in enumerate(binary):
            # Create box
            box = Square(side_length=0.5, color=WHITE)
            # Create number
            number = Text(bit, font_size=20)
            number.move_to(box.get_center())
            # Create power of 2
            if include_index:
                power = Text(f"2^{3-i}", font_size=16, color=GRAY)
                power.next_to(box, DOWN, buff=0.1)
                digits.add(VGroup(box, number, power))
            else:
                digits.add(VGroup(box, number))
        
        digits.arrange(RIGHT, buff=0.1)
        
        # Add label if provided
        if label:
            label_text = Text(label, font_size=24, color=YELLOW)
            label_text.next_to(digits, LEFT, buff=0.3)
            return VGroup(label_text, digits)
        
        return digits
    
    def construct(self):
        title = Text("Understanding Bitwise Operations", color=BLUE, font_size=36)
        title.to_edge(UP, buff=0.3)
        
        self.play(Write(title))
        self.wait(0.5)
        
        # Example 2: (i & (i+1)) - 1 for query
        subtitle2 = Text("Query Operation: (i & (i+1)) - 1", color=RED, font_size=28)
        subtitle2.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(subtitle2))
        self.wait(0.5)
        
        # Show example for i = 5
        i = 5
        i_binary = self.create_binary_number(i, "i = 5")
        i_plus_1 = self.create_binary_number(i + 1, "i + 1 = 6")
        i_and = self.create_binary_number(i & (i + 1), "i & (i+1) = 4")
        i_result = self.create_binary_number((i & (i + 1)) - 1, "Result = 3")
        
        example2 = VGroup(i_binary, i_plus_1, i_and, i_result)
        example2.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        example2.next_to(subtitle2, DOWN, buff=0.4)
        
        # Show step by step
        self.play(FadeIn(i_binary))
        self.wait(0.5)
        
        self.play(FadeIn(i_plus_1))
        self.wait(0.5)
        
        explanation2 = Text(
            "AND with (i+1) removes the least significant 1",
            font_size=20,
            color=YELLOW
        ).next_to(example2, DOWN, buff=0.3)
        
        self.play(Write(explanation2))
        self.wait(0.5)
        
        self.play(FadeIn(i_and))
        self.wait(0.5)
        
        explanation3 = Text(
            "Subtracting 1 fills all bits after the removed 1",
            font_size=20,
            color=YELLOW
        ).next_to(explanation2, DOWN, buff=0.2)
        
        self.play(Write(explanation3))
        self.wait(0.5)
        
        self.play(FadeIn(i_result))
        self.wait(1)
        
        # Clear previous content for tree relationship
        self.play(
            FadeOut(VGroup(
                title, subtitle2, example2,
                explanation2, explanation3
            ))
        )
        self.wait(0.5)
        
        # Show tree relationship in center of screen
        new_title = Text("Tree Structure Relationship", color=BLUE, font_size=36)
        new_title.to_edge(UP, buff=1.0)
        
        # Create update operation text group
        update_group = VGroup(
            Text("• Update Operation (i |= i+1):", font_size=28, color=BLUE_B),
            Text("  Moves up to parent node in the tree", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Create query operation text group
        query_group = VGroup(
            Text("• Query Operation ((i & (i+1)) - 1):", font_size=28, color=RED_B),
            Text("  Jumps to previous complete subtree", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Combine all text with proper spacing
        tree_text = VGroup(update_group, query_group)
        tree_text.arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        
        explanation_group = VGroup(new_title, tree_text)
        explanation_group.arrange(DOWN, buff=0.8)
        explanation_group.move_to(ORIGIN)
        
        # Animate the tree relationship
        self.play(Write(new_title))
        self.wait(0.5)
        
        # Animate update operation first
        self.play(Write(update_group))
        self.wait(0.5)
        
        # Then animate query operation
        self.play(Write(query_group))
        self.wait(0.5)
        
        self.wait(2)
        
        # Clear everything
        self.play(FadeOut(explanation_group))
        self.wait(0.5) 