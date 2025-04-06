from manim import *
from DataStructures.fenwickTree.intro import IntroScene
from DataStructures.fenwickTree.visualization import VisualizationScene
from DataStructures.fenwickTree.construction import ConstructionScene
from DataStructures.fenwickTree.query import QueryScene
from DataStructures.fenwickTree.bitwise import BitwiseScene, BitwiseScene2
from DataStructures.fenwickTree.summary import SummaryScene

# Configure video settings for 1080p
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 8.0
config.frame_width = 14.222222222222222

class FenwickTreeAnimation(IntroScene, VisualizationScene, ConstructionScene, QueryScene, BitwiseScene, BitwiseScene2, SummaryScene):
    def construct(self):
        # Run intro animations
        IntroScene.construct(self)
        self.clear()
        self.wait(1)
        
        # Run visualization animations
        VisualizationScene.construct(self)
        self.clear()
        self.wait(1)
        
        # Run construction animations
        ConstructionScene.construct(self)
        self.clear()
        self.wait(1)
        
        # Run query animations
        QueryScene.construct(self)
        self.clear()
        self.wait(1)
        
        # Run first bitwise operations explanation
        BitwiseScene.construct(self)
        self.wait(1)
        
        # Run second bitwise operations explanation
        BitwiseScene2.construct(self)
        self.wait(1)
        
        # Run summary and outro
        SummaryScene.construct(self)
        self.wait(1) 