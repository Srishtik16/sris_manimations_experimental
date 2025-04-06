from manim import *
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Problems.twoSum.intro import IntroScene
from Problems.twoSum.bruteforce import BruteForceScene
from Problems.twoSum.optimal import OptimalScene
from Problems.twoSum.summary import SummaryScene

config.max_files_cached = 10  # Set maximum cached files to 10

class TwoSumAnimation(IntroScene, BruteForceScene, OptimalScene, SummaryScene):
    def __init__(self, **kwargs):
        # Define the array and target for the Two Sum problem
        self.nums = [2, 7, 11, 15]
        self.target = 18
        super().__init__(**kwargs)

    def construct(self):
        # Run intro animations
        IntroScene.construct(self)
        self.clear()
        self.wait(1)
        
        # Run brute force animations
        BruteForceScene.construct(self)
        self.clear()
        self.wait(1)
        
        # Run optimal solution animations
        OptimalScene.construct(self)
        self.clear()
        self.wait(1)
        
        # Run summary animations
        SummaryScene.construct(self)
        self.clear()
        self.wait(1)

if __name__ == "__main__":
    """
    To render individual scenes:
    python3 -m manim -pql main.py IntroScene
    python3 -m manim -pql main.py BruteForceScene
    python3 -m manim -pql main.py OptimalScene
    python3 -m manim -pql main.py SummaryScene
    
    To render the complete animation:
    python3 -m manim -pql main.py TwoSumAnimation
    """
    with tempconfig({
        "quality": "high_quality",
        "preview": True,
        "pixel_width": 1920,
        "pixel_height": 1080,
        "frame_rate": 60,
        "renderer": "cairo",
        "background_color": BLACK,
        "background_opacity": 1,
    }):
        scene = TwoSumAnimation()
        scene.render() 