from manim import *
from Problems.starsAndBars.intro import IntroScene
from Problems.starsAndBars.visualization import VisualizationScene
from Problems.starsAndBars.combinatorics import CombinatoricsScene
from Problems.starsAndBars.positive_case import PositiveCaseScene
from Problems.starsAndBars.sample_problem import SampleProblemScene
from Problems.starsAndBars.summary import SummaryScene

# Configure the video quality
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 8.0
config.frame_width = 14.222
config.frame_rate = 30
config.background_color = "#1e1e1e"

class StarsAndBarsAnimation(IntroScene, VisualizationScene, CombinatoricsScene, PositiveCaseScene, SampleProblemScene, SummaryScene):
    def construct(self):
        # Add audio track for the entire video
        self.add_sound("media/fractals3b1b.mpeg")

        # Module 1: Introduction
        IntroScene.construct(self)
        self.clear()
        
        # Module 2: Visualization
        VisualizationScene.construct(self)
        self.clear()
        
        # Module 3: Combinatorics
        CombinatoricsScene.construct(self)
        self.clear()
        
        # Module 4: Positive Case
        PositiveCaseScene.construct(self)
        self.clear()
        
        # Module 5: Sample Problem
        SampleProblemScene.construct(self)
        self.clear()
        
        # Module 6: Summary
        SummaryScene.construct(self)
        
        # End the video and audio
        self.wait(1.0)  # Small wait to ensure final frame is captured