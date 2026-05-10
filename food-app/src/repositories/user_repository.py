from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    return User(
        row["username"],
        row["password"],
        row["goal_calories"],
        row["id"]) if row else None


class UserRepository:
    """ Luokka, joka sisältää käyttäjiin liittyvät tietokantaoperaatiot """

    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            connection: Tietokantayhteyden Connection-olio
        """

        self.connection = connection

    def create_user(self, user):
        """ Lisää tietokantaan uuden käyttäjän 

        Args:
            user: User-olio, joka halutaan lisätä tietokantaan

        Returns:
            User-olio, joka on lisätty tietokantaan ja jolle on asetettu id
        """

        cursor = self.connection.cursor()
        cursor.execute(
            """insert into users (
                username,
                password,
                goal_calories
            ) values (?, ?, ?)
            """,
            (user.username, user.password, user.goal_calories))
        self.connection.commit()
        user.id = cursor.lastrowid
        return user

    def get_user_by_username(self, username):
        """ Hakee tietokannasta käyttäjän, joka vastaa annettuja tietoja 

        Args:
            username: Käyttäjätunnus, jota haetaan

        Returns:
            User-olio, joka vastaa annettuja tietoja, tai None jos käyttäjää ei löydy
        """

        cursor = self.connection.cursor()
        cursor.execute("select * from users where username = ?",
                       (username,))
        row = cursor.fetchone()
        return get_user_by_row(row)

    def update_user_info(self, user_id, new_username, new_goal_calories):
        """ Päivittää käyttäjätiedot tietokantaan

        Args:
            user_id: Käyttäjän id, jonka tietoja halutaan päivittää
            new_username: Uusi käyttäjätunnus, joka asetetaan käyttäjälle
            new_goal_calories: Uusi tavoitekalorimäärä, joka asetetaan käyttäjälle
        """

        cursor = self.connection.cursor()
        cursor.execute(
            "update users set username = ?, goal_calories = ? where id = ?",
            (new_username, new_goal_calories, user_id)
        )
        self.connection.commit()


user_repository = UserRepository(get_database_connection())
