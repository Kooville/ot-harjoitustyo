from entities.user import User
from entities.meal import Meal
from entities.item import Item
from repositories.meal_repository import meal_repository as default_meal_repository
from repositories.item_repository import item_repository as default_item_repository
from repositories.user_repository import user_repository as default_user_repository


class DiaryService:
    """ Luokka, joka sisältää sovelluslogiikan """

    def __init__(self,
                 user_repository=default_user_repository,
                 item_repository=default_item_repository,
                 meal_repository=default_meal_repository):
        """Luokan konstruktori joka perustaa sovelluslogiikasta vastaavan toiminnon

        Args:
            user_repository: Käyttäjätietokannan repository. Defaults to default_user_repository.
            item_repository: Ruoka-aineiden tietokannan repository. Defaults to default_item_repository.
            meal_repository: Aterioiden tietokannan repository. Defaults to default_meal_repository.
        """
        self._user = None
        self._user_repository = user_repository
        self._item_repository = item_repository
        self._meal_repository = meal_repository

    def create_user(self, username, password, password_confirmation):
        """ Luo uuden käyttäjän 

        Args:
            username: Käyttäjätunnus, joka halutaan luoda
            password: Salasana, joka halutaan asettaa uudelle käyttäjälle
            password_confirmation: Salasana uudestaan, varmistetaan että käyttäjä on kirjoittanut salasanan oikein

        Returns:
            User-olio, joka on luotu ja lisätty tietokantaan
        """

        if password != password_confirmation:
            raise ValueError("Salasanat eivät täsmää")

        existing_user = self._user_repository.get_user_by_username(username)

        if existing_user:
            raise ValueError("Käyttäjätunnus on varattu")

        user = self._user_repository.create_user(User(username, password))

        self._user = user
        return user

    def login(self, username, password):
        """ Kirjaa käyttäjän sisään 

        Args:
            username: Käyttäjätunnus, jolla halutaan kirjautua sisään
            password: Salasana, jolla halutaan kirjautua sisään

        Returns:
            User-olio, joka on kirjautunut sisään
        """

        user = self._user_repository.get_user_by_username(username)

        if not user or user.password != password:
            raise ValueError("Väärä käyttäjätunnus tai salasana")

        self._user = user
        return user

    def get_current_user(self):
        """ Palauttaa nykyisen käyttäjän 

        Returns:
            User-olio, joka on tällä hetkellä kirjautuneena sisään, tai None
        """
        return self._user

    def logout(self):
        """ Kirjaa käyttäjän ulos """

        self._user = None

    def create_item(self, name, calories, carbs, protein, fat):
        """ Luo uuden ruoka-aineen 

        Args:
            name: Ruoka-aineen nimi
            calories: Ruoka-aineen kalorimäärä 100 grammassa
            carbs: Ruoka-aineen hiilihydraattimäärä 100 grammassa
            protein: Ruoka-aineen proteiinimäärä 100 grammassa
            fat: Ruoka-aineen rasvamäärä 100 grammassa

        Returns:
            Item-olio, joka on luotu ja lisätty tietokantaan
        """

        return self._item_repository.create_item(Item(name, calories, carbs, protein, fat))

    def get_all_items(self):
        """ Palauttaa kaikki ruoka-aineet 

        Returns:
            Lista kaikista Item-olioista, jotka löytyvät tietokannasta
        """

        return self._item_repository.get_all_items()

    def create_meal(self, name, selected_items):
        """ Luo uuden aterian 

        Args:
            name: Aterian nimi
            selected_items: Lista tupleja, joissa on Item-olio ja kerroin,
            joka kertoo kuinka paljon kyseistä ruoka-ainetta ateriassa on

        Returns:
            Meal-olio, joka on luotu ja lisätty tietokantaan
        """

        items = []
        for item in selected_items:
            multiplied_item = self._item_repository.get_item_by_multiplier(
                item[0], item[1])
            items.append(multiplied_item)
        calories = sum(item.calories for item in items)
        carbs = sum(item.carbs for item in items)
        protein = sum(item.protein for item in items)
        fat = sum(item.fat for item in items)

        return self._meal_repository.create_meal(Meal(name, calories, carbs, protein, fat))

    def delete_meal(self, meal_id):
        """ Poistaa aterian 

        Args:
            meal_id: Aterian id, joka halutaan poistaa tietokannasta
        """

        self._meal_repository.delete_meal(meal_id)

    def get_all_meals(self):
        """ Palauttaa kaikki ateriat 

        Returns:
            Lista kaikista Meal-olioista, jotka löytyvät tietokannasta
        """

        return self._meal_repository.get_all_meals()


diary_service = DiaryService()
