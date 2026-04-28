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
        cursor.execute("insert into meals (name, calories, carbs, protein, fat)"
                       " values (?, ?, ?, ?, ?)",
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


meal_repository = MealRepository(get_database_connection())
