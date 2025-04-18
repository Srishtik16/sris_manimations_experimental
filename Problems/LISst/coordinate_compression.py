from manim import *

class CoordinateCompressionScene(Scene):
    def construct(self):
        # Title
        title = Text("Coordinate Compression", font_size=36)
        subtitle = Text("Mapping values to segment tree indices", font_size=24, color=BLUE)
        title.to_edge(UP, buff=0.3)
        subtitle.next_to(title, DOWN, buff=0.2)
        
        # Original array
        original_array = [3, 1, 4, 1, 5]
        original_label = Text("Original Array:", font_size=28)
        original_squares = VGroup(*[
            Square(side_length=0.7).set_fill(color=BLUE_E, opacity=0.3) 
            for _ in original_array
        ]).arrange(RIGHT, buff=0.1)
        original_nums = VGroup(*[
            Text(str(n), font_size=22) for n in original_array
        ])
        for num, square in zip(original_nums, original_squares):
            num.move_to(square)
        original_group = VGroup(original_squares, original_nums)
        original_row = VGroup(original_label, original_group).arrange(RIGHT, buff=0.5)
        
        # Sorted unique elements
        sorted_unique = sorted(set(original_array))
        sorted_label = Text("Sorted Unique:", font_size=28)
        sorted_squares = VGroup(*[
            Square(side_length=0.7).set_fill(color=GREEN_E, opacity=0.3) 
            for _ in sorted_unique
        ]).arrange(RIGHT, buff=0.1)
        sorted_nums = VGroup(*[
            Text(str(n), font_size=22) for n in sorted_unique
        ])
        for num, square in zip(sorted_nums, sorted_squares):
            num.move_to(square)
        sorted_group = VGroup(sorted_squares, sorted_nums)
        
        # Create a container for sorted label and array that ensures alignment
        sorted_container = VGroup(sorted_label, sorted_group).arrange(RIGHT, buff=0.5)
        
        # Compressed indices (now directly under sorted squares)
        compressed_nums = VGroup(*[
            Text(str(i), font_size=22, color=YELLOW) 
            for i in range(len(sorted_unique))
        ])
        
        # Position each index directly under its corresponding square
        for idx, (num, square) in enumerate(zip(compressed_nums, sorted_squares)):
            num.next_to(square, DOWN, buff=0.3)
        
        # Group the sorted array with its indices
        sorted_with_indices = VGroup(sorted_container, compressed_nums)
        
        # Arrange all elements vertically with proper spacing
        all_elements = VGroup(
            original_row,
            sorted_with_indices
        ).arrange(DOWN, buff=1.2, aligned_edge=LEFT)
        
        # Position everything relative to the subtitle
        all_elements.next_to(subtitle, DOWN, buff=1.0)
        
        # Initial animation
        self.play(
            Write(title),
            Write(subtitle)
        )
        self.wait(0.5)
        
        # Show original array
        self.play(Write(original_row))
        self.wait(0.5)
        
        # Show sorted unique elements
        self.play(Write(sorted_container))
        self.wait(0.5)
        
        # Show compressed indices
        self.play(Write(compressed_nums))
        self.wait(0.5)
        
        # Create thin mapping arrows
        mapping_arrows = VGroup()
        for i, num in enumerate(original_array):
            original_square = original_squares[i]
            target_idx = sorted_unique.index(num)
            target_square = sorted_squares[target_idx]
            
            arrow = Arrow(
                original_square.get_bottom(),
                target_square.get_top(),
                color=YELLOW,
                buff=0.2,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.1
            )
            mapping_arrows.add(arrow)
        
        # Animate mapping arrows
        self.play(Create(mapping_arrows))
        self.wait(1)
        
        # Show usage in segment tree
        usage_text = VGroup(
            Text("These compressed indices are used in:", font_size=24),
            Text("1. query(0, compressed_index - 1)", font_size=20, color=GREEN),
            Text("2. update(compressed_index, value)", font_size=20, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        usage_text.next_to(sorted_with_indices, DOWN, buff=1.0)
        
        self.play(Write(usage_text))
        self.wait(1)
        
        # Highlight example
        example = VGroup(
            Text("Example:", font_size=24, color=YELLOW),
            Text("For value 3:", font_size=20),
            Text("compressed_index = 1", font_size=20, color=GREEN),
            Text("query(0, 0) → get max in range", font_size=20, color=GREEN),
            Text("update(1, value) → update segment tree", font_size=20, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        example.next_to(usage_text, DOWN, buff=0.8)
        
        self.play(Write(example))
        self.wait(1)

class ImplementationScene(Scene):
    def construct(self):
        # Title
        title = Text("Implementation", font_size=36)
        subtitle = Text("LIS using Segment Tree", font_size=24, color=BLUE)
        title.to_edge(UP, buff=0.3)
        subtitle.next_to(title, DOWN, buff=0.2)
        
        # Code implementation with shorter lines and compact formatting
        code = '''def longest_increasing_subsequence(arr):
    # 1. Coordinate compression
    unique = sorted(set(arr))
    val_to_idx = {x: i for i, x in enumerate(unique)}
    n = len(unique)
    tree = [0] * (4 * n)  # Initialize segment tree
    
    def query(node, start, end, l, r):
        if r < start or end < l: return 0
        if l <= start and end <= r: return tree[node]
        mid = (start + end) // 2
        return max(query(2*node, start, mid, l, r),
                  query(2*node+1, mid+1, end, l, r))
    
    def update(node, start, end, pos, val):
        if start == end:
            tree[node] = val
            return
        mid = (start + end) // 2
        if pos <= mid:
            update(2*node, start, mid, pos, val)
        else:
            update(2*node+1, mid+1, end, pos, val)
        tree[node] = max(tree[2*node], tree[2*node+1])
    
    # 2. Build LIS using segment tree
    dp = [1] * len(arr)
    for i, num in enumerate(arr):
        idx = val_to_idx[num]
        if idx > 0:
            dp[i] = 1 + query(1, 0, n-1, 0, idx-1)
        update(1, 0, n-1, idx, dp[i])
    
    return max(dp)'''

        # Create code text with specific styling
        code_text = Code(
            code_string=code,
            tab_width=4,
            language="python"
        )
        
        # Position and scale code
        code_text.next_to(subtitle, DOWN, buff=0.5)
        code_text.scale(0.4)  # Adjust scale to fit screen
        
        # Center the code on screen
        code_text.move_to(ORIGIN).shift(DOWN * 0.5)
        
        # Animation
        self.play(Write(title), Write(subtitle))
        self.wait(0.5)
        self.play(Create(code_text))
        self.wait(2)

class OutroScene(Scene):
    def construct(self):
        # Title
        title = Text("Summary", font_size=36)
        subtitle = Text("Using Segment Tree for LIS", font_size=24, color=BLUE)
        title.to_edge(UP, buff=0.3)
        subtitle.next_to(title, DOWN, buff=0.2)
        
        # Key points with icons
        points = VGroup(
            Text("🔄 Compress values to array indices", font_size=24),
            Text("🔍 Query max dp for smaller values", font_size=24),
            Text("⬆️ Update new dp in segment tree", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # Segment tree usage box
        usage_box = VGroup(
            Text("Segment Tree Operations", font_size=28, color=YELLOW),
            Text("• Range Query: Get max dp[j] where arr[j] < arr[i]", font_size=22),
            Text("• Point Update: Store new dp[i] values", font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        usage_box.set_color_by_gradient(BLUE, GREEN)
        
        # Time complexity badge
        complexity = VGroup(
            Text("Time Complexity", font_size=28, color=YELLOW),
            Text("O(n log n)", font_size=32, color=GREEN)
        ).arrange(DOWN, buff=0.2)
        complexity_box = SurroundingRectangle(complexity, buff=0.3, color=BLUE)
        complexity_group = VGroup(complexity, complexity_box)
        
        # Final prompt
        prompt = Text("Try implementing this!", font_size=32, color=YELLOW)
        
        # Arrange elements
        points.next_to(subtitle, DOWN, buff=0.5)
        usage_box.next_to(points, DOWN, buff=0.5)
        complexity_group.next_to(usage_box, DOWN, buff=0.5)
        prompt.next_to(complexity_group, DOWN, buff=0.5)
        
        # Animations
        self.play(Write(title), Write(subtitle))
        self.wait(0.5)
        
        # Animate key points one by one
        for point in points:
            self.play(Write(point))
            self.wait(0.3)
        
        # Animate usage box
        self.play(Write(usage_box))
        self.wait(0.5)
        
        # Animate complexity badge
        self.play(
            Write(complexity),
            Create(complexity_box)
        )
        self.wait(0.5)
        
        # Animate final prompt with bounce effect
        self.play(
            Write(prompt),
            prompt.animate.scale(1.1).shift(UP * 0.1)
        )
        self.play(prompt.animate.scale(1/1.1).shift(DOWN * 0.1))
        self.wait(1) 