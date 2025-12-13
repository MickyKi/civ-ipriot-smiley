from abc import ABC, abstractmethod

class Blinkable(ABC):
    """
    Specify what anything that claims to be 'blinkable' should be able to do.
    """
    @abstractmethod
    def blink(self, delay=0.25):
        """
        Abstract blink method — subclasses must implement their own blink behaviour.
        """
        pass
