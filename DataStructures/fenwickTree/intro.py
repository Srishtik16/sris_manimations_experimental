from manim import *

class IntroScene(Scene):
    def construct(self):
        # Title
        title = Text("Fenwick Tree (Binary Indexed Tree)", color=BLUE, font_size=48)
        title.to_edge(UP, buff=1)
        
        # Subtitle - Use case
        subtitle = Text("Efficient data structure for prefix sums", 
                       color=YELLOW, 
                       font_size=36)
        subtitle.next_to(title, DOWN, buff=0.8)
        
        # Time complexities
        time_complexity = VGroup()
        
        complexity_title = Text("Time Complexity:", 
                              font_size=32)
        
        update_complexity = Text("• Update: O(log n)", 
                               font_size=28,
                               color=GREEN)
        
        query_complexity = Text("• Query: O(log n)", 
                              font_size=28,
                              color=GREEN)
        
        time_complexity.add(complexity_title, update_complexity, query_complexity)
        time_complexity.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        time_complexity.next_to(subtitle, DOWN, buff=1)
        
        # Example scenario
        example = VGroup()
        
        example_title = Text("Example Use Case:", 
                           font_size=32)
        
        scenario = Text("We want to compute prefix sums quickly\nafter multiple updates to the array", 
                       font_size=28,
                       color=BLUE_B)
        scenario.set_line_spacing(0.5)  # Adjust line spacing
        
        # Center title above scenario
        example_title.move_to(scenario.get_top() + UP * 0.5)
        
        example.add(example_title, scenario)
        example.next_to(time_complexity, DOWN, buff=1)
        
        # Animation sequence
        # 1. Fade in title
        self.play(
            Write(title)
        )
        self.wait(1)
        
        # 2. Slide in use case text
        self.play(
            FadeIn(subtitle, shift=RIGHT)
        )
        self.wait(1)
        
        # 3. Display time complexities one by one
        for item in time_complexity:
            self.play(
                Write(item)
            )
            self.wait(0.5)
        
        # 4. Show example scenario
        self.play(
            Write(example_title)
        )
        self.wait(0.5)
        
        # Highlight the use case with a growing effect
        self.play(
            GrowFromCenter(scenario)
        )
        self.wait(2) 