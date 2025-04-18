from manim import *
from Problems.LISbs.intro import IntroScene
from Problems.LISbs.tail_intuition import TailIntuitionScene
from Problems.LISbs.binary_search import BinarySearchScene
from Problems.LISbs.final_answer import FinalAnswerScene
from Problems.LISbs.implementation import ImplementationScene
from Problems.LISbs.outro import OutroScene

# Configure video settings for 1080p
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 8
config.frame_width = 14.22
config.frame_rate = 30
config.background_color = "#1e1e1e"

FASTER = 0.4

class LISBinarySearchAnimation(IntroScene, TailIntuitionScene, BinarySearchScene, 
                             FinalAnswerScene, ImplementationScene, OutroScene):
    def construct(self):
        # Run intro animations
        IntroScene.construct(self)
        self.wait(0.5)
        
        # Clear screen for tail intuition
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=FASTER)
        self.wait(0.5)
        
        # Run tail intuition animations
        TailIntuitionScene.construct(self)
        self.wait(0.5)
        
        # Clear screen for binary search
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=FASTER)
        self.wait(0.5)
        
        # Run binary search animations
        BinarySearchScene.construct(self)
        self.wait(0.5)
        
        # Clear screen for final answer
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=FASTER)
        self.wait(0.5)
        
        # Run final answer animations
        FinalAnswerScene.construct(self)
        self.wait(0.5)
        
        # Clear screen for implementation
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=FASTER)
        self.wait(0.5)
        
        # Run implementation animations
        ImplementationScene.construct(self)
        self.wait(0.5)
        
        # Clear screen for outro
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=FASTER)
        self.wait(0.5)
        
        # Run outro animations
        OutroScene.construct(self)
        self.wait(1)
        