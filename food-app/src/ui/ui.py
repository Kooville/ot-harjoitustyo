from ui.create_user_view import CreateUserView
from ui.login_view import LoginView
from ui.start_view import StartView
from ui.create_item_view import CreateItemView
from ui.create_meal_view import CreateMealView
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

        self._current_view = StartView(
            self._root, self._show_create_user_view, self._show_login_view)
        self._current_view.pack()

    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateUserView(self._root, self._show_main_menu, self._show_start_view)
        self._current_view.pack()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(self._root, self._show_main_menu, self._show_start_view)
        self._current_view.pack()

    def _show_main_menu(self):
        self._hide_current_view()

        self._current_view = MainMenu(self._root,
                                      self._show_start_view,
                                      self._show_create_meal_view,
                                      self._show_create_item_view
                                      )
        self._current_view.pack()

    def _show_create_meal_view(self):
        self._hide_current_view()

        self._current_view = CreateMealView(self._root, self._show_main_menu)
        self._current_view.pack()

    def _show_create_item_view(self):
        self._hide_current_view()

        self._current_view = CreateItemView(self._root, self._show_main_menu)
        self._current_view.pack()
