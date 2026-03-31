from entities.user import User

from repositories.user_repository import user_repository as default_user_repository

class DiaryService:
    """ Luokka, joka sisältää sovelluslogiikan """

    def __init__(self,
                 user_repository=default_user_repository
                 ):
        self._user = None
        self._user_repository = user_repository

    def create_user(self, username, password, password_confirmation):
        """ Luo uuden käyttäjän """
        if password != password_confirmation:
            raise ValueError("Salasanat eivät täsmää")

        user = self._user_repository.create_user(User(username, password))

        self._user = user
        return user

    def login(self, username, password):
        """ Kirjaa käyttäjän sisään """
        user = self._user_repository.get_user(username, password)
        self._user = user
        return user

    def logout(self):
        """ Kirjaa käyttäjän ulos """
        self._user = None

diary_service = DiaryService()
