from entities.user import User
from entities.item import Item
from repositories.item_repository import item_repository as default_item_repository
from repositories.user_repository import user_repository as default_user_repository


class DiaryService:
    """ Luokka, joka sisältää sovelluslogiikan """

    def __init__(self, user_repository=default_user_repository, item_repository=default_item_repository):
        self._user = None
        self._user_repository = user_repository
        self._item_repository = item_repository

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

diary_service = DiaryService()
