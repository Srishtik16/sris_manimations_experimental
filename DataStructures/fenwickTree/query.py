from manim import *

class QueryScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nums = [1, 7, 3, 0, 7, 8, 3, 2]
        # Final BIT values after construction
        self.bit = [1, 8, 3, 11, 7, 15, 3, 31]
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
            angle=-PI/4  # Downward curve
        )
        return arrow
    
    def construct(self):
        # Create BIT array visualization
        bit_array, bit_boxes, bit_numbers, bit_indices, bit_label = self.create_array_visualization(
            self.bit,
            color=GREEN,
            array_label="Fenwick Tree (BIT[])"
        )
        bit_array.shift(UP * 1)
        
        # Create query title
        query_title = Text("Query: prefix_sum(5)", color=YELLOW, font_size=36)
        query_title.to_edge(UP, buff=0.5)
        
        # Create running sum display
        sum_text = Text("Running Sum: 0", font_size=32, color=WHITE)
        sum_text.to_edge(DOWN, buff=1)
        
        # Show initial state
        self.play(
            FadeIn(bit_array),
            Write(query_title)
        )
        self.wait(0.5)
        
        self.play(
            Write(sum_text)
        )
        self.wait(0.5)
        
        # Process prefix sum query
        r = 5
        total = 0
        
        while r >= 0:
            # Highlight current BIT position
            bit_box_copy = bit_boxes[r].copy()
            bit_box_copy.set_color(RED)
            
            # Show binary representation
            curr_binary = self.show_binary(r, bit_boxes[r].get_top() + UP * 1.5, BLUE)
            next_r = (r & (r + 1)) - 1
            if next_r >= 0:
                next_binary = self.show_binary(next_r, bit_boxes[next_r].get_top() + UP * 1.5, GREEN)
            
            # Create operation text
            operation = Text(f"Add BIT[{r}] = {self.bit[r]}", font_size=28, color=YELLOW)
            operation.next_to(bit_boxes[r], UP, buff=0.5)
            
            # Update total
            total += self.bit[r]
            new_sum_text = Text(f"Running Sum: {total}", font_size=32, color=WHITE)
            new_sum_text.move_to(sum_text.get_center())
            
            # Create and show update arrow if not last element
            if next_r >= 0:
                arrow = self.create_update_arrow(
                    bit_boxes[r].get_center(),
                    bit_boxes[next_r].get_center()
                )
            
            # Animate changes
            anims = [
                Transform(bit_boxes[r], bit_box_copy),
                Write(curr_binary),
                Write(operation),
                Transform(sum_text, new_sum_text)
            ]
            
            if next_r >= 0:
                anims.extend([
                    Write(next_binary),
                    Create(arrow)
                ])
            
            self.play(*anims)
            self.wait(1)
            
            # Clean up
            self.play(
                FadeOut(curr_binary),
                FadeOut(operation),
                bit_boxes[r].animate.set_color(GREEN)
            )
            if next_r >= 0:
                self.play(
                    FadeOut(next_binary),
                    FadeOut(arrow)
                )
            
            # Update r
            r = next_r
        
        # Show final result
        final_result = Text(f"Prefix Sum up to index 5: {total}", font_size=36, color=YELLOW)
        final_result.move_to(sum_text.get_center())
        
        self.play(
            Transform(sum_text, final_result)
        )
        self.wait(1)
        
        # Clear everything
        self.play(
            FadeOut(bit_array),
            FadeOut(query_title),
            FadeOut(sum_text)
        )
        self.wait(0.5)
        
        # Show Implementation
        heading = Text("Implementation", color=BLUE, font_size=40)
        heading.move_to(ORIGIN + UP * 2)
        
        code_text = """def prefix_sum(r):
    total = 0
    while r >= 0:
        total += bit[r]
        r = (r & (r + 1)) - 1  # Jump to next
    return total"""
        
        code = Code(
            code_string=code_text,
            language="python",
            background="window",
            tab_width=4
        )
        code.next_to(heading, DOWN, buff=0.8)
        
        self.play(
            Write(heading)
        )
        self.wait(0.5)
        
        self.play(
            FadeIn(code, shift=UP)
        )
        self.wait(2) 