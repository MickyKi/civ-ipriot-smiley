"""Demonstrates the use of the Smiley class and its subclasses.
If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator),
you can use the real SenseHAT class instead of the mock SenseHAT class.
That is, delete the sense_hat.py file that is included in this bundle.
"""

import time

from happy import Happy
from sad import Sad   

def main():
    # Tests the Happy Smiley
    happy_face = Happy()
    happy_face.draw_happy_face()   
    time.sleep(1)
    happy_face.blink()

    # Tests the Sad Smiley
    sad_face = Sad()
    sad_face.draw_sad_face()       
    time.sleep(1)
    sad_face.blink()


if __name__ == '__main__':
    ############################################################
    # Uncomment the lines below only if you have multi-processing issues
    # from multiprocessing import freeze_support
    # freeze_support()
    ############################################################
    main()
