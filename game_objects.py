import pyray
from math import sqrt


class GameObject:
    __directions = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0),
        "up_left": (-1 / sqrt(2), -1 / sqrt(2)),
        "up_right": (1 / sqrt(2), -1 / sqrt(2)),
        "down_left": (-1 / sqrt(2), 1 / sqrt(2)),
        "down_right": (1 / sqrt(2), 1 / sqrt(2)),
        "stop": (0, 0)
    }

    def __init__(
            self,
            x: int, y: int,
            color: pyray.Color,
            speed: int = 0, direction: str = "stop"
    ) -> None:
        self._x = self._real_x = x
        self._y = self._real_y = y
        self._color = color
        self._speed = speed

        if direction in GameObject.__directions:
            self._x_direction, self._y_direction = GameObject.__directions[direction]
        else:
            raise ValueError("Неправильно указано направление")
        self._direction = direction

    def set_x(self, x: int) -> None:
        self._x = self._real_x = x

    def get_x(self) -> int:
        return self._x

    def get_real_x(self) -> int | float:
        return self._real_x

    def set_y(self, y: int) -> None:
        self._y = self._real_y = y

    def get_y(self) -> int:
        return self._y

    def get_real_y(self) -> int | float:
        return self._real_y

    def set_x_y(self, x: int | float, y: int | float) -> None:
        self._real_x = x
        self._x = int(x)
        self._real_y = y
        self._y = int(y)

    def get_x_y(self) -> tuple:
        return self._x, self._y

    def get_real_x_y(self) -> tuple:
        return self._real_x, self._real_y

    def set_color(self, color: pyray.Color) -> None:
        self._color = color

    def set_speed(self, speed: int) -> None:
        self._speed = speed

    def set_direction(self, direction: str) -> None:
        if direction in GameObject.__directions:
            self._x_direction, self._y_direction = GameObject.__directions[direction]
        else:
            raise ValueError("Неверно указано направление")
        self._direction = direction

    def get_direction(self) -> str:
        return self._direction

    def move(self, dt: float) -> None:
        self._real_x += self._speed * self._x_direction * dt
        self._x = int(self._real_x)
        self._real_y += self._speed * self._y_direction * dt
        self._y = int(self._real_y)

    def draw(self) -> None:
        pass


class GameObjectRectangle(GameObject):
    def __init__(
            self,
            x: int, y: int,
            width: int, height: int,
            color: pyray.Color,
            speed: int = 0, direction: str = "stop"
    ) -> None:
        super().__init__(x, y, color, speed, direction)

        self._width = width
        self._height = height

        self._half_width = width // 2
        self._half_height = height // 2

    def set_width(self, width: int) -> None:
        self._width = width
        self._half_width = width // 2

    def get_width(self) -> int:
        return self._width

    def get_half_width(self) -> int:
        return self._half_width

    def set_height(self, height: int) -> None:
        self._height = height
        self._half_height = height // 2

    def get_height(self) -> int:
        return self._height

    def get_half_height(self) -> int:
        return self._half_height

    def draw(self) -> None:
        pyray.draw_rectangle(self._x, self._y, self._width, self._height, self._color)


class GameObjectCircle(GameObject):
    def __init__(
            self,
            x: int, y: int,
            r: int,
            color: pyray.Color,
            speed: int = 0, direction: str = "stop"
    ) -> None:
        super().__init__(x, y, color, speed, direction)

        self._r = r

    def set_r(self, r: int) -> None:
        self._r = r

    def get_r(self) -> int:
        return self._r

    def draw(self) -> None:
        pyray.draw_circle(self._x, self._y, self._r, self._color)
