from tkinter import ttk, constants, StringVar, BooleanVar
from services.diary_service import diary_service
from ui.style import init_styles


class CreateMealView:
    """ Käyttöliittymä uuden aterian luonnille """

    def __init__(self, root, show_all_meals_view):
        self._root = root
        self._frame = None
        self._style = init_styles()
        self._name_entry = None
        self._items = diary_service.get_all_items()
        self._show_all_meals_view = show_all_meals_view
        self._item_vars = {}  # item_name: (selected_var, amount_var)

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _handle_create_meal_click(self):
        self._error_variable.set("")
        name = self._name_entry.get()
        selected_items = []

        for item in self._items:
            selected_var, amount_var = self._item_vars[item.name]

            if selected_var.get():
                try:
                    amount = float(amount_var.get())
                    if amount <= 0:
                        raise ValueError(
                            "Määrän tulee olla positiivinen luku.")
                    selected_items.append((item, amount))
                except ValueError:
                    self._error_variable.set(
                        f"Virheellinen määrä ruoka-aineelle {item.name}.")
                    return

        try:
            diary_service.create_meal(name, selected_items)
            self._show_all_meals_view()

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

    def _initialize_choose_items_field(self):
        items_label = ttk.Label(master=self._container,
                                text="Valitse ruoka-aineet",
                                style="Card.TLabel"
                                )

        items_label.grid(row=1,
                         column=0,
                         sticky=constants.W,
                         padx=20,
                         pady=10
                         )

        for index, item in enumerate(self._items):
            selected_var = BooleanVar()
            amount_var = StringVar()

            self._item_vars[item.name] = (selected_var, amount_var)

            checkbox = ttk.Checkbutton(
                master=self._container,
                text=item.name,
                variable=selected_var
            )

            amount_frame = ttk.Frame(master=self._container)
            amount_label = ttk.Label(master=amount_frame, text="Määrä:")

            amount_entry = ttk.Entry(
                master=amount_frame,
                textvariable=amount_var,
                width=10
            )

            unit_label = ttk.Label(master=amount_frame, text="g")

            amount_label.pack(side="left")
            amount_entry.pack(side="left", padx=(5, 0))
            unit_label.pack(side="left")

            checkbox.grid(row=2 + index,
                          column=0,
                          sticky=constants.W,
                          padx=20,
                          pady=5
                          )
            amount_frame.grid(row=2 + index,
                              column=1,
                              sticky=constants.EW,
                              padx=20,
                              pady=5
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
            command=self._show_all_meals_view,
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
            text="Lisää uusi ateria",
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
        self._initialize_choose_items_field()

        self._error_variable = StringVar()

        create_meal_button = ttk.Button(
            master=self._container,
            text="Lisää ateria",
            command=self._handle_create_meal_click,
            style="Card.TButton"
        )

        create_meal_button.grid(row=5,
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
