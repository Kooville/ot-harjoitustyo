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
        self._user = None
        self._user_repository = user_repository
        self._item_repository = item_repository
        self._meal_repository = meal_repository

    def create_user(self, username, password, password_confirmation):
        """ Luo uuden käyttäjän """
        if password != password_confirmation:
            raise ValueError("Salasanat eivät täsmää")

        existing_user = self._user_repository.get_user_by_username(username)

        if existing_user:
            raise ValueError("Käyttäjätunnus on varattu")

        user = self._user_repository.create_user(User(username, password))

        self._user = user
        return user

    def login(self, username, password):
        """ Kirjaa käyttäjän sisään """
        user = self._user_repository.get_user_by_username(username)

        if not user or user.password != password:
            raise ValueError("Väärä käyttäjätunnus tai salasana")

        self._user = user
        return user

    def get_current_user(self):
        """ Palauttaa nykyisen käyttäjän """
        return self._user

    def logout(self):
        """ Kirjaa käyttäjän ulos """
        self._user = None

    def create_item(self, name, calories, carbs, protein, fat):
        """ Luo uuden ruoka-aineen """
        return self._item_repository.create_item(Item(name, calories, carbs, protein, fat))

    def get_all_items(self):
        """ Palauttaa kaikki ruoka-aineet """
        return self._item_repository.get_all_items()

    def create_meal(self, name, selected_items):
        """ Luo uuden aterian """
        items = []
        for item in selected_items:
            multiplied_item = self._item_repository.get_item_by_multiplier(
                item[0], item[1])
            items.append(multiplied_item)

        return self._meal_repository.create_meal(Meal(name, items))


diary_service = DiaryService()
