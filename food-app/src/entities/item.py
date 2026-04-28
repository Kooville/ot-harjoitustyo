class Item:
    """ Luokka joka sisältää yksittäisen ruoka-aineen """

    def __init__(self, name, calories, carbs, protein, fat, item_id=None):
        """ Luo uuden ruoka-aineen """
        self.name = name
        self.calories = calories
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
        self.id = item_id
