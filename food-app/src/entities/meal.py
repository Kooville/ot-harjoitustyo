class Meal:
    """ Luokka joka sisältää yksittäisen aterian 

    Attributes:
        name: Aterian nimi
        calories: Aterian kalorimäärä
        carbs: Aterian hiilihydraattimäärä
        protein: Aterian proteiinimäärä
        fat: Aterian rasvamäärä
        meal_id: Aterian id tietokannassa
    """

    def __init__(self, name, calories, carbs, protein, fat, meal_id=None):
        """ Luokan konstruktori, joka luo uuden aterian 

        Args:
            name: Aterian nimi
            calories: Aterian kalorimäärä
            carbs: Aterian hiilihydraattimäärä
            protein: Aterian proteiinimäärä
            fat: Aterian rasvamäärä
            meal_id: Aterian id tietokannassa, oletuksena None
        """

        self.name = name
        self.calories = calories
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
        self.id = meal_id
