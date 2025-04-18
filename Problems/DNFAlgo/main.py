from manim import *
from Problems.DNFAlgo.intro import IntroScene
from Problems.DNFAlgo.array_display import ArrayDisplayScene
from Problems.DNFAlgo.pointer_setup import PointerSetupScene, SortingProcessScene
from Problems.DNFAlgo.sorting_animation import DNFSortingScene
from Problems.DNFAlgo.implementation_summary import ImplementationScene, SummaryScene
# Configure the video quality
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 8.0
config.frame_width = 14.222
config.frame_rate = 30
config.background_color = "#1e1e1e"

class DutchNationalFlagAnimation(IntroScene, ArrayDisplayScene, PointerSetupScene):
    def construct(self):
        # Add audio track for the entire video
        self.add_sound("media/fractals3b1b.mpeg")

        # Module 1: Introduction
        IntroScene.construct(self)
        
        # Module 2: Array Display
        ArrayDisplayScene.construct(self)

        # Module 3: Sorting
        PointerSetupScene.construct(self)
        
        # Create and play sorting process scene
        DNFSortingScene.construct(self)
        
        # Module 5: Implementation
        ImplementationScene.construct(self)
        
        # Module 6: Summary
        SummaryScene.construct(self)
        
        # End the video
        self.wait(0.1)  # Small wait to ensure final frame is captured 