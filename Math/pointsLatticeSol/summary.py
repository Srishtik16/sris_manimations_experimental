from manim import *

class SummaryScene(Scene):
    def construct(self):
        # Title
        title = Text("Proof Summary", font_size=36)
        title.to_edge(UP, buff=0.3)
        
        # Key points
        points = [
            "Midpoint is integer ⇔ same parity",
            "Only 4 parity classes",
            "5 points → at least 1 duplicate class"
        ]
        
        # Create points with checkmarks
        point_mobjects = VGroup()
        for point in points:
            # Create checkmark
            check = MathTex("\\checkmark", color=GREEN)
            check.scale(0.8)
            
            # Create point text
            text = Text(point, font_size=28)
            
            # Group checkmark and text
            group = VGroup(check, text)
            group.arrange(RIGHT, buff=0.3)
            point_mobjects.add(group)
        
        # Arrange points vertically
        point_mobjects.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        point_mobjects.next_to(title, DOWN, buff=1.0)
        
        # Create proof complete text
        proof_complete = Text("Proof Complete ✅", font_size=36, color=GREEN)
        proof_complete.next_to(point_mobjects, DOWN, buff=1.0)
        
        # Create final note
        final_note = Text(
            "A classic case of the Pigeonhole Principle meets Coordinate Parity!",
            font_size=24,
            color=YELLOW
        )
        final_note.next_to(proof_complete, DOWN, buff=0.8)
        
        # Animations
        self.play(Write(title))
        self.wait(0.5)
        
        # Animate points one by one
        for point in point_mobjects:
            self.play(
                FadeIn(point[0]),  # Checkmark
                Write(point[1]),   # Text
                run_time=1
            )
            self.wait(0.3)
        
        # Show proof complete with bounce effect
        self.play(
            Write(proof_complete),
            run_time=1
        )
        self.play(
            proof_complete.animate.scale(1.2),
            run_time=0.3
        )
        self.play(
            proof_complete.animate.scale(1/1.2),
            run_time=0.3
        )
        
        # Show final note
        self.play(
            Write(final_note),
            run_time=1
        )
        self.wait(2)
        
        # Clear the scene
        self.play(
            FadeOut(title),
            FadeOut(point_mobjects),
            FadeOut(proof_complete),
            FadeOut(final_note)
        ) 