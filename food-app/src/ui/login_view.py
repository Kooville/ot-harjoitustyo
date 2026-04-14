from tkinter import ttk, constants, StringVar
from services.diary_service import diary_service
from ui.style import init_styles


class LoginView:
    """ Käyttöliittymä sisäänkirjautumiseen """

    def __init__(self, root, show_main_menu, show_start_view):
        self._root = root
        self._frame = None
        self._style = init_styles()
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._show_main_menu = show_main_menu
        self._show_start_view = show_start_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _handle_login_click(self):
        self._error_variable.set("")
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            diary_service.login(username, password)
            self._show_main_menu()
        except ValueError as error:
            self._error_variable.set(str(error))

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._container,
                                   text="Käyttäjätunnus",
                                   style="Card.TLabel"
                                   )

        self._username_entry = ttk.Entry(master=self._container)

        username_label.grid(row=0,
                            column=0,
                            sticky=constants.W,
                            padx=20,
                            pady=10
                            )

        self._username_entry.grid(row=0,
                                  column=1,
                                  sticky=constants.EW,
                                  padx=20,
                                  pady=10
                                  )

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._container,
                                   text="Salasana",
                                   style="Card.TLabel"
                                   )

        self._password_entry = ttk.Entry(master=self._container,
                                         show="*"
                                         )

        password_label.grid(row=1,
                            column=0,
                            sticky=constants.W,
                            padx=20,
                            pady=10
                            )

        self._password_entry.grid(row=1,
                                  column=1,
                                  sticky=constants.EW,
                                  padx=20,
                                  pady=10
                                  )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root,
                                style="TFrame"
                                )
        self._frame.grid_rowconfigure(0, weight=0)
        self._frame.grid_rowconfigure(1, weight=0)
        self._frame.grid_rowconfigure(2, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)

        back_button = ttk.Button(
        master=self._frame,
        text="←",
        command=self._show_start_view,
        style="TButton"
        )

        back_button.grid(
        row=0,
        column=0,
        sticky=constants.W,
        padx=10,
        pady=10
        )

        title_label = ttk.Label(
            master=self._frame,
            text="Kirjaudu sisään",
            style="Title.TLabel"
        )

        title_label.grid(
            row=1,
            column=0,
            pady=(100, 50)
        )

        container = ttk.Frame(self._frame,
                              padding=30,
                              style="Card.TFrame"
                              )
        container.grid(row=2, column=0, sticky="n")
        self._container = container

        self._initialize_username_field()
        self._initialize_password_field()

        self._error_variable = StringVar()
        error_label = ttk.Label(
            master=self._container,
            textvariable=self._error_variable,
            style="CardError.TLabel"
        )
        error_label.grid(row=3,
                         column=0,
                         columnspan=2,
                         sticky=constants.W,
                         padx=20,
                         pady=10
                         )

        login_button = ttk.Button(
            master=self._container,
            text="Kirjaudu sisään",
            command=self._handle_login_click,
            style="Card.TButton"
        )

        login_button.grid(row=4,
                          column=0,
                          columnspan=2,
                          sticky=constants.EW,
                          padx=20,
                          pady=20,
                          )
        self._container.grid_columnconfigure(0, weight=1)
        self._container.grid_columnconfigure(1, weight=1)
