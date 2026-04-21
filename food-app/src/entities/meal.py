class Meal:
    """ Luokka joka sisältää yksittäisen aterian """

    def __init__(self, name, calories, carbs, protein, fat):
        """ Luo uuden aterian """
        self.name = name
        self.calories = calories
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
