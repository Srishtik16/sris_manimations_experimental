from manim import *

class CreateArray(Scene):
    def __init__(self, elements, **kwargs):
        super().__init__(**kwargs)
        self.elements = elements
      
    def construct(self): 
        elementsCnt = len(self.elements)
        print(elementsCnt)
        rectangle = Rectangle(width=elementsCnt, height=1, color=WHITE)
        self.play(Create(rectangle))
        self.wait(2)

        # Calculate positions for lines
        line_positions = []
        for i in range(elementsCnt - 1):
            x_pos = -elementsCnt/2 + (i + 1)
            line_positions.append(x_pos)

        # Create dividing lines
        lines = VGroup(
            *[Line(start=[x, -0.5, 0], end=[x, 0.5, 0], color=WHITE)
              for x in line_positions]
        )
        self.play(Create(lines))
        self.wait(2)

        # Create numbers with proper positioning
        self.numbers = VGroup()  # Store as instance variable
        for i, num in enumerate(self.elements):
            x_pos = -elementsCnt/2 + i + 0.5  # Position at the center of each cell
            number = MathTex(r"\mathbf{" + str(num) + "}")
            number.move_to([x_pos, 0, 0])
            self.numbers.add(number)

        self.play(Create(self.numbers))
        self.wait(3)