from manim import *

class GridSetupScene(Scene):
    def construct(self):
        # Create 8x8 grid
        grid = NumberPlane(
            x_range=(1, 9, 1),
            y_range=(1, 9, 1),
            x_length=8,
            y_length=8,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
            }
        )
        grid.scale(0.7)
        grid.to_edge(UP, buff=1.0)
        
        # Add axis labels
        x_labels = VGroup()
        y_labels = VGroup()
        for i in range(1, 9):
            x_label = Text(str(i), font_size=20).next_to(grid.c2p(i, 1), DOWN, buff=0.1)
            y_label = Text(str(i), font_size=20).next_to(grid.c2p(1, i), LEFT, buff=0.1)
            x_labels.add(x_label)
            y_labels.add(y_label)
        
        # Highlight lattice points
        lattice_points = VGroup()
        for x in range(1, 9):
            for y in range(1, 9):
                point = Dot(grid.c2p(x, y), color=WHITE, radius=0.05)
                lattice_points.add(point)
        
        # Add explanation text
        explanation = Text(
            "Only points at these intersections are allowed",
            font_size=24,
            color=YELLOW
        )
        explanation.next_to(grid, DOWN, buff=0.5)
        
        # Create a semi-transparent background for non-lattice regions
        background = Rectangle(
            width=grid.width + 0.5,
            height=grid.height + 0.5,
            fill_opacity=0.2,
            fill_color=BLACK,
            stroke_width=0
        )
        background.move_to(grid)
        
        # Animations
        self.play(Create(grid))
        self.play(Write(x_labels), Write(y_labels))
        self.play(Create(lattice_points))
        self.play(FadeIn(background))
        self.play(Write(explanation))
        self.wait(2)
        
        # Clear the scene
        self.play(
            FadeOut(grid),
            FadeOut(x_labels),
            FadeOut(y_labels),
            FadeOut(lattice_points),
            FadeOut(background),
            FadeOut(explanation)
        ) 