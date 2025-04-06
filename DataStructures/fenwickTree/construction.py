from manim import *

class ConstructionScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nums = [1, 7, 3, 0, 7, 8, 3, 2]
        self.bit = [0] * len(self.nums)
        self.box_width = 0.8
        self.box_height = 0.8
        
    def create_array_visualization(self, values, color=WHITE, with_indices=True, array_label=""):
        boxes = VGroup()
        numbers = VGroup()
        indices = VGroup() if with_indices else None
        n = len(values)
        
        # Create array label
        label = Text(array_label, font_size=32, color=BLUE).next_to(boxes, UP, buff=0.5)
        
        # Create boxes, numbers, and indices
        for i in range(n):
            # Box
            box = Square(side_length=self.box_width, color=color)
            box.move_to([i * (self.box_width + 0.2), 0, 0])
            boxes.add(box)
            
            # Number
            number = Text(str(values[i]), font_size=24)
            number.move_to(box.get_center())
            numbers.add(number)
            
            # Index
            if with_indices:
                index = Text(str(i), font_size=20, color=GRAY)
                index.next_to(box, DOWN, buff=0.2)
                indices.add(index)
        
        # Center the entire array
        array_group = VGroup(boxes, numbers)
        if with_indices:
            array_group.add(indices)
        array_group.add(label)
        array_group.move_to(ORIGIN)
        
        return array_group, boxes, numbers, indices, label
    
    def show_binary(self, num, pos, color=WHITE):
        binary = format(num, '04b')
        binary_text = Text(f"Binary: {binary}", font_size=24, color=color)
        binary_text.move_to(pos)
        return binary_text
    
    def create_update_arrow(self, start, end, color=YELLOW):
        arrow = CurvedArrow(
            start_point=start,
            end_point=end,
            color=color,
            angle=PI/4  # Using PI/4 for a gentler curve
        )
        return arrow
    
    def construct(self):
        # Create input array visualization
        input_array, input_boxes, input_numbers, input_indices, input_label = self.create_array_visualization(
            self.nums,
            color=BLUE,
            array_label="Input Array"
        )
        input_array.shift(UP * 2)
        
        # Create BIT array visualization
        bit_array, bit_boxes, bit_numbers, bit_indices, bit_label = self.create_array_visualization(
            self.bit,
            color=GREEN,
            array_label="Fenwick Tree (BIT[])"
        )
        bit_array.shift(DOWN * 1)
        
        # Create bitwise operation explanation
        bitwise_title = Text("Understanding i |= (i + 1)", color=YELLOW, font_size=32)
        bitwise_title.to_edge(UP, buff=0.5)
        
        example_i = 3  # Using 3 as an example
        example_text = VGroup(
            Text(f"For i = {example_i}:", color=WHITE, font_size=28),
            Text(f"Binary(i)     = {format(example_i, '04b')}", color=BLUE, font_size=28),
            Text(f"Binary(i + 1)  = {format(example_i + 1, '04b')}", color=GREEN, font_size=28),
            Text(f"Binary(result) = {format(example_i | (example_i + 1), '04b')}", color=RED, font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        example_text.next_to(bitwise_title, DOWN, buff=0.8)
        
        # Show bitwise operation explanation
        self.play(Write(bitwise_title))
        self.wait(0.5)
        
        for text in example_text:
            self.play(Write(text))
            self.wait(0.5)
        
        self.wait(1)
        
        # Clear bitwise explanation
        self.play(
            FadeOut(bitwise_title),
            FadeOut(example_text)
        )
        self.wait(0.5)
        
        # Show initial arrays
        self.play(
            FadeIn(input_array),
            FadeIn(bit_array)
        )
        
        # Create status text
        status = Text("", font_size=28, color=YELLOW)
        status.to_edge(UP, buff=0.5)
        
        # Process each number in the input array
        for i, num in enumerate(self.nums):
            # Highlight current input number
            input_box_copy = input_boxes[i].copy()
            input_box_copy.set_color(YELLOW)
            
            # Show status
            status_text = f"Processing nums[{i}] = {num}"
            status.become(Text(status_text, font_size=28, color=YELLOW).to_edge(UP, buff=0.5))
            
            self.play(
                Transform(input_boxes[i], input_box_copy),
                Write(status)
            )
            self.wait(0.5)
            
            # Update BIT
            idx = i
            while idx < len(self.nums):
                # Highlight current BIT position
                bit_box_copy = bit_boxes[idx].copy()
                bit_box_copy.set_color(RED)
                
                # Show binary representation
                curr_binary = self.show_binary(idx, bit_boxes[idx].get_bottom() + DOWN * 1.5, BLUE)
                next_idx = idx | (idx + 1)
                if next_idx < len(self.nums):
                    next_binary = self.show_binary(next_idx, bit_boxes[next_idx].get_bottom() + DOWN * 1.5, GREEN)
                
                # Create and show update arrow
                if next_idx < len(self.nums):
                    arrow = self.create_update_arrow(
                        bit_boxes[idx].get_center(),
                        bit_boxes[next_idx].get_center()
                    )
                
                # Update BIT value
                self.bit[idx] += num
                new_number = Text(str(self.bit[idx]), font_size=24)
                new_number.move_to(bit_numbers[idx].get_center())
                
                # Animate changes
                anims = [
                    Transform(bit_boxes[idx], bit_box_copy),
                    Transform(bit_numbers[idx], new_number),
                    Write(curr_binary)
                ]
                
                if next_idx < len(self.nums):
                    anims.extend([
                        Write(next_binary),
                        Create(arrow)
                    ])
                
                self.play(*anims)
                self.wait(0.5)
                
                # Clean up
                self.play(
                    FadeOut(curr_binary),
                    bit_boxes[idx].animate.set_color(GREEN)
                )
                if next_idx < len(self.nums):
                    self.play(
                        FadeOut(next_binary),
                        FadeOut(arrow)
                    )
                
                # Update index
                idx = next_idx
            
            # Reset input box color
            self.play(
                input_boxes[i].animate.set_color(BLUE)
            )
            self.wait(0.5)
        
        # Clear everything
        self.play(
            FadeOut(input_array),
            FadeOut(bit_array),
            FadeOut(status)
        )
        self.wait(1)
        
        # Create and show Implementation heading
        heading = Text("Implementation", color=BLUE, font_size=40)
        heading.move_to(ORIGIN + UP * 2)
        
        # Create pseudocode panel
        code_text = """def add(i, delta):
    while i < n:
        bit[i] += delta
        i |= i + 1  # i = i | (i + 1)"""
        code = Code(
            code_string=code_text,
            language="python",
            background="window",
            tab_width=4
        )
        code.next_to(heading, DOWN, buff=0.8)
        
        # Show heading and code
        self.play(
            Write(heading)
        )
        self.wait(0.5)
        
        self.play(
            FadeIn(code, shift=UP)
        )
        self.wait(2) 