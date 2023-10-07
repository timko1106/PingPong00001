import random

import pyray
from raylib import colors

from app import App
from ball import Ball
from player_block import PlayerBlock
import game_objects
from game_objects import Directions, DOWN,UP,LEFT,RIGHT,DOWN_LEFT,DOWN_RIGHT,UP_LEFT,UP_RIGHT,STOP

#Класс приложения пинг-понга
class AppPong(App):
    def __init__(
            self,
            width: int = 720, height: int = 480,
            title: str = "PONG",
            bg_color: pyray.Color = colors.BLACK
    ) -> None:
        super().__init__(width, height, title, bg_color)
        # Тут задаём значения не сразу, так как нужно получить размеры объекта
        # В принципе логично. Не поспоришь
        self.__left_player = PlayerBlock()
        self.__left_player.set_y(self._WINDOW_HEIGHT // 2 - self.__left_player.get_height() // 2)
        self.__right_player = PlayerBlock()
        self.__right_player.set_x_y(
            self._WINDOW_WIDTH - self.__right_player.get_width(),
            self._WINDOW_HEIGHT // 2 - self.__right_player.get_height() // 2
        )

        self.__ball = Ball(x=self._WINDOW_WIDTH // 2, y=self._WINDOW_HEIGHT // 2)
        # выбираем случайное направления старта
        # псевдослучайное. Реальная случайность только в квантовой физике
        self.__ball.set_direction(random.choice([UP_LEFT,UP_RIGHT,DOWN_LEFT,DOWN_RIGHT]))
    #Проверка конкретного игрока на коллизии
    def __check_player (player : PlayerBlock, window_height : float, dt : float) -> None:
        py = player.get_y()
        if py <= 0:
            player.set_y (1)
            player.set_direction (DOWN)
        if py + player.get_height () >= window_height:
            player.set_direction (UP)
    #По формуле окружности. Кстати она выводится через пифагора
    def __intersect_circle (x0 : float, y0 : float, r : float, x : float, y : float) -> bool:
        return (x - x0) ** 2 + (y - y0) ** 2 <= r * r
    #Принадлежит ли точка квадрату.
    def __intersect_square (x0 : float, y0 : float, width : float, height : float, x : float, y : float) -> bool:
        return x >= x0 and x <= (x0 + width) and y >= y0 and y <= (y0 + height)
    #Проверка пересекаются ли квадрат и круг (квадрат : tuple((Ax,Ay),(Bx,By),(Cx,Cy),(Dx,Dy)))
    #circle_center = (Ox,Oy)
    def __intersects (circle_center : tuple, radius : float, square : tuple) -> bool:
        if AppPong.__intersect_square (*(square[0]), *(square[2][i] - square[0][i] for i in range (2)), *circle_center):
            return True
        if AppPong.__intersect_circle (*circle_center, radius, *(square[0])):
            return True
        if AppPong.__intersect_circle (*circle_center, radius, *(square[1])):
            return True
        if AppPong.__intersect_circle (*circle_center, radius, *(square[2])):
            return True
        if AppPong.__intersect_circle (*circle_center, radius, *(square[3])):
            return True
        return False
    #Проверка пересекаются ли круг и квадрат. Сделана дополнительно для упрощения
    #circle_center = (Ox,Oy)
    #begin = (Ax,Ay)
    #dimensions = (Cx-Ax,Cy-Ay)
    def __intersects_square_and_circle (circle_center : tuple, radius : float, begin : tuple, dimensions : tuple):
        return AppPong.__intersects (circle_center, radius, (begin,(begin[0] + dimensions[0],begin[1]), \
                (begin[0] + dimensions[0], begin[1] + dimensions[1]), \
                (begin[0],begin[1] + dimensions[1])))
    #Проверка коллизий мяча
    def __check_ball (self) -> None:
        bx,by = self.__ball.get_x(), self.__ball.get_y()
        br = self.__ball.get_r()
        wall1_x,wall1_y = self.__left_player.get_x(),self.__left_player.get_y ()
        wall2_x,wall2_y = self.__right_player.get_x(), self.__right_player.get_y ()
        wall_width, wall_height = self.__left_player.get_width(), self.__left_player.get_height ()
        direction = self.__ball._direction
        add = None#Новая директива для мяча. None-> не меняем
        if by + br <= 0:
            self.__ball.set_y (br + 1)
            add = (direction.dx (), -direction.dy())
        if by + br >= self._WINDOW_HEIGHT:
            self.__ball.set_y (self._WINDOW_HEIGHT - br - 1)
            add = (direction.dx (), -direction.dy ())
        if bx - br <= 0:
            self.__ball.set_x (br + 1)
            add = (-direction.dx(),direction.dy())
        elif bx - br <= wall1_x + wall_width:
            if AppPong.__intersects_square_and_circle ((bx, by), br, (wall1_x, wall1_y), (wall_width, wall_height)):
                self.__ball.set_x (wall1_x + wall_width + br)
                add = (-direction.dx(), direction.dy())
        if bx - br >= self._WINDOW_WIDTH:
            self.__ball.set_x (self._WINDOW_WIDTH - br - 1)
            add = (-direction.dx (), direction.dy ())
        elif bx + br >= wall2_x and AppPong.__intersects_square_and_circle ((bx,by), br, (wall2_x, wall2_y), (wall_width, wall_height)):
            self.__ball.set_x (wall2_x - br - 1)
            add = (-direction.dx (), direction.dy ())
        if not (add is None):
            self.__ball.set_direction (Directions (dx = add[0], dy = add[1]))
    #Проверка клавиатуры
    def __check_player_keyboard (up_key : int, down_key : int, player : PlayerBlock) -> None:
        if pyray.is_key_down(up_key):
            player.set_direction (UP)
        elif pyray.is_key_down(down_key):
            player.set_direction (DOWN)
    #Куда проще старой логики
    def _check_logic(self) -> None:
        super()._check_logic()
        AppPong.__check_player_keyboard (pyray.KeyboardKey.KEY_UP, pyray.KeyboardKey.KEY_DOWN, self.__right_player)
        AppPong.__check_player_keyboard (pyray.KeyboardKey.KEY_W, pyray.KeyboardKey.KEY_S, self.__left_player)
        # Коллизии
        AppPong.__check_player (self.__left_player, self._WINDOW_HEIGHT, self._dt)
        AppPong.__check_player (self.__right_player, self._WINDOW_HEIGHT, self._dt)
        self.__check_ball ()
        self.__left_player.move(self._dt)
        self.__right_player.move(self._dt)
        self.__ball.move(self._dt)
    #Отрисовка фона, блоков, мяча, FPS и instruction
    def _draw(self) -> None:
        pyray.begin_drawing()

        self._draw_background()
        self.__left_player.draw()
        self.__right_player.draw()
        self.__ball.draw()
        pyray.draw_text ("Press W/S to control left block,\n up and down keys for right block", 460, 410, 14, pyray.RED)
        pyray.draw_fps (600, 450)

        pyray.end_drawing()
