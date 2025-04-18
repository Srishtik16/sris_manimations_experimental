from manim import *
from Problems.LISdp.intro import IntroScene
from Problems.LISdp.dp_init import DPInitScene
from Problems.LISdp.dp_iteration import DPIterationScene
from Problems.LISdp.highlight_answer import HighlightAnswerScene
from Problems.LISdp.code_reveal import CodeRevealScene
from Problems.LISdp.summary import SummaryScene

# Configure video settings for 1080p
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 8
config.frame_width = 14.22
config.frame_rate = 30
config.background_color = "#1e1e1e"

class LISAnimation(IntroScene, DPInitScene, DPIterationScene, 
                  HighlightAnswerScene, CodeRevealScene, SummaryScene):
    def construct(self):

        self.add_sound("media/fractals3b1b.mpeg")

        # Run intro animations
        IntroScene.construct(self)
        self.wait(0.5)
        
        # Clear screen for DP initialization
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)
        
        # Run DP initialization animations
        DPInitScene.construct(self)
        self.wait(0.5)
        
        # Clear screen for DP iteration
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)
        
        # Run DP iteration animations
        DPIterationScene.construct(self)
        self.wait(0.5)
        
        # Clear screen for highlighting answer
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)
        
        # Run highlight answer animations
        HighlightAnswerScene.construct(self)
        self.wait(0.5)
        
        # Clear screen for code reveal
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)
        
        # Run code reveal animations
        CodeRevealScene.construct(self)
        self.wait(0.5)
        
        # Clear screen for summary
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)
        
        # Run summary animations
        SummaryScene.construct(self)
        self.wait(1) 