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
    """ Luokka, joka sisältää aterioihin liittyvät tietokantaoperaatiot """

    def __init__(self, connection):
        self.connection = connection

    def create_meal(self, meal):
        """ Lisää tietokantaan uuden aterian """
        cursor = self.connection.cursor()
        cursor.execute("insert into meals (name, calories, carbs, protein, fat)"
                       " values (?, ?, ?, ?, ?)",
                       (meal.name, meal.calories, meal.carbs, meal.protein, meal.fat))
        self.connection.commit()
        meal.id = cursor.lastrowid
        return meal
    
    def delete_meal(self, meal_id):
        """ Poistaa aterian tietokannasta """
        cursor = self.connection.cursor()
        cursor.execute("delete from meals where id = ?", (meal_id,))
        self.connection.commit()

    def get_all_meals(self):
        """ Hakee tietokannasta kaikki ateriat """
        cursor = self.connection.cursor()
        cursor.execute("select * from meals")
        rows = cursor.fetchall()
        return [get_meal_by_row(row) for row in rows]


meal_repository = MealRepository(get_database_connection())
