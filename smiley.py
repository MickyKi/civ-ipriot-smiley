from sense_hat import SenseHat
import time

class Smiley:
    # Class variables (shared constants)
    BLACK   = (0, 0, 0)
    BLANK   = BLACK
    YELLOW  = (255, 255, 0)
    WHITE   = (255, 255, 255)
    RED     = (255, 0, 0)
    GREEN   = (0, 255, 0)
    BLUE    = (0, 0, 255)
    ORANGE  = (255, 165, 0)

    def __init__(self, complexion=YELLOW):
        # Instance variables
        self.sense_hat = SenseHat()
        self.my_complexion = complexion

        # 8x8 grid AFTER refactor: complexion, complexion, ...
        self.pixels = [
            complexion, complexion, complexion, complexion, complexion, complexion, complexion, complexion,
            complexion, complexion, complexion, complexion, complexion, complexion, complexion, complexion,
            complexion, complexion, complexion, complexion, complexion, complexion, complexion, complexion,
            complexion, complexion, complexion, complexion, complexion, complexion, complexion, complexion,
            complexion, complexion, complexion, complexion, complexion, complexion, complexion, complexion,
            complexion, complexion, complexion, complexion, complexion, complexion, complexion, complexion,
            complexion, complexion, complexion, complexion, complexion, complexion, complexion, complexion,
            complexion, complexion, complexion, complexion, complexion, complexion, complexion, complexion,
        ]

        self.show()

    def show(self):
        self.sense_hat.set_pixels(self.pixels)

    def clear(self):
        self.pixels = [self.BLACK] * 64
        self.show()

    def complexion(self):
        return self.my_complexion


class HappySmiley(Smiley):
    def __init__(self):
        super().__init__(complexion=Smiley.YELLOW)


class SadSmiley(Smiley):
    def __init__(self):
        super().__init__(complexion=Smiley.BLUE)


class AngrySmiley(Smiley):
    def __init__(self):
        super().__init__(complexion=Smiley.RED)


if __name__ == "__main__":
    Smiley()         # default yellow
    time.sleep(1)
    HappySmiley()    # yellow
    time.sleep(1)
    SadSmiley()      # blue
    time.sleep(1)
    AngrySmiley()    # red
    time.sleep(1)
