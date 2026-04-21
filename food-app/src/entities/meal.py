class Meal:
    """ Luokka joka sisältää yksittäisen aterian """

    def __init__(self, name, items: list):
        """ Luo uuden aterian """
        self.name = name
        self.items = items
        self.calories = sum(item.calories for item in items)
        self.carbs = sum(item.carbs for item in items)
        self.protein = sum(item.protein for item in items)
        self.fat = sum(item.fat for item in items)
