from tkinter import ttk, constants
from services.diary_service import diary_service
from ui.style import init_styles


class AllMealsView:
    """ Käyttöliittymä aterioiden näkymälle """

    def __init__(self, root, show_main_menu, show_create_meal_view):
        self._root = root
        self._frame = None
        self._style = init_styles()

        self._show_main_menu = show_main_menu
        self._show_create_meal_view = show_create_meal_view

        self._meals = diary_service.get_all_meals()
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize_meals_list(self):
        if not self._meals:
            no_meals_label = ttk.Label(
                master=self._container,
                text="Ei aterioita",
                style="Card.TLabel"
            )
            no_meals_label.grid(row=0, column=0, pady=20)
        else:
            for index, meal in enumerate(self._meals):
                meal_label = ttk.Label(
                    master=self._container,
                    text=f"{meal.name}: {meal.calories:.1f} kcal, "
                         f"{meal.carbs:.1f} g hiilihydraatteja, "
                         f"{meal.protein:.1f} g proteiinia, "
                         f"{meal.fat:.1f} g rasvaa",
                    style="Card.TLabel"
                )
                meal_label.grid(row=index, column=0, sticky="W", pady=10)

    def _handle_create_meal_click(self):
        self._show_create_meal_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root,
                                style="TFrame"
                                )

        self._frame.grid_rowconfigure(0, weight=0)
        self._frame.grid_rowconfigure(1, weight=0)
        self._frame.grid_rowconfigure(2, weight=0)
        self._frame.grid_rowconfigure(3, weight=0)
        self._frame.grid_rowconfigure(4, weight=1)
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
            text="Kaikki ateriat",
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

        self._initialize_meals_list()

        create_user_button = ttk.Button(
            master=self._container,
            text="Lisää ateria",
            command=self._handle_create_meal_click,
            style="Card.TButton"
        )

        create_user_button.grid(row=3,
                                column=0,
                                columnspan=2,
                                sticky=constants.EW,
                                padx=20,
                                pady=20,
                                )
        self._container.grid_columnconfigure(0, weight=1)
        self._container.grid_columnconfigure(1, weight=1)
