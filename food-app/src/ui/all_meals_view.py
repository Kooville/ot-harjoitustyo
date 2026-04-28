from tkinter import ttk, constants
from services.diary_service import diary_service
from ui.components.all_meals_list import AllMealsList
from ui.style import init_styles


class AllMealsView:
    """ Käyttöliittymä aterioiden näkymälle """

    def __init__(self, root, show_main_menu, show_create_meal_view):
        self._root = root
        self._frame = None
        self._style = init_styles()

        self._show_main_menu = show_main_menu
        self._show_create_meal_view = show_create_meal_view
        self._meals_list = None
        self._selected_meal_id = None

        self._meals = diary_service.get_all_meals()
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize_meals_list(self):
        self._meals_list = AllMealsList(
            self._container,
            self._meals,
            self._on_meal_select
        )
        self._meals_list.get_frame().grid(row=0, column=0, sticky="nsew")

    def _on_meal_select(self, meal_id):
        self._selected_meal_id = meal_id
        self._delete_button.config(state="normal")

    def _clear_selection(self):
        self._selected_meal_id = None
        self._delete_button.config(state="disabled")

    def _delete_selected_meal(self):
        if not self._selected_meal_id:
            return

        meal_id = self._selected_meal_id
        diary_service.delete_meal(int(meal_id))
        self._meals = [meal for meal in self._meals if str(meal.id) != meal_id]
        self._meals_list.delete_meal(meal_id)
        self._clear_selection()

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
                              style="TFrame"
                              )
        container.grid(row=2, column=0, sticky="n")
        self._container = container

        self._initialize_meals_list()

        button_frame = ttk.Frame(self._container, style="TFrame")
        button_frame.grid(row=0, column=1, sticky="n", padx=0, pady=0)

        create_meal_button = ttk.Button(
            master=button_frame,
            text="Lisää ateria",
            command=self._handle_create_meal_click,
            style="Card.TButton"
        )

        create_meal_button.grid(row=0,
                                column=0,
                                columnspan=1,
                                sticky=constants.NW,
                                padx=10,
                                pady=5
                                )

        self._delete_button = ttk.Button(
            button_frame,
            text="Poista ateria",
            style="Card.TButton",
            command=self._delete_selected_meal,
            state="disabled"
        )
        self._delete_button.grid(
            row=1,
            column=0,
            columnspan=1,
            sticky=constants.NW,
            padx=10,
            pady=5
        )

        self._container.grid_columnconfigure(0, weight=1)
        self._container.grid_columnconfigure(2, weight=1)
