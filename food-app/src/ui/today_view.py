from tkinter import ttk, constants
from services.diary_service import diary_service
from ui.components.all_meals_list import AllMealsList
from ui.style import init_styles
from datetime import datetime


class TodayView:
    """ Käyttöliittymä nykyisen päivän näkymälle """

    def __init__(self, root, show_main_menu, show_create_meal_view):
        self._root = root
        self._frame = None
        self._style = init_styles()
        self._date = datetime.now().strftime("%d.%m.%Y")

        self._show_main_menu = show_main_menu
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
        self._meals_list.get_frame().grid(row=1, column=1, sticky="nsew")

    def _on_meal_select(self, meal_id):
        self._selected_meal_id = meal_id
        self._choice_button.config(state="normal")

    def _clear_selection(self):
        self._selected_meal_id = None
        self._choice_button.config(state="disabled")

    def _choose_selected_meal(self):
        if not self._selected_meal_id:
            return

        meal_id = self._selected_meal_id
        

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

        self._container = ttk.Frame(self._frame, style="TFrame")
        self._container.grid(row=2, column=0, sticky="nsew")

        title_label = ttk.Label(
            master=self._container,
            text=f"Tänään {self._date}",
            style="TLabel"
        )

        title_label.grid(
            row=0,
            column=0,
            pady=(100, 50)
        )


        self._initialize_meals_list()

        button_frame = ttk.Frame(self._container, style="TFrame")
        button_frame.grid(row=1, column=2, sticky="n", padx=0, pady=0)
        
        self._choice_button = ttk.Button(
            button_frame,
            text="Valitse ateria",
            style="Card.TButton",
            command=self._choose_selected_meal,
            state="disabled"
        )
        self._choice_button.grid(
            row=0,
            column=0,
            columnspan=1,
            sticky=constants.NW,
            padx=10,
            pady=5
        )
