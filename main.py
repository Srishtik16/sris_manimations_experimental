from manim import *
from CustomArray import CreateArray
from BinarySearch import BinarySearchAnimation
import os


class MainScene(BinarySearchAnimation):
    def __init__(self, **kwargs):
        # Get array and search key from environment variables
        array_str = os.getenv('ARRAY', '6,2,7,1,3,8,4')
        search_key = int(os.getenv('KEY', '3'))  # Default search key is 3
        
        try:
            elements = [int(x.strip()) for x in array_str.split(',')]
        except ValueError:
            print("Error: Please provide numbers separated by commas (e.g., '6,2,7,1,3,8,4')")
            elements = [6,2,7,1,3,8,4]  # fallback to default
            
        super().__init__(elements, search_key, **kwargs)

    def construct(self):
        super().construct()


if __name__ == "__main__":
    scene = MainScene()
    scene.render()


# class CreateCircle(Scene):
#     def construct(self):
#         rectangle = Rectangle(width=5, height=1, color=WHITE)
#         self.add(rectangle)
#         self.wait(3)
#         lines = VGroup(
#             *[Line(start=[x, -0.5, 0], end=[x, 0.5, 0], color=WHITE)
#               for x in [-1.5, -0.5, 0.5, 1.5]]  # Positions of the lines
#         )
#         self.play(Create(lines))
#         self.wait(2)

#         numbers = VGroup(
#             *[
#                 MathTex(r"\mathbf{" + str(i) + "}").move_to([x, 0, 0])
#                 for i, x in enumerate([-2, -1, 0, 1, 2], start=1)
#             ]
#         )

#         self.play(Create(numbers))
#         self.wait(3)

#         redNumbers = VGroup(
#             *[
#                 MathTex(r"\mathbf{" + str(x[0]) + "}", color=RED).move_to([x[1], 0, 0])
#                 for i, x in enumerate([[2, -1], [5, 2]], start=1)
#             ]
#         )

#         self.play(Create(redNumbers))
#         self.wait(3)

#         self.play(FadeOut(numbers[1]), FadeOut(numbers[4]))


#         self.play(FadeOut(redNumbers))
#         self.wait(1)

#         transformedRedNumbers = VGroup(
#             *[
#                 MathTex(r"\mathbf{" + str(x[0]) + "}", color=RED).move_to([x[1], 0, 0])
#                 for i, x in enumerate(([5, -1], [2, 2]), start=1)
#             ]
#         )

#         self.play(Create(transformedRedNumbers))
#         self.wait(3)
