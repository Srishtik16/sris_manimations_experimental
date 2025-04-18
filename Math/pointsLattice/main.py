from manim import *
from Math.pointsLattice.intro import IntroScene
from Math.pointsLattice.grid_setup import GridSetupScene
from Math.pointsLattice.random_points import RandomPointsScene
from Math.pointsLattice.goal import GoalScene
from Math.pointsLattice.integer_midpoints import IntegerMidpointsScene

# Configure the video quality
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 8.0
config.frame_width = 14.222
config.frame_rate = 30
config.background_color = "#1e1e1e"

class LatticePointsAnimation(IntroScene, GridSetupScene, RandomPointsScene, GoalScene, IntegerMidpointsScene):
    def construct(self):

        # Add audio track for the entire video
        self.add_sound("media/fractals3b1b.mpeg")

        # Module 1: Introduction
        IntroScene.construct(self)
        
        # Module 2: Grid Setup
        GridSetupScene.construct(self)
        
        # Module 3: Random Points
        RandomPointsScene.construct(self)
        
        # Module 4: Goal
        GoalScene.construct(self)
        
        # Module 5: Integer Midpoints
        IntegerMidpointsScene.construct(self)
        
        # End the video
        self.wait(0.1)  # Small wait to ensure final frame is captured