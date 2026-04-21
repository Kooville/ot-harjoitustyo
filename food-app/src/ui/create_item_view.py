from tkinter import ttk, constants, StringVar
from services.diary_service import diary_service
from ui.style import init_styles


class CreateItemView:
    """ Käyttöliittymä uuden ruoka-aineen luonnille """

    def __init__(self, root, show_main_menu):
        self._root = root
        self._frame = None
        self._style = init_styles()
        self._name_entry = None
        self._calories_entry = None
        self._carbs_entry = None
        self._protein_entry = None
        self._fat_entry = None
        self._error_variable = None
        self._show_main_menu = show_main_menu

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _handle_create_item_click(self):
        self._error_variable.set("")
        name = self._name_entry.get()
        calories = self._calories_entry.get()
        carbs = self._carbs_entry.get()
        protein = self._protein_entry.get()
        fat = self._fat_entry.get()

        try:
            diary_service.create_item(name,
                                      calories,
                                      carbs,
                                      protein,
                                      fat
                                      )
            self._show_main_menu()

        except ValueError as error:
            self._error_variable.set(str(error))

    def _initialize_name_field(self):
        name_label = ttk.Label(master=self._container,
                               text="Nimi",
                               style="Card.TLabel"
                               )

        self._name_entry = ttk.Entry(master=self._container)

        name_label.grid(row=0,
                        column=0,
                        sticky=constants.W,
                        padx=20,
                        pady=10
                        )

        self._name_entry.grid(row=0,
                              column=1,
                              sticky=constants.EW,
                              padx=20,
                              pady=10
                              )

    def _initialize_calories_field(self):
        calories_label = ttk.Label(master=self._container,
                                   text="Kalorit / 100g",
                                   style="Card.TLabel"
                                   )

        self._calories_entry = ttk.Entry(master=self._container)

        calories_label.grid(row=1,
                            column=0,
                            sticky=constants.W,
                            padx=20,
                            pady=10
                            )

        self._calories_entry.grid(row=1,
                                  column=1,
                                  sticky=constants.EW,
                                  padx=20,
                                  pady=10
                                  )

    def _initialize_carbs_field(self):
        carbs_label = ttk.Label(master=self._container,
                                text="Hiilihydraatit / 100g",
                                style="Card.TLabel"
                                )

        self._carbs_entry = ttk.Entry(master=self._container)

        carbs_label.grid(row=2,
                         column=0,
                         sticky=constants.W,
                         padx=20,
                         pady=10
                         )

        self._carbs_entry.grid(row=2,
                               column=1,
                               sticky=constants.EW,
                               padx=20,
                               pady=10
                               )

    def _initialize_protein_field(self):
        protein_label = ttk.Label(master=self._container,
                                  text="Proteiinit / 100g",
                                  style="Card.TLabel"
                                  )

        self._protein_entry = ttk.Entry(master=self._container)

        protein_label.grid(row=3,
                           column=0,
                           sticky=constants.W,
                           padx=20,
                           pady=10
                           )

        self._protein_entry.grid(row=3,
                                 column=1,
                                 sticky=constants.EW,
                                 padx=20,
                                 pady=10
                                 )

    def _initialize_fat_field(self):
        fat_label = ttk.Label(master=self._container,
                              text="Rasvaa / 100g",
                              style="Card.TLabel"
                              )

        self._fat_entry = ttk.Entry(master=self._container)

        fat_label.grid(row=4,
                       column=0,
                       sticky=constants.W,
                       padx=20,
                       pady=10
                       )

        self._fat_entry.grid(row=4,
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
        command=self._show_main_menu,
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
            text="Lisää uusi ruoka-aine",
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

        self._initialize_name_field()
        self._initialize_calories_field()
        self._initialize_carbs_field()
        self._initialize_protein_field()
        self._initialize_fat_field()

        self._error_variable = StringVar()

        create_item_button = ttk.Button(
            master=self._container,
            text="Lisää ruoka-aine",
            command=self._handle_create_item_click,
            style="Card.TButton"
        )

        create_item_button.grid(row=5,
                                column=0,
                                columnspan=2,
                                sticky=constants.EW,
                                padx=20,
                                pady=20,
                                )

        error_label = ttk.Label(
            master=self._container,
            textvariable=self._error_variable,
            style="CardError.TLabel"
        )
        error_label.grid(row=6,
                         column=0,
                         columnspan=2,
                         sticky=constants.W,
                         padx=20,
                         pady=10
                         )

        self._container.grid_columnconfigure(0, weight=1)
        self._container.grid_columnconfigure(1, weight=1)
