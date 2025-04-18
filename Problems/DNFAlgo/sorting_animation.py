from manim import *

class DNFSortingScene(Scene):
    def construct(self):
        # Title
        title = Text("Dutch National Flag Sorting", font_size=36)
        title.to_edge(UP, buff=0.5)
        
        # Initial array [2, 0, 2, 1, 1, 0]
        nums = [2, 0, 2, 1, 1, 0]
        n = len(nums)
        
        # Colors for numbers
        colors = {0: BLUE, 1: WHITE, 2: RED}
        
        # Create array squares
        squares = VGroup()
        numbers = VGroup()
        indices = VGroup()
        
        # Create array visualization (including position 6 for high pointer)
        for i in range(n + 1):
            # Create square
            square = Square(side_length=1)
            if i < n:  # Only color and fill actual array elements
                square.set_fill(colors[nums[i]], opacity=0.5)
                square.set_stroke(WHITE, 2)
                # Number
                num = Text(str(nums[i]), font_size=24)
                num.set_color(BLACK if nums[i] == 1 else WHITE)
            else:  # Position 6 is invisible
                square.set_fill(opacity=0)
                square.set_stroke(opacity=0)
                num = Text("", font_size=24)
            
            # Index below
            index = Text(str(i), font_size=20, color=WHITE)
            
            # Position elements
            square.shift(RIGHT * (i - n/2) * 1.5)  # Center the array
            num.move_to(square.get_center())
            index.next_to(square, DOWN, buff=0.3)
            
            squares.add(square)
            numbers.add(num)
            indices.add(index)
        
        # Create pointers
        def create_pointer(index, color, name):
            arrow = Arrow(
                start=squares[index].get_bottom() + DOWN * 0.8,
                end=squares[index].get_bottom() + DOWN * 0.3,
                color=color,
                buff=0
            )
            label = Text(f"{name}={index}", font_size=20, color=color)
            label.next_to(arrow, DOWN, buff=0.1)
            return VGroup(arrow, label)
        
        # Initial pointer positions
        low = create_pointer(0, GREEN, "low")
        mid = create_pointer(0, YELLOW, "mid")
        high = create_pointer(5, RED, "high")  # Start at position 5
        
        # Status text
        status = Text("Initial array", font_size=24)
        status.next_to(title, DOWN, buff=0.5)
        
        # Show initial setup
        self.play(Write(title), Write(status))
        self.play(
            *[Create(square) for square in squares[:n]],  # Don't show position 6
            *[Write(num) for num in numbers[:n]],
            *[Write(idx) for idx in indices],
            Create(low), Create(mid), Create(high)
        )
        self.wait()
        
        def update_pointer(pointer, new_index, name):
            new_arrow = Arrow(
                start=squares[new_index].get_bottom() + DOWN * 0.8,
                end=squares[new_index].get_bottom() + DOWN * 0.3,
                color=pointer[0].get_color(),
                buff=0
            )
            new_label = Text(f"{name}={new_index}", font_size=20, color=pointer[0].get_color())
            new_label.next_to(new_arrow, DOWN, buff=0.1)
            return self.play(
                Transform(pointer[0], new_arrow),
                Transform(pointer[1], new_label)
            )
            
        def swap_elements(i, j):
            # Swap in array
            nums[i], nums[j] = nums[j], nums[i]
            
            # Create swap arrow
            arrow = Arrow(squares[i].get_center(), squares[j].get_center(), color=YELLOW)
            
            # Animate swap
            self.play(Create(arrow))
            self.play(
                numbers[i].animate.become(
                    Text(str(nums[i]), font_size=24, color=BLACK if nums[i] == 1 else WHITE)
                    .move_to(squares[i].get_center())
                ),
                squares[i].animate.set_fill(colors[nums[i]], opacity=0.5),
                numbers[j].animate.become(
                    Text(str(nums[j]), font_size=24, color=BLACK if nums[j] == 1 else WHITE)
                    .move_to(squares[j].get_center())
                ),
                squares[j].animate.set_fill(colors[nums[j]], opacity=0.5)
            )
            self.play(FadeOut(arrow))
        
        # Step 1
        self.play(status.animate.become(Text("Step 1: nums[mid] = 2, swap with high", font_size=24).next_to(title, DOWN, buff=0.5)))
        swap_elements(0, 5)
        update_pointer(high, 4, "high")
        self.wait()
        
        # Step 2
        self.play(status.animate.become(Text("Step 2: nums[mid] = 0, self-swap at low", font_size=24).next_to(title, DOWN, buff=0.5)))
        update_pointer(low, 1, "low")
        update_pointer(mid, 1, "mid")
        self.wait()
        
        # Step 3
        self.play(status.animate.become(Text("Step 3: nums[mid] = 0, self-swap at low", font_size=24).next_to(title, DOWN, buff=0.5)))
        update_pointer(low, 2, "low")
        update_pointer(mid, 2, "mid")
        self.wait()
        
        # Step 4
        self.play(status.animate.become(Text("Step 4: nums[mid] = 2, swap with high", font_size=24).next_to(title, DOWN, buff=0.5)))
        swap_elements(2, 4)
        update_pointer(high, 3, "high")
        self.wait()
        
        # Step 5
        self.play(status.animate.become(Text("Step 5: nums[mid] = 1, increment mid", font_size=24).next_to(title, DOWN, buff=0.5)))
        update_pointer(mid, 3, "mid")
        self.wait()
        
        # Step 6
        self.play(status.animate.become(Text("Step 6: nums[mid] = 1, increment mid", font_size=24).next_to(title, DOWN, buff=0.5)))
        update_pointer(mid, 4, "mid")
        self.wait()
        
        # Exit condition
        self.play(status.animate.become(Text("Exit: mid(4) > high(3), sorting complete!", font_size=24).next_to(title, DOWN, buff=0.5)))
        self.wait(2)
        
        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        ) 