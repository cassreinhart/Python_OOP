"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=100):
        """ Make a new serial number generator, starting at optional start value """

        self.start = self.n = start

    def __repr__(self):
        """return representation of object"""

        return f'<SerialGenerator start={self.start} n={self.n}>'

    def generate(self, start=100):
        """ Return a new serial number. """

        self.n += 1
        return self.n -1

    def reset(self, start=100):
        """ reset generator to original start. """
        self.n = self.start



