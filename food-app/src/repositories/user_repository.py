from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    return User(row["username"], row["password"], row["goal_calories"], row["today_calories"], row["id"]) if row else None


class UserRepository:
    """ Luokka, joka sisältää käyttäjiin liittyvät tietokantaoperaatiot """

    def __init__(self, connection):
        self.connection = connection

    def create_user(self, user):
        """ Lisää tietokantaan uuden käyttäjän """
        cursor = self.connection.cursor()
        cursor.execute("insert into users (username, password, goal_calories, today_calories) values (?, ?, ?, ?)",
                       (user.username, user.password, user.goal_calories, user.today_calories))
        self.connection.commit()
        user.id = cursor.lastrowid
        return user

    def get_user_by_username(self, username):
        """ Hakee tietokannasta käyttäjän, joka vastaa annettuja tietoja """
        cursor = self.connection.cursor()
        cursor.execute("select * from users where username = ?",
                       (username,))
        row = cursor.fetchone()
        return get_user_by_row(row)


user_repository = UserRepository(get_database_connection())
