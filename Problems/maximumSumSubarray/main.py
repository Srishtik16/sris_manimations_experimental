from manim import *
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Problems.maximumSumSubarray.intro import IntroScene
from Problems.maximumSumSubarray.visualization import VisualizationScene
from Problems.maximumSumSubarray.kadane_init import KadaneInitScene
from Problems.maximumSumSubarray.kadane_iteration import KadaneIterationScene
from Problems.maximumSumSubarray.final_result import FinalResultScene
from Problems.maximumSumSubarray.code_display import CodeDisplayScene
from Problems.maximumSumSubarray.outro import OutroScene

# Set maximum cached files to 10
config.max_files_cached = 10

# Configure video settings for 1080p
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 8.0
config.frame_width = 14.222222222222222

class MaximumSubarrayAnimation(IntroScene, VisualizationScene, KadaneInitScene, KadaneIterationScene, FinalResultScene, CodeDisplayScene, OutroScene):
    def __init__(self, **kwargs):
        # Define the array for the Maximum Subarray problem
        self.nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        super().__init__(**kwargs)

    def construct(self):
        # Clear the scene between each part
        IntroScene.construct(self)
        self.clear()
        self.wait(1)
        
        VisualizationScene.construct(self)
        self.clear()
        self.wait(1)
        
        KadaneInitScene.construct(self)
        self.clear()
        self.wait(1)
        
        KadaneIterationScene.construct(self)
        self.clear()
        self.wait(1)
        
        FinalResultScene.construct(self)
        self.clear()
        self.wait(1)
        
        CodeDisplayScene.construct(self)
        self.clear()
        self.wait(1)
        
        OutroScene.construct(self)
        self.wait(2) 