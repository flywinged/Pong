from TGL.internal import GameObject, Box

class Ball(GameObject):
    '''

    '''

    def __init__(self, box: Box):
        GameObject.__init__(self, box)
    
    def _setValues(self):
        self.bufferCanvas.backgroundColors.fill(255)