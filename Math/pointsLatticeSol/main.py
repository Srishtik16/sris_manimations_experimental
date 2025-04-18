from manim import *
from Math.pointsLatticeSol.intro import SolutionIntroScene
from Math.pointsLatticeSol.parity import ParityScene
from Math.pointsLatticeSol.sample_points import SamplePointsScene
from Math.pointsLatticeSol.parity_classification import ParityClassificationScene
from Math.pointsLatticeSol.pigeonhole import PigeonholeScene
from Math.pointsLatticeSol.midpoint import MidpointScene
from Math.pointsLatticeSol.summary import SummaryScene
# Configure the video quality
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 8.0
config.frame_width = 14.222
config.frame_rate = 30
config.background_color = "#1e1e1e"

class LatticePointsSolutionAnimation(Scene):
    def construct(self):

         # Add audio track for the entire video
        self.add_sound("media/fractals3b1b.mpeg")
        
        # Module 1: Introduction and Problem Recap
        SolutionIntroScene.construct(self)

        # Module 2: Coordinate Parity
        ParityScene.construct(self)

        # Module 3: Sample Points
        SamplePointsScene.construct(self)    

        # Module 4: Parity Classification
        ParityClassificationScene.construct(self)
        
        # Module 5: Pigeonhole Principle
        PigeonholeScene.construct(self)

        # Module 6: Midpoint
        MidpointScene.construct(self)
        
        # Module 7: Summary
        SummaryScene.construct(self)
        
        # End the video
        self.wait(0.1)  # Small wait to ensure final frame is captured 