from manim import *

class CreateArray(VGroup):
    def __init__(self, elements, color=WHITE, **kwargs):
        super().__init__(**kwargs)
        self.elements = elements
        self.color = color
        self.create_array()
    
    def create_array(self):
        elementsCnt = len(self.elements)
        
        # Create the main rectangle
        rectangle = Rectangle(width=elementsCnt, height=1, color=self.color)
        self.add(rectangle)
        
        # Calculate positions for lines
        line_positions = []
        for i in range(elementsCnt - 1):
            x_pos = -elementsCnt/2 + (i + 1)
            line_positions.append(x_pos)
        
        # Create dividing lines
        lines = VGroup(
            *[Line(start=[x, -0.5, 0], end=[x, 0.5, 0], color=self.color)
              for x in line_positions]
        )
        self.add(lines)
        
        # Add numbers
        numbers = VGroup()
        for i, element in enumerate(self.elements):
            x_pos = -elementsCnt/2 + i + 0.5  # Center in each cell
            number = Text(str(element), color=self.color, font_size=24)
            number.move_to([x_pos, 0, 0])
            numbers.add(number)
        self.add(numbers)
    
    def create_animation(self):
        return Create(self)