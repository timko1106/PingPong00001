import pyray


class App:
    def __init__(self, width: int, height: int, title: str, bg_color: pyray.Color) -> None:
        self._WINDOW_WIDTH = width
        self._WINDOW_HEIGHT = height
        self._WINDOW_TITLE = title
        self._window_bg_color = bg_color

        self._dt = int()

        pyray.init_window(self._WINDOW_WIDTH, self._WINDOW_HEIGHT, self._WINDOW_TITLE)

    def __del__(self) -> None:
        pyray.close_window()

    def set_bg_color(self, color: pyray.Color) -> None:
        self._window_bg_color = color

    def run(self) -> None:
        while not pyray.window_should_close():
            self._check_events()
            self._check_logic()
            self._draw()

    def _check_events(self) -> None:
        pass

    def _check_logic(self) -> None:
        self._dt = pyray.get_frame_time()

    def _draw(self) -> None:
        pass

    def _draw_background(self) -> None:
        pyray.clear_background(self._window_bg_color)
