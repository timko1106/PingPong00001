import pyray

#Базовый класс окна.
class App:
    #Конструктор: принимает ширину,высоту,название и фон
    def __init__(self, width: int, height: int, title: str, bg_color: pyray.Color) -> None:
        self._WINDOW_WIDTH = width
        self._WINDOW_HEIGHT = height
        self._WINDOW_TITLE = title
        self._window_bg_color = bg_color

        self._dt = int(0)

        pyray.init_window(self._WINDOW_WIDTH, self._WINDOW_HEIGHT, self._WINDOW_TITLE)
    #Уничтожение окна (альтернатива free)
    def __del__(self) -> None:
        pyray.close_window()
    #Динамическое изменение цвета окна
    def set_bg_color(self, color: pyray.Color) -> None:
        self._window_bg_color = color

    def run(self) -> None:
        try:
            while not pyray.window_should_close():
                self._check_events()
                self._check_logic()
                self._draw()
        except KeyboardInterrupt:
            #Обработка пользовательских прерываний
            print ("Interrupted by user")

    def _check_events(self) -> None:
        pass

    def _check_logic(self) -> None:
        self._dt = pyray.get_frame_time()

    def _draw(self) -> None:
        pass

    def _draw_background(self) -> None:
        pyray.clear_background(self._window_bg_color)
