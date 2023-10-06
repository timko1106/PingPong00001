import random

import pyray
from raylib import colors

from app import App
from ball import Ball
from player_block import PlayerBlock


class AppPong(App):
    def __init__(
            self,
            width: int = 720, height: int = 480,
            title: str = "PONG",
            bg_color: pyray.Color = colors.BLACK
    ) -> None:
        super().__init__(width, height, title, bg_color)

        # Тут задаём значения не сразу, так как нужно получить размеры объекта
        self.__left_player = PlayerBlock()
        self.__left_player.set_y(self._WINDOW_HEIGHT // 2 - self.__left_player.get_height() // 2)
        self.__right_player = PlayerBlock()
        self.__right_player.set_x_y(
            self._WINDOW_WIDTH - self.__right_player.get_width(),
            self._WINDOW_HEIGHT // 2 - self.__right_player.get_height() // 2
        )

        self.__ball = Ball(x=self._WINDOW_WIDTH // 2, y=self._WINDOW_HEIGHT // 2)
        # выбираем случайное направления старта
        self.__ball.set_direction(("up_left", "up_right", "down_left", "down_right")[random.randint(0, 3)])

    def _check_logic(self) -> None:
        super()._check_logic()

        # куда двигаются игроки
        if self.__left_player.get_y() + self.__left_player.get_half_height() > self.__ball.get_y():
            self.__left_player.set_direction("up")
        elif self.__left_player.get_y() + self.__left_player.get_half_height() < self.__ball.get_y():
            self.__left_player.set_direction("down")
        else:
            self.__left_player.set_direction("stop")
        if self.__right_player.get_y() + self.__right_player.get_half_height() > self.__ball.get_y():
            self.__right_player.set_direction("up")
        elif self.__right_player.get_y() + self.__right_player.get_half_height() < self.__ball.get_y():
            self.__right_player.set_direction("down")
        else:
            self.__right_player.set_direction("stop")

        # Коллизии
        if self.__left_player.get_y() <= 0:
            self.__left_player.set_y(0)
        elif self.__left_player.get_y() + self.__left_player.get_height() >= self._WINDOW_HEIGHT:
            self.__left_player.set_y(self._WINDOW_HEIGHT - self.__left_player.get_height())
        if self.__right_player.get_y() <= 0:
            self.__right_player.set_y(0)
        elif self.__right_player.get_y() + self.__right_player.get_height() >= self._WINDOW_HEIGHT:
            self.__right_player.set_y(self._WINDOW_HEIGHT - self.__right_player.get_height())
        if self.__ball.get_y() - self.__ball.get_r() <= 0:
            self.__ball.set_y(self.__ball.get_r())
            self.__ball.set_direction("down_left" if self.__ball.get_direction() == "up_left" else "down_right")
        elif self.__ball.get_y() + self.__ball.get_r() >= self._WINDOW_HEIGHT:
            self.__ball.set_y(self._WINDOW_HEIGHT - self.__ball.get_r())
            self.__ball.set_direction("up_left" if self.__ball.get_direction() == "down_left" else "up_right")
        # if self.__ball.get_x() - self.__ball.get_r() <= self.__left_player.get_width() and \
        #         (
        #                 self.__ball.get_y() - self.__ball.get_r() >= self.__left_player.get_y() or
        #                 self.__ball)

        self.__left_player.move(self._dt)
        self.__right_player.move(self._dt)
        self.__ball.move(self._dt)

    def _draw(self) -> None:
        pyray.begin_drawing()

        self._draw_background()
        self.__left_player.draw()
        self.__right_player.draw()
        self.__ball.draw()

        pyray.end_drawing()
