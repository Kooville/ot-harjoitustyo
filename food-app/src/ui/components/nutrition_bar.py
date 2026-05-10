import tkinter as tk

class NutritionBar(tk.Canvas):
    """ Näyttää ravintoaineiden osuudet kalorimäärästä visuaalisesti """
    def __init__(self, master, height=25, **kwargs):
        super().__init__(
            master,
            height=height,
            bg="white",
            highlightthickness=0,
            **kwargs
        )

        self._protein = 0
        self._carbs = 0
        self._fat = 0
        self._goal = 1

        self.bind("<Configure>", lambda e: self.after_idle(self._draw))

    def update_data(self, protein, carbs, fat):
        self._protein = protein
        self._carbs = carbs
        self._fat = fat

        self.after_idle(self._draw)

    def _draw(self):
        self.delete("all")

        if self._goal <= 0:
            return

        width = self.winfo_width()

        if width <= 1:
            self.after(10, self._draw)
            return

        total = self._protein + self._carbs + self._fat

        if total <= 0:
            return

        x = 0

        def draw(amount, color, text):
            nonlocal x
            w = (amount / total) * width

            self.create_rectangle(
                x, 0, x + w, 25,
                fill=color,
                outline=""
            )
            if w > 50:
                self.create_text(
                    x + w / 2,
                    12,
                    text=f"{text}: {amount}g",
                    fill="white",
                    font=("Arial", 10, "bold")
                )

            x += w

        draw(self._protein, "#E53935", "Proteiini")
        draw(self._carbs, "#43A047", "Hiilihydraatti")
        draw(self._fat, "#FB8C00", "Rasva")
