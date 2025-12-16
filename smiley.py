from sense_hat import SenseHat

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
        self.pixels = [self.my_complexion] * 64
        self.show()

    def show(self):
        self.sense_hat.set_pixels(self.pixels)

    def clear(self):
        self.pixels = [self.BLACK] * 64
        self.show()

    # New method for Step 1 complexion sector
    def complexion(self):
        return self.YELLOW
