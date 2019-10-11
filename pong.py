from TGL import Window

from objects.ball import Ball

from TGL.internal import Box

import numpy

if __name__ == "__main__":

    w = Window((160, 41))

    ball = Ball(Box(79, 20, 2, 1), numpy.array([160, 41]))

    w.addGameObject(ball)

    w.gameLoop()