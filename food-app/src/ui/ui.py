from ui.create_user_view import CreateUserView
from ui.start_view import StartView
from ui.main_menu import MainMenu
class UI:
    """ Käyttöliittymästä vastaava luokka """

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        """ Käynnistää käyttöliittymän """
        self._show_start_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_start_view(self):
        self._hide_current_view()

        self._current_view = StartView(self._root, self._show_create_user_view)
        self._current_view.pack()

    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateUserView(self._root, self._show_main_menu)
        self._current_view.pack()

    def _show_main_menu(self, user):
        self._hide_current_view()

        self._current_view = MainMenu(self._root, user)
        self._current_view.pack()
