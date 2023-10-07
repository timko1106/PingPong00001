import pyray
from raylib import colors

import game_objects

#Гениально создавать классы, которые ничего не делают полезного
class Ball(game_objects.GameObjectCircle):
    def __init__(
            self,
            x: int = 0, y: int = 0,
            r: int = 10,
            color: pyray.Color = colors.WHITE,
            speed: int = 200, direction: game_objects.Directions = game_objects.STOP
    ) -> None:
        super().__init__(x, y, r, color, speed, direction)
