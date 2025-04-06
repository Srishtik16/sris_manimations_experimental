from manim import *

class VisualizationScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nums = [1, 7, 3, 0, 7, 8, 3, 2]
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
    
    def construct(self):
        # Create input array visualization
        input_array, input_boxes, input_numbers, input_indices, input_label = self.create_array_visualization(
            self.nums,
            color=BLUE,
            array_label="Input Array"
        )
        input_array.shift(UP * 2)
        
        # Create BIT array (initialized with zeros)
        bit_array, bit_boxes, bit_numbers, bit_indices, bit_label = self.create_array_visualization(
            [0] * len(self.nums),
            color=GREEN,
            array_label="Fenwick Tree (BIT[])"
        )
        bit_array.shift(DOWN * 1)
        
        # Animation sequence
        # 1. Show input array boxes with indices
        self.play(
            Create(input_boxes),
            Write(input_indices),
            Write(input_label)
        )
        self.wait(0.5)
        
        # 2. Fill in input array numbers with a wave effect
        for number in input_numbers:
            self.play(
                Write(number),
                run_time=0.25
            )
        self.wait(1)
        
        # 3. Show BIT array
        self.play(
            Create(bit_boxes),
            Write(bit_indices),
            Write(bit_label)
        )
        self.wait(0.5)
        
        # 4. Fill in BIT array with zeros
        for number in bit_numbers:
            self.play(
                Write(number),
                run_time=0.15
            )
        self.wait(2) 