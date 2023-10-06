import pyray
from raylib import colors

from game_objects import GameObjectRectangle


class PlayerBlock(GameObjectRectangle):
    def __init__(
            self,
            x: int = 0, y: int = 0,
            width: int = 20, height: int = 200,
            color: pyray.Color = colors.WHITE,
            speed: int = 100, direction: str = "stop"
    ) -> None:
        super().__init__(x, y, width, height, color, speed, direction)
