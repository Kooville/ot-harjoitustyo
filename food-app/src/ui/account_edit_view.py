from tkinter import ttk, constants, StringVar
from ui.style import init_styles
from services.diary_service import diary_service


class AccountEditView:
    """ Käyttöliittymä käyttäjän tietojen näkymälle """

    def __init__(self, root, main_menu_view):
        self._root = root
        self._user = diary_service.get_current_user()
        self._main_menu_view = main_menu_view
        self._style = init_styles()
        self._frame = None
        self._error_variable = StringVar()
        self._error_label = None
        self._username_entry = None
        self._goal_calories_entry = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _save_changes(self):
        self._error_variable.set("")
        self._error_label.grid_remove()
        new_username = self._username_entry.get()
        new_goal_calories = self._goal_calories_entry.get()

        try:
            diary_service.update_user_info(
                new_username,
                new_goal_calories
            )
            self._main_menu_view()
        except ValueError as error:
            self._error_variable.set(str(error))

            self._error_label.grid(
                row=5,
                column=0,
                columnspan=2,
                pady=10
            )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root, style="TFrame")

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)

        back_button = ttk.Button(
            master=self._frame,
            text="←",
            command=self._main_menu_view,
            style="TButton"
        )

        back_button.grid(
            row=0,
            column=0,
            sticky=constants.W,
            padx=10,
            pady=10
        )

        label = ttk.Label(master=self._frame,
                          text=f"Käyttäjän {self._user.username} tiedot",
                          anchor="center",
                          style="Title.TLabel"
                          )
        label.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=(50, 50)
        )

        self._container = ttk.Frame(
            master=self._frame,
            style="TFrame"
        )
        self._container.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="n"
        )

        username_label = ttk.Label(
            master=self._container,
            text="Käyttäjätunnus:",
            style="TLabel"
        )
        username_label.grid(
            row=0,
            column=0,
            sticky=constants.W,
            padx=10,
            pady=10
        )
        self._username_entry = ttk.Entry(
            master=self._container,
            width=30,
            style="TEntry"
        )
        self._username_entry.grid(
            row=0,
            column=1,
            sticky=constants.EW,
            padx=10,
            pady=10
        )
        self._username_entry.insert(0, self._user.username)

        goal_calories_label = ttk.Label(
            master=self._container,
            text="Tavoitekalorit:",
            style="TLabel"
        )
        goal_calories_label.grid(
            row=1,
            column=0,
            sticky=constants.W,
            padx=10,
            pady=10
        )
        self._goal_calories_entry = ttk.Entry(
            master=self._container,
            width=30,
            style="TEntry"
        )
        self._goal_calories_entry.grid(
            row=1,
            column=1,
            sticky=constants.EW,
            padx=10,
            pady=10
        )
        self._goal_calories_entry.insert(0, self._user.goal_calories)

        save_button = ttk.Button(
            master=self._container,
            text="Tallenna",
            style="TButton",
            command=self._save_changes
        )
        save_button.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=20
        )

        self._error_label = ttk.Label(
            master=self._container,
            textvariable=self._error_variable,
            style="Error.TLabel"
        )
