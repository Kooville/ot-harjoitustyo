from tkinter import ttk, constants
from ui.style import init_styles

class StartView:
    """ Käyttöliittymä sovelluksen aloitussivulle  """

    def __init__(self, root, handle_create_user_click):
        self._root = root
        self._handle_create_user_click = handle_create_user_click
        self._style = init_styles()
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root, style="TFrame")
        

        label = ttk.Label(master=self._frame,
                          text="Tervetuloa käyttämään ruokapäiväkirjaa!",
                          anchor="center"
                          )
        button = ttk.Button(
            master=self._frame,
            text="Luo uusi käyttäjä",
            command=self._handle_create_user_click
        )
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_rowconfigure(3, weight=1)

        label.grid(row=1,
                   column=0,
                   sticky=constants.EW,
                   padx=20,
                   pady=10
                   )

        button.grid(row=2,
                    column=0,
                    sticky=constants.EW,
                    padx=20,
                    pady=10
                    )

        self._frame.grid_columnconfigure(0, weight=1)
