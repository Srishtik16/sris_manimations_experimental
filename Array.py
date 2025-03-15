from manim import *

class CreateArray(Scene) :
      def __init__(self, elements, **kwargs):
        super().__init__(**kwargs)
        self.elements = elements
      
      def construct(self): 
          elementsCnt = len(self.elements)
          print(elementsCnt)
          rectangle = Rectangle(width=elementsCnt, height=1, color=WHITE)
          self.add(rectangle)
          self.wait(3)
          self.play(Create(rectangle))
          self.wait(2)

          lines = VGroup(
              *[Line(start=[x + 1 if elementsCnt % 2 == 0 else x + 0.5, -0.5, 0], end=[x + 1 if elementsCnt % 2 == 0 else x + 0.5, 0.5, 0], color=WHITE)
                for x in range(-elementsCnt // 2, elementsCnt // 2, 1)]  # Positions of the lines
          )
          self.play(Create(lines))
          self.wait(2)

          numbers = VGroup(
              *[
                  MathTex(r"\mathbf{" + str(x) + "}").move_to([i + 0.5 if elementsCnt % 2 == 0 else i, 0, 0])
                  for i, x in enumerate((self.elements), start=-elementsCnt // 2)
              ]
          )

          self.play(Create(numbers))
          self.wait(3)