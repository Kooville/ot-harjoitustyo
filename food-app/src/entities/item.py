class Item:
    """ Luokka, joka sisältää yksittäisen ruoka-aineen.
     
      Attributes:
       name: Ruoka-aineen nimi
       calories: Ruoka-aineen kalorimäärä 100 grammassa
       carbs: Ruoka-aineen hiilihydraattimäärä 100 grammassa
       protein: Ruoka-aineen proteiinimäärä 100 grammassa
       fat: Ruoka-aineen rasvamäärä 100 grammassa
       item_id: Ruoka-aineen id tietokannassa
    """

    def __init__(self, name, calories, carbs, protein, fat, item_id=None):
        """ Luokan konstruktori, joka luo uuden ruoka-aineen
        Args:
            name: Ruoka-aineen nimi
            calories: Ruoka-aineen kalorimäärä 100 grammassa
            carbs: Ruoka-aineen hiilihydraattimäärä 100 grammassa
            protein: Ruoka-aineen proteiinimäärä 100 grammassa
            fat: Ruoka-aineen rasvamäärä 100 grammassa
            item_id: Ruoka-aineen id tietokannassa, oletuksena None
        """

        self.name = name
        self.calories = calories
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
        self.id = item_id
