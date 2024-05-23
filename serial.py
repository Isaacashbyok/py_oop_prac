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
    
    def __init__(self, start=0):
        '''
        Makes a new serial generator
        '''
        self.start = self.next = start
        
    def __repr__(self):
        '''
        Shows representation of serial generator
        '''
        return f'SerialGenerator (start = {self.start} next = {self.next})'
    
    def generate(self):
        '''
        returns the next serial number
        '''
        
        self.next += 1
        return self.next -1 
    
    def reset(self):
        '''
        Resets the serial number to the start
        '''
        
        self.next = self.start

