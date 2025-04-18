from manim import *

class ImplementationScene(Scene):
    def construct(self):
        # Title
        title = Text("Z-Function Implementation", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        
        # Code
        code_str = """vector<int> z_function(string s) {
    int n = s.size();
    vector<int> z(n);
    int l = 0, r = 0;
    for(int i = 1; i < n; i++) {
        if(i < r) {
            z[i] = min(r - i, z[i - l]);
        }
        while(i + z[i] < n && s[z[i]] == s[i + z[i]]) {
            z[i]++;
        }
        if(i + z[i] > r) {
            l = i;
            r = i + z[i];
        }
    }
    return z;
}"""
        
        # Create code with proper formatting
        code = Code(
            code_string=code_str,
            tab_width=4,
            language="cpp",
        )
        
        # Scale code to fit screen
        code.scale(0.8)
        code.next_to(title, DOWN, buff=0.8)
        
        # Create explanation boxes
        explanation1 = Text(
            "Key Components:",
            font_size=28,
            color=YELLOW
        )
        explanation1.next_to(code, DOWN, buff=0.8)
        
        points = [
            "• l, r: Current window boundaries",
            "• z[i]: Length of prefix match at i",
            "• Optimization: Reuse previous matches",
            "• Time Complexity: O(n)"
        ]
        
        point_texts = []
        for point in points:
            text = Text(point, font_size=24, color=WHITE)
            point_texts.append(text)
        
        points_group = VGroup(*point_texts)
        points_group.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        points_group.next_to(explanation1, DOWN, buff=0.5)
        
        # Animate everything
        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(code))
        self.wait(0.5)
        self.play(Write(explanation1))
        self.wait(0.5)
        
        for point in point_texts:
            self.play(Write(point))
            self.wait(0.3)
        
        self.wait(2) 