from manim import *


class CreateCircle(Scene):
    def construct(self):
        rectangle = Rectangle(width=5, height=1, color=WHITE)
        self.add(rectangle)
        self.wait(3)
        lines = VGroup(
            *[Line(start=[x, -0.5, 0], end=[x, 0.5, 0], color=WHITE)
              for x in [-1.5, -0.5, 0.5, 1.5]]  # Positions of the lines
        )
        self.play(Create(lines))
        self.wait(2)

        numbers = VGroup(
            *[
                MathTex(r"\mathbf{" + str(i) + "}").move_to([x, 0, 0])
                for i, x in enumerate([-2, -1, 0, 1, 2], start=1)
            ]
        )

        self.play(Create(numbers))
        self.wait(3)

        redNumbers = VGroup(
            *[
                MathTex(r"\mathbf{" + str(x[0]) + "}", color=RED).move_to([x[1], 0, 0])
                for i, x in enumerate([[2, -1], [5, 2]], start=1)
            ]
        )

        self.play(Create(redNumbers))
        self.wait(3)

        self.play(FadeOut(numbers[1]), FadeOut(numbers[4]))


        self.play(FadeOut(redNumbers))
        self.wait(1)

        transformedRedNumbers = VGroup(
            *[
                MathTex(r"\mathbf{" + str(x[0]) + "}", color=RED).move_to([x[1], 0, 0])
                for i, x in enumerate(([5, -1], [2, 2]), start=1)
            ]
        )

        self.play(Create(transformedRedNumbers))
        self.wait(3)
