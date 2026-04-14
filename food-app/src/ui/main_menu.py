from tkinter import ttk, constants
from ui.style import init_styles
from services.diary_service import diary_service


class MainMenu:
    """ Käyttöliittymä sovelluksen päävalikolle """

    def __init__(self, root, start_view, create_item_view):
        self._root = root
        self._user = diary_service.get_current_user()
        self._handle_view_todays_entries = None
        self.start_view = start_view
        self.create_item_view = create_item_view
        self._style = init_styles()
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _handle_logout_click(self):
        diary_service.logout()
        self.start_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root, style="TFrame")

        label = ttk.Label(master=self._frame,
                          text=f"Tervetuloa käyttämään ruokapäiväkirjaa {self._user.username}!",
                          anchor="center"
                          )
        todays_entries_button = ttk.Button(
            master=self._frame,
            text="Tämän päivän tiedot",
            command=self._handle_view_todays_entries
        )
        create_item_button = ttk.Button(
            master=self._frame,
            text="Luo ruoka-aine",
            command=self.create_item_view
        )
        logout_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command=self._handle_logout_click
        )
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_rowconfigure(5, weight=1)

        label.grid(row=1,
                   column=0,
                   sticky=constants.EW,
                   padx=20,
                   pady=10
                   )

        todays_entries_button.grid(row=2,
                                   column=0,
                                   sticky=constants.EW,
                                   padx=20,
                                   pady=10
                                   )

        create_item_button.grid(row=3,
                                column=0,
                                sticky=constants.EW,
                                padx=20,
                                pady=10
                                 )

        logout_button.grid(row=4,
                           column=0,
                           sticky=constants.EW,
                           padx=20,
                           pady=10
                           )

        self._frame.grid_columnconfigure(0, weight=1)
