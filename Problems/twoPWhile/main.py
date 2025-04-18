from manim import *
from Problems.twoPWhile.intro import IntroScene
from Problems.twoPWhile.pointer_scene import PointerScene
from Problems.twoPWhile.while_loop_scene import WhileLoopScene
from Problems.twoPWhile.implementation_scene import ImplementationScene
from Problems.twoPWhile.summary_scene import SummaryScene

# Configure the video quality
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 8.0
config.frame_width = 14.222
config.frame_rate = 30
config.background_color = "#1e1e1e"

class TwoPWhileAnimation(IntroScene, PointerScene, WhileLoopScene, ImplementationScene, SummaryScene):
    def construct(self):
        # Add audio track for the entire video
        self.add_sound("media/fractals3b1b.mpeg")

        # Module 1: Introduction
        IntroScene.construct(self)
        self.clear()
        
        # Module 2: Pointer Scene
        PointerScene.construct(self)
        self.clear()
        
        # Module 3: While Loop Execution
        WhileLoopScene.construct(self)
        self.clear()
        
        # Module 4: Implementation
        ImplementationScene.construct(self)
        self.clear()
        
        # Module 5: Summary & Outro
        SummaryScene.construct(self)
        
        self.wait(0.1)  # Small wait to ensure final frame is captured 