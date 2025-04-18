from manim import *

class PointerSetupScene(Scene):
    def construct(self):
        # Title
        title = Text("3-Pointer Setup", font_size=36)
        title.to_edge(UP, buff=0.3)
        
        # Input array
        nums = [2, 0, 2, 1, 1, 0]
        n = len(nums)
        
        # Create boxes and labels
        boxes = VGroup()
        num_labels = VGroup()
        index_labels = VGroup()
        
        # Colors for numbers
        colors = {
            0: BLUE,    # Blue for 0
            1: WHITE,   # White for 1
            2: RED      # Red for 2
        }
        
        # Create boxes and labels
        for i, num in enumerate(nums):
            # Create box
            box = Square(
                side_length=1,
                color=colors[num],
                fill_opacity=0.5,
                stroke_width=2
            )
            
            # Create number label
            num_label = Text(
                str(num),
                font_size=24,
                color=BLACK if num == 1 else WHITE
            )
            num_label.move_to(box.get_center())
            
            # Create index label
            index_label = Text(
                str(i),
                font_size=20,
                color=WHITE
            )
            index_label.next_to(box, DOWN, buff=0.2)
            
            # Position box
            box.shift(RIGHT * i * 1.2)
            num_label.shift(RIGHT * i * 1.2)
            index_label.shift(RIGHT * i * 1.2)
            
            boxes.add(box)
            num_labels.add(num_label)
            index_labels.add(index_label)
        
        # Center the group
        boxes_group = VGroup(boxes, num_labels, index_labels)
        boxes_group.center()
        boxes_group.shift(DOWN * 0.5)
        
        # Create pointers
        low_arrow = Arrow(
            start=boxes[0].get_bottom() + DOWN * 0.5,
            end=boxes[0].get_bottom(),
            color=GREEN
        )
        low_label = Text("low = 0", font_size=20, color=GREEN)
        low_label.next_to(low_arrow, DOWN, buff=0.2)
        
        mid_arrow = Arrow(
            start=boxes[0].get_bottom() + DOWN * 0.5,
            end=boxes[0].get_bottom(),
            color=YELLOW
        )
        mid_label = Text("mid = 0", font_size=20, color=YELLOW)
        mid_label.next_to(mid_arrow, DOWN, buff=0.2)
        
        high_arrow = Arrow(
            start=boxes[-1].get_bottom() + DOWN * 0.5,
            end=boxes[-1].get_bottom(),
            color=RED
        )
        high_label = Text(f"high = {n-1}", font_size=20, color=RED)
        high_label.next_to(high_arrow, DOWN, buff=0.2)
        
        # Create region rectangles
        unknown_rect = Rectangle(
            width=n * 1.2,
            height=1.2,
            color=GRAY,
            fill_opacity=0.2,
            stroke_width=2
        )
        unknown_rect.move_to(boxes_group.get_center())
        
        # Create region labels with better positioning
        region_labels = VGroup()
        
        # Create "2s" label at top
        twos_label = Text("2s [6, 5]", font_size=20, color=RED)
        twos_label.to_edge(UP, buff=1.2)
        
        # Create "1s" label below "2s"
        ones_label = Text("1s [0, -1]", font_size=20, color=WHITE)
        ones_label.next_to(twos_label, DOWN, buff=0.3)
        
        # Create "unknown" label
        unknown_label = Text("unknown [0, 5]", font_size=20, color=GRAY)
        unknown_label.next_to(unknown_rect, UP, buff=0.2)
        
        region_labels.add(twos_label, ones_label, unknown_label)
        
        # Create helper text
        helper_text = Text(
            "Initial Setup: All elements are in unknown region [0, n-1]",
            font_size=20
        )
        helper_text.next_to(title, DOWN, buff=0.3)
        
        # Animations
        self.play(Write(title))
        self.wait(0.5)
        
        # Show boxes and labels
        self.play(
            LaggedStart(
                *[FadeIn(box) for box in boxes],
                lag_ratio=0.2
            ),
            run_time=1.5
        )
        
        self.play(
            LaggedStart(
                *[Write(label) for label in num_labels],
                lag_ratio=0.2
            ),
            run_time=1.5
        )
        
        self.play(
            LaggedStart(
                *[Write(label) for label in index_labels],
                lag_ratio=0.2
            ),
            run_time=1.5
        )
        
        # Show helper text
        self.play(Write(helper_text))
        self.wait(0.5)
        
        # Show pointers
        self.play(
            Create(low_arrow),
            Write(low_label),
            run_time=0.5
        )
        self.play(
            Create(mid_arrow),
            Write(mid_label),
            run_time=0.5
        )
        self.play(
            Create(high_arrow),
            Write(high_label),
            run_time=0.5
        )
        
        # Fade out helper text before showing regions
        self.play(FadeOut(helper_text))
        
        # Show regions
        self.play(Create(unknown_rect))
        self.play(
            LaggedStart(
                Write(twos_label),
                Write(ones_label),
                Write(unknown_label),
                lag_ratio=0.3
            )
        )
        
        self.wait(2)
        
        # Clear the scene
        self.play(
            FadeOut(title),
            FadeOut(boxes),
            FadeOut(num_labels),
            FadeOut(index_labels),
            FadeOut(low_arrow),
            FadeOut(low_label),
            FadeOut(mid_arrow),
            FadeOut(mid_label),
            FadeOut(high_arrow),
            FadeOut(high_label),
            FadeOut(unknown_rect),
            FadeOut(region_labels)
        )

