from TGL import Window

from objects.ball import Ball
from objects.paddle import PlayerPaddle, EnemyPaddle

from TGL.internal import Box

import numpy

if __name__ == "__main__":

    w = Window((160, 41))

    ball = Ball(Box(79, 20, 2, 1), numpy.array([160, 41]))
    playerPaddle = PlayerPaddle(Box(0, 17, 1, 7), numpy.array([160, 41]))
    enemyPaddle = EnemyPaddle(Box(159, 17, 1, 7), numpy.array([160, 41]))

    w.addGameObject(ball)
    w.addGameObject(playerPaddle)
    w.addGameObject(enemyPaddle)

    w.rootGameObject = playerPaddle

    w.gameLoop()