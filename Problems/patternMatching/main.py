from manim import *
from Problems.patternMatching.intro import IntroScene
from Problems.patternMatching.z_array_meaning import ZArrayMeaningScene
from Problems.patternMatching.naive_computation import NaiveComputationScene
from Problems.patternMatching.optimized_computation import OptimizedComputationScene
from Problems.patternMatching.pattern_matching import PatternMatchingScene
from Problems.patternMatching.implementation import ImplementationScene
from Problems.patternMatching.summary import SummaryScene
import os

# Configure the video quality
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 8.0
config.frame_width = 14.222
config.frame_rate = 30
config.background_color = "#1e1e1e"

# Set output directory
config.media_dir = os.path.join(os.getcwd(), "media")
config.output_file = "ZAlgorithmAnimation"

class ZAlgorithmAnimation(IntroScene, ZArrayMeaningScene, NaiveComputationScene, OptimizedComputationScene, PatternMatchingScene, ImplementationScene, SummaryScene):
    def construct(self):
        # Add audio track for the entire video
        # self.add_sound("media/fractals3b1b.mpeg")

        # Module 1: Introduction
        IntroScene.construct(self)
        self.clear()
        
        # Module 2: Z-Array Meaning
        ZArrayMeaningScene.construct(self)
        self.clear()
        
        # Module 3: Naive Computation
        NaiveComputationScene.construct(self)
        self.clear()
        
        # Module 4: Optimized Computation
        OptimizedComputationScene.construct(self)
        self.clear()
        
        # Module 5: Pattern Matching
        PatternMatchingScene.construct(self)
        self.clear()
        
        # Module 6: Implementation
        ImplementationScene.construct(self)
        self.clear()
        
        # Module 7: Summary
        SummaryScene.construct(self)
        
        # End the video
        self.wait(0.1)  # Small wait to ensure final frame is captured 