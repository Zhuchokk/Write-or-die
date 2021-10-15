from abc import abstractmethod, ABCMeta


class ITimer(object):
    """Timer, after which if the user does not write a single letter, there will be a punishment"""

    @abstractmethod
    def countdown(self, func):
        """Visual countdown
        func - function for punishment"""

    @abstractmethod
    def _continue(self):
        """The timer continues to count down"""

    @abstractmethod
    def reset(self, plug):
        """Reloads the timer
        plug - plug for function keyboard.hook"""

    @abstractmethod
    def stop(self):
        """Stops the timer"""

    @abstractmethod
    def checker(self):
        """Check keyboard hook"""
