from manim import *
from CustomArray import CreateArray

class BinarySearchAnimation(CreateArray):
    def __init__(self, elements, search_key, **kwargs):
        # Sort the elements first since binary search needs sorted array
        self.original_elements = elements.copy()
        self.sorted_elements = sorted(elements)
        self.search_key = search_key
        super().__init__(self.original_elements, **kwargs)

    def construct(self):
        # First create the array using parent class
        super().construct()
        self.wait(1)

        # Add title for sorting phase
        sort_title = Text("Sorting the Array", font_size=36)
        sort_title.to_edge(UP)
        self.play(Write(sort_title))
        self.wait(1)

        # Animate sorting
        self.animate_sorting()
        self.wait(1)

        # Remove sorting title and add binary search title
        search_title = Text("Binary Search", font_size=36)
        search_title.to_edge(UP)
        self.play(
            FadeOut(sort_title),
            Write(search_title)
        )
        self.wait(1)

        # Add search key information
        key_info = Text(f"Searching for: {self.search_key}", font_size=24)
        key_info.next_to(search_title, DOWN)
        self.play(Write(key_info))
        self.wait(1)

        # Perform binary search animation
        self.animate_binary_search()
        self.wait(2)

    def animate_sorting(self):
        # Bubble sort with animation
        n = len(self.original_elements)
        array_copy = self.original_elements.copy()
        
        for i in range(n):
            for j in range(0, n-i-1):
                # Highlight current comparison
                first = self.numbers[j]
                second = self.numbers[j+1]
                
                # Create highlighting rectangles
                highlight1 = SurroundingRectangle(first, color=YELLOW)
                highlight2 = SurroundingRectangle(second, color=YELLOW)
                
                self.play(
                    Create(highlight1),
                    Create(highlight2),
                    run_time=0.5
                )
                
                if array_copy[j] > array_copy[j+1]:
                    # Swap animation
                    self.play(
                        first.animate.set_color(RED),
                        second.animate.set_color(RED)
                    )
                    
                    # Swap the numbers with arc animation
                    arc1 = ArcBetweenPoints(
                        first.get_center(),
                        second.get_center(),
                        angle=-TAU/4
                    )
                    arc2 = ArcBetweenPoints(
                        second.get_center(),
                        first.get_center(),
                        angle=TAU/4
                    )
                    
                    first_copy = first.copy()
                    second_copy = second.copy()
                    self.add(first_copy, second_copy)
                    
                    self.play(
                        FadeOut(first),
                        FadeOut(second)
                    )
                    
                    self.play(
                        MoveAlongPath(first_copy, arc1),
                        MoveAlongPath(second_copy, arc2),
                        run_time=1
                    )
                    
                    # Update array and mobjects
                    array_copy[j], array_copy[j+1] = array_copy[j+1], array_copy[j]
                    self.numbers[j] = second_copy
                    self.numbers[j+1] = first_copy
                    
                    self.play(
                        first_copy.animate.set_color(WHITE),
                        second_copy.animate.set_color(WHITE)
                    )
                
                self.play(
                    FadeOut(highlight1),
                    FadeOut(highlight2)
                )

    def animate_binary_search(self):
        left = 0
        right = len(self.sorted_elements) - 1
        found = False
        
        # Create pointers with correct directions
        left_arrow = Arrow(start=UP, end=DOWN, color=BLUE)  # Points downward
        right_arrow = Arrow(start=UP, end=DOWN, color=BLUE)  # Points downward
        mid_arrow = Arrow(start=DOWN, end=UP, color=GREEN)   # Points upward
        
        # Add labels
        left_label = Text("L", font_size=24, color=BLUE)
        right_label = Text("R", font_size=24, color=BLUE)
        mid_label = Text("M", font_size=24, color=GREEN)
        
        while left <= right and not found:
            mid = (left + right) // 2
            
            # Position arrows and labels
            for arrow, label, idx, is_mid in [
                (left_arrow, left_label, left, False),
                (right_arrow, right_label, right, False),
                (mid_arrow, mid_label, mid, True)
            ]:
                pos = self.numbers[idx].get_center()
                if is_mid:
                    # Position mid arrow below the number
                    arrow.next_to(self.numbers[idx], DOWN, buff=0.3)
                    label.next_to(arrow, DOWN, buff=0.1)
                else:
                    # Position L/R arrows above the number
                    arrow.next_to(self.numbers[idx], UP, buff=0.3)
                    label.next_to(arrow, UP, buff=0.1)
                
                self.play(
                    Create(arrow),
                    Write(label),
                    run_time=0.5
                )
            
            # Highlight current element
            current = self.numbers[mid]
            highlight = SurroundingRectangle(current, color=YELLOW)
            self.play(Create(highlight))
            self.wait(0.5)
            
            if self.sorted_elements[mid] == self.search_key:
                # Found the key
                self.play(
                    current.animate.set_color(GREEN),
                    Flash(current, color=GREEN, line_length=0.3)
                )
                found = True
            elif self.sorted_elements[mid] < self.search_key:
                # Move left pointer
                left = mid + 1
                self.play(
                    current.animate.set_color(RED),
                    FadeOut(left_arrow),
                    FadeOut(left_label)
                )
            else:
                # Move right pointer
                right = mid - 1
                self.play(
                    current.animate.set_color(RED),
                    FadeOut(right_arrow),
                    FadeOut(right_label)
                )
            
            # Clean up for next iteration
            self.play(
                FadeOut(highlight),
                FadeOut(mid_arrow),
                FadeOut(mid_label)
            )
            
            if not found and left > right:
                # Key not found
                not_found_text = Text("Key not found!", color=RED)
                not_found_text.to_edge(DOWN)
                self.play(Write(not_found_text)) 