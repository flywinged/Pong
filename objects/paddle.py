from TGL.internal import GameObject, Box, timeFunction, Event

import numpy

class Paddle(GameObject):
    '''

    '''

    def __init__(self, box: Box, windowSize: numpy.ndarray):
        GameObject.__init__(self, box)

        self.windowSize: numpy.ndarray = windowSize

        self.position: float = .5
        self.width: float = self.realH / self.windowSize[1]
        self.velocity: float = 0

        self.lastTime: float = timeFunction()

    def _setValues(self):

        self.bufferCanvas.backgroundColors[:,:] = numpy.array([255, 180, 180], dtype = numpy.uint8)
    
    def update(self):

        newTime = timeFunction()
        timeElapsed = newTime - self.lastTime
        self.lastTime = newTime

        self.position = self.position + self.velocity * timeElapsed

        if self.position < 0:
            self.position = 0
            self.velocity = 0

        
        if self.position > 1.0:
            self.position = 1.0
            self.velocity = 0
        
        self.realY = numpy.round(self.position * (self.windowSize[1] - self.realH)).astype(numpy.int16)

class PlayerPaddle(Paddle):
    '''

    '''

    def __init__(self, box: Box, windowSize: numpy.ndarray):
        Paddle.__init__(self, box, windowSize)

    def _onEvent(self, event: Event):

        if event.keyName == "UP" and self.realY > 0:
            self.velocity -= .3
        if event.keyName == "DOWN" and self.realY + self.realH < self.windowSize[1] - 1:
            self.velocity += .3

class EnemyPaddle(Paddle):
    '''

    '''

    def __init__(self, box: Box, windowSize: numpy.ndarray):
        Paddle.__init__(self, box, windowSize)