from TGL.internal import GameObject, Box, timeFunction

import numpy

class Ball(GameObject):
    '''

    '''

    def __init__(self, box: Box, windowSize: numpy.ndarray):
        GameObject.__init__(self, box)
    
        self.velocity: numpy.ndarray = numpy.array([.1, .2])
        self.lastTime: float = timeFunction()

        self.position: numpy.ndarray = numpy.array([.5, .5])

        self.windowSize: numpy.ndarray = windowSize

    def _setValues(self):

        self.bufferCanvas.backgroundColors.fill(255)
    
    def update(self):

        newTime = timeFunction()
        timeElapsed = newTime - self.lastTime
        self.lastTime = newTime

        self.position = self.position + self.velocity * timeElapsed

        if self.position[0] < 0:
            self.position[0] = -self.position[0]
            self.velocity[0] = -self.velocity[0]
        if self.position[1] < 0:
            self.position[1] = -self.position[1]
            self.velocity[1] = -self.velocity[1]
        
        if self.position[0] > 1.0:
            self.position[0] = 2 - self.position[0]
            self.velocity[0] = -self.velocity[0]
        if self.position[1] > 1.0:
            self.position[1] = 2 - self.position[1]
            self.velocity[1] = -self.velocity[1]
        
        screenPosition = numpy.round(self.position * (self.windowSize - numpy.array([2, 1]))).astype(numpy.int16)
        self.realX, self.realY = screenPosition[0], screenPosition[1]