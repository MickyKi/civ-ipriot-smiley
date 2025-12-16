from smiley import Smiley

class AngrySmiley(Smiley):
    # I used an orange background made to help distinguish, while sharing same smiley base smiley setup, red eyes would not have shown on red background... 
    ORANGE = (255, 165, 0)

    def __init__(self):
        # Use orange complexion for background
        super().__init__(complexion=self.ORANGE)
        self.draw_angry_face()

    def draw_mouth(self):
        """
        Draws a straight/downturned mouth for the angry face.
        """
        mouth = [42, 43, 44, 45]   # middle line
        corners = [41, 46]         # corners to emphasise downturned mouth
        for pixel in mouth + corners:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self):
        """
        Draws red eyes for the angry face.
        """
        eye_pixels = [10, 13, 18, 21]
        for pixel in eye_pixels:
            self.pixels[pixel] = self.RED

    def draw_angry_face(self):
        """
        Combines mouth and eyes into a full angry face.
        """
        self.pixels = [self.my_complexion] * 64
        self.draw_mouth()
        self.draw_eyes()
        self.show()
