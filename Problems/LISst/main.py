from manim import *
from Problems.LISst.coordinate_compression import CoordinateCompressionScene
from Problems.LISst.coordinate_compression import ImplementationScene
from Problems.LISst.coordinate_compression import OutroScene
from Problems.LISst.intro import IntroScene
from Problems.LISst.segment_tree_use import SegmentTreeUseScene

# Configure video settings for 1080p
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 8
config.frame_width = 14.22
config.frame_rate = 30
config.background_color = "#1e1e1e"

FASTER = 0.4

class LISSegmentTreeAnimation(IntroScene, SegmentTreeUseScene, CoordinateCompressionScene, ImplementationScene, OutroScene):
    def construct(self):
        # Run intro animations
        IntroScene.construct(self)
        self.wait(0.5)
        
        # Clear screen for segment tree use
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=FASTER)
        self.wait(0.5)
        
        # Run segment tree use animations
        SegmentTreeUseScene.construct(self)
        self.wait(0.5)
        
        # Clear screen for coordinate compression
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=FASTER)
        self.wait(0.5)
        
        # Run coordinate compression animations
        CoordinateCompressionScene.construct(self)
        self.wait(1)

        # Clear screen for implementation
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=FASTER)
        self.wait(0.5)

        # Run implementation animations
        ImplementationScene.construct(self)
        self.wait(1)

        # Clear screen for outro
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=FASTER)
        self.wait(0.5)
        
        # Run outro animations
        OutroScene.construct(self)