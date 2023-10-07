import pyray
from raylib import colors

import game_objects

class PlayerBlock(game_objects.GameObjectRectangle):
    def __init__(
            self,
            x: int = 0, y: int = 0,
            width: int = 20, height: int = 200,
            color: pyray.Color = colors.WHITE,
            speed: int = 100, direction: game_objects.Directions = game_objects.UP
    ) -> None:
        super().__init__(x, y, width, height, color, speed, direction)
