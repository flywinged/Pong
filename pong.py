from TGL import Window

from objects.ball import Ball

from TGL.internal import Box

if __name__ == "__main__":

    w = Window((160, 41))

    ball = Ball(Box(79, 20, 2, 1))

    w.addGameObject(ball)

    w.gameLoop()