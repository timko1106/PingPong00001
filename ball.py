import pyray
from raylib import colors

from game_objects import GameObjectCircle


class Ball(GameObjectCircle):
    def __init__(
            self,
            x: int = 0, y: int = 0,
            r: int = 10,
            color: pyray.Color = colors.WHITE,
            speed: int = 200, direction: str = "stop"
    ) -> None:
        super().__init__(x, y, r, color, speed, direction)
