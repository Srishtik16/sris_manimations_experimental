from manim import *

class ImplementationScene(Scene):
    def construct(self):
        # Title
        title = Text("Implementation", font_size=36)
        title.to_edge(UP, buff=0.5)
        
        # Create the code text
        code = '''void sortColors(vector<int>& a) {
    int n = a.size();
    int low = 0, mid = 0, high = n - 1;
    
    while(mid <= high) {
        if(a[mid] == 0) {
            swap(a[low], a[mid]);
            low++;
            mid++;
        }
        else if(a[mid] == 1) {
            mid++;
        }
        else {
            swap(a[mid], a[high]);
            high--;
        }
    }
}'''

        # Create code block with syntax highlighting
        code_block = Code(
            code_string=code,
            tab_width=4,
            language="cpp"
        )
        code_block.next_to(title, DOWN, buff=0.3)
        code_block.scale(0.6)
        
        # Show title and code
        self.play(Write(title))
        self.play(Create(code_block))
        self.wait(2)
        
        # Fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class SummaryScene(Scene):
    def construct(self):
        # Title
        title = Text("Summary", font_size=36)
        title.to_edge(UP, buff=0.5)
        
        # Create complexity information
        complexity_title = Text("Complexity Analysis:", font_size=28)
        time_complexity = Text("Time Complexity: O(n)", font_size=24, color=GREEN)
        space_complexity = Text("Space Complexity: O(1)", font_size=24, color=BLUE)
        
        # Stack complexity info vertically
        complexity_group = VGroup(complexity_title, time_complexity, space_complexity)
        complexity_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        complexity_group.next_to(title, DOWN, buff=0.7)
        
        # Create keywords section
        keywords_title = Text("Key Concepts:", font_size=28)
        keywords = VGroup(
            Text("• Dutch National Flag Problem", font_size=24),
            Text("• Three-Pointer Technique", font_size=24),
            Text("• Single-Pass Algorithm", font_size=24),
            Text("Try to implement this algorithm on your own!", font_size=28, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        keywords_group = VGroup(keywords_title, keywords)
        keywords_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        keywords_group.next_to(complexity_group, DOWN, buff=0.7)
        
        # Create visualization
        # Array squares
        squares = VGroup()
        colors = [RED, BLUE, RED, WHITE, WHITE, BLUE]
        for i in range(6):
            square = Square(side_length=0.8)
            square.set_fill(colors[i], opacity=0.5)
            square.set_stroke(WHITE, 2)
            squares.add(square)
        squares.arrange(RIGHT, buff=0.1)
        
        # Pointers
        low_arrow = Arrow(start=ORIGIN, end=UP, color=GREEN, buff=0)
        mid_arrow = Arrow(start=ORIGIN, end=UP, color=YELLOW, buff=0)
        high_arrow = Arrow(start=ORIGIN, end=UP, color=RED, buff=0)
        
        # Position arrows
        low_arrow.next_to(squares[0], DOWN, buff=0.1)
        mid_arrow.next_to(squares[1], DOWN, buff=0.1)
        high_arrow.next_to(squares[4], DOWN, buff=0.1)
        
        # Labels
        low_label = Text("low", font_size=20, color=GREEN)
        mid_label = Text("mid", font_size=20, color=YELLOW)
        high_label = Text("high", font_size=20, color=RED)
        
        low_label.next_to(low_arrow, DOWN, buff=0.1)
        mid_label.next_to(mid_arrow, DOWN, buff=0.1)
        high_label.next_to(high_arrow, DOWN, buff=0.1)
        
        # Group visualization
        vis_group = VGroup(squares, low_arrow, mid_arrow, high_arrow, 
                          low_label, mid_label, high_label)
        vis_group.next_to(keywords_group, DOWN, buff=0.7)
        
        # Animate everything
        self.play(Write(title))
        self.play(Write(complexity_title))
        self.play(Write(time_complexity))
        self.play(Write(space_complexity))
        
        self.play(Write(keywords_title))
        self.play(Write(keywords))
        
        self.wait(2)
        
        # Fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        ) 