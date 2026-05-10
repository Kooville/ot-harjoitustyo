from entities.meal import Meal
from database_connection import get_database_connection


def get_meal_by_row(row):
    return Meal(row["name"],
                row["calories"],
                row["carbs"],
                row["protein"],
                row["fat"],
                row["id"]) if row else None


class MealRepository:
    """ Luokka, joka sisältää aterioihin liittyvät tietokantaoperaatiot"""

    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            connection: Tietokantayhteyden Connection-olio
        """

        self.connection = connection

    def create_meal(self, meal):
        """Lisää uuden aterian tietokantaan

        Args:
            meal: Meal-olio, joka lisätään tietokantaan

        Returns:
            Meal-olio, joka on lisätty tietokantaan ja jolle on asetettu id
        """

        cursor = self.connection.cursor()
        cursor.execute("""insert into meals (
                            name,
                            calories,
                            carbs,
                            protein,
                            fat
                        ) values (?, ?, ?, ?, ?)
                       """,
                       (meal.name, meal.calories, meal.carbs, meal.protein, meal.fat))
        self.connection.commit()
        meal.id = cursor.lastrowid
        return meal

    def delete_meal(self, meal_id):
        """ Poistaa aterian tietokannasta 

        Args:
            meal_id: Aterian id, joka halutaan poistaa tietokannasta
        """

        cursor = self.connection.cursor()
        cursor.execute("delete from meals where id = ?", (meal_id,))
        self.connection.commit()

    def get_all_meals(self):
        """ Hakee tietokannasta kaikki ateriat 

        Returns:
            Lista kaikista Meal-olioista, jotka löytyvät tietokannasta
        """

        cursor = self.connection.cursor()
        cursor.execute("select * from meals")
        rows = cursor.fetchall()
        return [get_meal_by_row(row) for row in rows]

    def get_meal_by_id(self, meal_id):
        """ Hakee tietokannasta aterian, joka vastaa annettua id:tä

        Args:
            meal_id: Aterian id, jota haetaan

        Returns:
            Meal-olio, joka vastaa annettua id:tä, tai None jos ateriaa ei löydy
        """

        cursor = self.connection.cursor()
        cursor.execute("select * from meals where id = ?", (meal_id,))
        row = cursor.fetchone()
        return get_meal_by_row(row)

    def add_meal_to_diary(self, meal_id, user_id, date):
        """ Lisää aterian päiväkirjaan tietokantaan 

        Args:
            meal_id: Aterian id, joka halutaan lisätä päiväkirjaan
            user_id: Käyttäjän id, jolle ateria halutaan lisätä
            date: Päivämäärä, johon ateria halutaan lisätä (muodossa "YYYY-MM-DD")
        """

        cursor = self.connection.cursor()
        cursor.execute(
            """insert into today_meals (date, user_id, meal_id)
            values (?, ?, ?)""",
            (date, user_id, meal_id))
        self.connection.commit()

    def get_todays_meals(self, user_id, date):
        """ Hakee kaikki ateriat, jotka on lisätty päiväkirjaan tiettynä päivänä 

        Args:
            user_id: Käyttäjän id, jonka ateriat halutaan hakea
            date: Päivämäärä, jonka ateriat halutaan hakea (muodossa "YYYY-MM-DD")

        Returns:
            Lista Meal-olioista, jotka on lisätty päiväkirjaan annettuna päivänä
        """

        cursor = self.connection.cursor()
        cursor.execute("""
            select meals.* from meals
            join today_meals on meals.id = today_meals.meal_id
            where today_meals.user_id = ? and today_meals.date = ?
        """, (user_id, date))
        rows = cursor.fetchall()
        return [get_meal_by_row(row) for row in rows]

    def delete_meal_from_diary(self, meal_id, user_id, date):
        """ Aterian poistaminen päiväkirjasta tietokannasta,
            siten että vain yksi ateria poistetaan

        Args:
            meal_id: Aterian id, joka halutaan poistaa päiväkirjasta
            user_id: Käyttäjän id, jolta ateria halutaan poistaa
            date: Päivämäärä, jolta ateria halutaan poistaa
        """

        cursor = self.connection.cursor()
        cursor.execute("""
                DELETE FROM today_meals
                WHERE rowid IN (
                    SELECT rowid 
                    FROM today_meals
                    WHERE meal_id = ? AND user_id = ? AND date = ?
                    LIMIT 1
               )
            """, (meal_id, user_id, date))
        self.connection.commit()

meal_repository = MealRepository(get_database_connection())
