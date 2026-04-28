from tkinter import ttk
from ui.style import init_styles


class AllMealsList:
    """ Aterioiden listaus, jota muut näkymät voivat käyttää """

    def __init__(self, parent, meals, on_select=None):
        self._parent = parent
        self._style = init_styles()

        self._frame = ttk.Frame(parent, style="TFrame")
        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)
        
        self._meals = meals
        self._on_select_callback = on_select
        self._tree = None

        self._initialize()

    def get_frame(self):
        return self._frame

    def _initialize(self):
            self._tree = ttk.Treeview(
                self._frame,
                columns=("name", "kcal", "carbs", "protein", "fat"),
                show="headings"
            )

            self._tree.heading("name", text="Nimi")
            self._tree.heading("kcal", text="Kcal")
            self._tree.heading("carbs", text="Hiilihydraatit")
            self._tree.heading("protein", text="Proteiini")
            self._tree.heading("fat", text="Rasva")

            self._tree.column("name", width=150)
            self._tree.column("kcal", width=100)
            self._tree.column("carbs", width=100)
            self._tree.column("protein", width=100)
            self._tree.column("fat", width=100)

            self._tree.grid(row=0, column=0, sticky="nsew")

            for meal in self._meals:
                self._tree.insert(
                    "",
                    "end",
                    iid=str(meal.id),
                    values=(meal.name, meal.calories, meal.carbs, meal.protein, meal.fat)
                )

            self._tree.bind("<<TreeviewSelect>>", self._on_meal_select)
   
    def _on_meal_select(self, event):
        selected_item = self._tree.selection()
        if selected_item:
            meal_id = selected_item[0]

            if self._on_select_callback:
                self._on_select_callback(meal_id)

    def get_selected_meal_id(self):
        selected_item = self._tree.selection()
        if selected_item:
            return selected_item[0]
        return None
    
    def delete_meal(self, meal_id):
        self._tree.delete(meal_id)