class SortingProcessScene(Scene):
    def construct(self):
        # Title
        title = Text("Step-by-Step Sorting Process", font_size=36)
        title.to_edge(UP, buff=0.3)
        
        # Input array and pointers
        nums = [2, 0, 2, 1, 1, 0]
        n = len(nums)
        low = 0
        mid = 0
        high = n - 1
        
        # Create boxes and labels
        boxes = VGroup()
        num_labels = VGroup()
        index_labels = VGroup()
        
        # Colors for numbers
        colors = {
            0: BLUE,    # Blue for 0
            1: WHITE,   # White for 1
            2: RED      # Red for 2
        }
        
        def create_array_elements():
            boxes = VGroup()
            num_labels = VGroup()
            index_labels = VGroup()
            
            # Create an extra box for high pointer when it's at n
            for i in range(n + 1):  # Add one more position for high pointer
                box = Square(
                    side_length=1,
                    color=GRAY if i == n else colors[nums[i]] if i < n else WHITE,
                    fill_opacity=0.5 if i < n else 0,
                    stroke_width=2 if i < n else 0
                )
                
                if i < n:
                    num_label = Text(
                        str(nums[i]),
                        font_size=24,
                        color=BLACK if nums[i] == 1 else WHITE
                    )
                    num_label.move_to(box.get_center())
                else:
                    num_label = Text("", font_size=24)
                    num_label.move_to(box.get_center())
                
                index_label = Text(
                    str(i),
                    font_size=20,
                    color=WHITE
                )
                index_label.next_to(box, DOWN, buff=0.2)
                
                box.shift(RIGHT * i * 1.2)
                num_label.shift(RIGHT * i * 1.2)
                index_label.shift(RIGHT * i * 1.2)
                
                boxes.add(box)
                num_labels.add(num_label)
                index_labels.add(index_label)
            
            return boxes, num_labels, index_labels
        
        # Initial setup
        boxes, num_labels, index_labels = create_array_elements()
        boxes_group = VGroup(boxes, num_labels, index_labels)
        boxes_group.center()
        boxes_group.shift(DOWN * 0.5)
        
        # Create pointers
        def create_pointer(pos, color, label_text):
            arrow = Arrow(
                start=boxes[pos].get_bottom() + DOWN * 0.5,
                end=boxes[pos].get_bottom(),
                color=color
            )
            label = Text(label_text, font_size=20, color=color)
            label.next_to(arrow, DOWN, buff=0.2)
            return arrow, label
        
        # Create initial pointers
        low_arrow, low_label = create_pointer(low, GREEN, f"low = {low}")
        mid_arrow, mid_label = create_pointer(mid, YELLOW, f"mid = {mid}")
        high_arrow, high_label = create_pointer(n-1, RED, f"high = {high}")  # Position at last valid index
        
        # Create status text
        status_text = Text("", font_size=20)
        status_text.next_to(title, DOWN, buff=0.5)
        
        # Show initial setup
        self.play(Write(title))
        self.play(
            *[FadeIn(box) for box in boxes[:n]],  # Only show actual array boxes
            *[Write(label) for label in num_labels[:n]],  # Only show actual array labels
            *[Write(label) for label in index_labels[:n+1]],  # Show all index labels including n
            Create(low_arrow), Write(low_label),
            Create(mid_arrow), Write(mid_label),
            Create(high_arrow), Write(high_label)
        )
        
        # Function to swap elements
        def swap_elements(i, j):
            # Swap in array
            nums[i], nums[j] = nums[j], nums[i]
            
            # Create swap arrow
            swap_arrow = Arrow(
                start=boxes[i].get_center(),
                end=boxes[j].get_center(),
                color=YELLOW,
                stroke_width=2
            )
            
            # Animate swap
            self.play(Create(swap_arrow))
            self.play(
                boxes[i].animate.set_color(colors[nums[i]]),
                boxes[j].animate.set_color(colors[nums[j]]),
                num_labels[i].animate.become(
                    Text(str(nums[i]), font_size=24, color=BLACK if nums[i] == 1 else WHITE)
                    .move_to(boxes[i].get_center())
                ),
                num_labels[j].animate.become(
                    Text(str(nums[j]), font_size=24, color=BLACK if nums[j] == 1 else WHITE)
                    .move_to(boxes[j].get_center())
                )
            )
            self.play(FadeOut(swap_arrow))
        
        # Function to update pointer position
        def update_pointer(arrow, label, pos, name):
            self.play(
                arrow.animate.move_to(boxes[pos].get_bottom() + DOWN * 0.25),
                label.animate.become(
                    Text(f"{name} = {pos}", font_size=20, color=arrow.get_color())
                ).next_to(arrow, DOWN, buff=0.2)
            )
        
        # Step 1: nums[mid] = 2
        self.play(
            status_text.animate.become(
                Text("Step 1: nums[mid] = 2, swap with high", font_size=20)
                .next_to(title, DOWN, buff=0.5)
            )
        )
        swap_elements(0, 5)  # mid=0, high=5
        high = 4  # high moves to 4
        update_pointer(high_arrow, high_label, high, "high")
        self.wait(0.5)
        
        # Step 2: nums[mid] = 0
        self.play(
            status_text.animate.become(
                Text("Step 2: nums[mid] = 0, self-swap at low", font_size=20)
                .next_to(title, DOWN, buff=0.5)
            )
        )
        low = 1
        mid = 1
        update_pointer(low_arrow, low_label, low, "low")
        update_pointer(mid_arrow, mid_label, mid, "mid")
        self.wait(0.5)
        
        # Step 3: nums[mid] = 0
        self.play(
            status_text.animate.become(
                Text("Step 3: nums[mid] = 0, self-swap at low", font_size=20)
                .next_to(title, DOWN, buff=0.5)
            )
        )
        low = 2
        mid = 2
        update_pointer(low_arrow, low_label, low, "low")
        update_pointer(mid_arrow, mid_label, mid, "mid")
        self.wait(0.5)
        
        # Step 4: nums[mid] = 2
        self.play(
            status_text.animate.become(
                Text("Step 4: nums[mid] = 2, swap with high", font_size=20)
                .next_to(title, DOWN, buff=0.5)
            )
        )
        swap_elements(2, 4)  # mid=2, high=4
        high = 3
        update_pointer(high_arrow, high_label, high, "high")
        self.wait(0.5)
        
        # Step 5: nums[mid] = 1
        self.play(
            status_text.animate.become(
                Text("Step 5: nums[mid] = 1, increment mid", font_size=20)
                .next_to(title, DOWN, buff=0.5)
            )
        )
        mid = 3
        update_pointer(mid_arrow, mid_label, mid, "mid")
        self.wait(0.5)
        
        # Step 6: nums[mid] = 1
        self.play(
            status_text.animate.become(
                Text("Step 6: nums[mid] = 1, increment mid", font_size=20)
                .next_to(title, DOWN, buff=0.5)
            )
        )
        mid = 4
        update_pointer(mid_arrow, mid_label, mid, "mid")
        self.wait(0.5)
        
        # Exit condition
        self.play(
            status_text.animate.become(
                Text("Exit: mid > high (4 > 3), sorting complete!", font_size=20)
                .next_to(title, DOWN, buff=0.5)
            )
        )
        self.wait(1)
        
        # Clear the scene
        self.play(
            FadeOut(title),
            FadeOut(boxes),
            FadeOut(num_labels),
            FadeOut(index_labels),
            FadeOut(low_arrow),
            FadeOut(low_label),
            FadeOut(mid_arrow),
            FadeOut(mid_label),
            FadeOut(high_arrow),
            FadeOut(high_label),
            FadeOut(status_text)
        ) 