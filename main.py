"""
Demonstrates the use of the Smiley class and its subclasses.
If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator),
you can use the real SenseHAT class instead of the mock SenseHAT class.
That is, delete the sense_hat.py file that is included in this bundle.
"""

import time
from happy import HappySmiley
from sad import SadSmiley
from angry import AngrySmiley

def main():
    # Show Happy Smiley
    happy_face = HappySmiley()
    time.sleep(1)
    happy_face.blink(delay=1)   # blink with 1 second delay

    # Show Sad Smiley
    sad_face = SadSmiley()
    time.sleep(1)
    sad_face.blink(delay=1)     # blink with 1 second delay

    # Show Angry Smiley
    angry_face = AngrySmiley()
    time.sleep(1)
    # Angry shows face only in this demo (no blink)

if __name__ == '__main__':
    ############################################################
    # Uncomment the lines below only if you have multi-processing issues
    # from multiprocessing import freeze_support
    # freeze_support()
    ############################################################
    main()
