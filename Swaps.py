from manim import *
from CustomArray import CreateArray

class SwapAnimation(CreateArray):
    def __init__(self, elements, swap_indices, **kwargs):
        super().__init__(elements, **kwargs)
        self.swap_indices = swap_indices  # tuple of (i, j) to swap
        
    def construct(self):
        # First use parent class to create the array
        super().construct()
        
        # Get indices to swap
        i, j = self.swap_indices
        first_num = self.numbers[i]  # Use self.numbers instead of getting from mobjects
        second_num = self.numbers[j]
        
        # Create index labels and arrows
        index_labels = VGroup()
        arrows = VGroup()
        
        for idx, num in [(i, first_num), (j, second_num)]:
            # Create index label
            label = MathTex(f"index_{idx}")
            label.next_to(num, UP, buff=1.2)
            
            # Create arrow pointing just outside the array boundary
            arrow = Arrow(
                start=label.get_bottom(),
                end=num.get_top() + UP * 0.1,  # Stop just outside the array boundary
                color=WHITE,
                buff=0.1
            )
            
            index_labels.add(label)
            arrows.add(arrow)
        
        # Show index labels and arrows
        self.play(
            Create(index_labels),
            Create(arrows)
        )
        self.wait(1)
        
        # Change numbers to red
        self.play(
            first_num.animate.set_color(RED),
            second_num.animate.set_color(RED)
        )
        self.wait(0.5)
        
        # Create copies for the arc animation
        first_num_copy = first_num.copy()
        second_num_copy = second_num.copy()
        
        # Calculate arc paths
        arc1 = ArcBetweenPoints(
            first_num.get_center(),
            second_num.get_center(),
            angle=-TAU/4
        )
        
        arc2 = ArcBetweenPoints(
            second_num.get_center(),
            first_num.get_center(),
            angle=TAU/4
        )
        
        # Add the copies to the scene
        self.add(first_num_copy, second_num_copy)
        
        # Fade out original numbers
        self.play(
            FadeOut(first_num),
            FadeOut(second_num)
        )
        
        # Animate the swap along arcs
        self.play(
            MoveAlongPath(first_num_copy, arc1),
            MoveAlongPath(second_num_copy, arc2),
            run_time=2,
            rate_func=smooth
        )
        
        # Update the array
        self.numbers[i] = second_num_copy
        self.numbers[j] = first_num_copy
        
        # Change numbers back to white
        self.play(
            second_num_copy.animate.set_color(WHITE),
            first_num_copy.animate.set_color(WHITE)
        )
        
        # Remove labels and arrows
        self.play(
            FadeOut(index_labels),
            FadeOut(arrows)
        )
        
        self.wait(2) 