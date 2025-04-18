from manim import *

class ImplementationScene(Scene):
    def construct(self):
        # Implementation 1: While-If Approach
        title1 = Text("Implementation 1: While-If Approach", font_size=36, color=BLUE)
        title1.to_edge(UP, buff=0.5)
        
        code1 = '''int lengthOfLongestSubstring_while(const string& s) {
    int n = s.size();
    int l = 0, r = 0;
    unordered_set<char> seen;
    int maxLen = 0;

    while (r < n) {
        if (seen.find(s[r]) == seen.end()) {
            seen.insert(s[r]);
            maxLen = max(maxLen, r - l + 1);
            r++;
        } else {
            seen.erase(s[l]);
            l++;
        }
    }
    return maxLen;
}'''

        code_text1 = Code(
            code_string=code1,
            tab_width=4,
            language="cpp",
        )
        code_text1.next_to(title1, DOWN, buff=0.5)
        code_text1.scale(0.6)
        
        # First implementation group
        impl1 = VGroup(title1, code_text1)
        
        # Show first implementation
        self.play(Write(title1))
        self.play(Create(code_text1))
        self.wait(2)
        
        # Move first implementation up and fade out
        self.play(
            impl1.animate.shift(UP * 7),
            FadeOut(impl1)
        )
        
        # Implementation 2: While-For Approach
        title2 = Text("Implementation 2: For-While Approach", font_size=36, color=BLUE)
        title2.to_edge(UP, buff=0.5)
        
        code2 = '''int lengthOfLongestSubstring_for(const string& s) {
    int n = s.size();
    unordered_set<char> seen;
    int l = 0, maxLen = 0;

    for (int r = 0; r < n; ++r) {
        while (seen.find(s[r]) != seen.end()) {
            seen.erase(s[l]);
            l++;
        }
        seen.insert(s[r]);
        maxLen = max(maxLen, r - l + 1);
    }
    return maxLen;
}'''

        code_text2 = Code(
            code_string=code2,
            tab_width=4,
            language="cpp",
        )
        code_text2.next_to(title2, DOWN, buff=0.5)
        code_text2.scale(0.6)
        
        # Second implementation group
        impl2 = VGroup(title2, code_text2)
        
        # Show second implementation
        self.play(Write(title2))
        self.play(Create(code_text2))
        self.wait(2)
        
        # Add comparison note
        note = Text(
            "Both implementations achieve the same result with different loop structures",
            font_size=24,
            color=YELLOW
        )
        note.next_to(code_text2, DOWN, buff=0.8)
        self.play(Write(note))
        self.wait(2) 