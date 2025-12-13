import time
from blinkable import Blinkable
from smiley import Smiley


class Happy(Smiley, Blinkable):
    """
   Provides a Smiley with a happy expression
    """
    def __init__(self):
        super().__init__()

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
       Renders a mouth by blanking the pixels that form that object.
        """
        mouth = [41, 46, 50, 51, 52, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK
            
    def draw_happy_face(self):
        """
        Combines mouth and eyes into a full happy face
        """
        self.draw_mouth()
        self.draw_eyes()
        self.show()   # push pixels to display

    def blink(self, delay=0.25):
        """
        Blinks the happy smiley's eyes once
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()


