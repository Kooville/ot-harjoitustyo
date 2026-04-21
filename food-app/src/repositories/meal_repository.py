from entities.meal import Meal
from database_connection import get_database_connection


def get_meal_by_row(row):
    return Meal(row["name"], row["items"]) if row else None


class MealRepository:
    """ Luokka, joka sisältää aterioihin liittyvät tietokantaoperaatiot """

    def __init__(self, connection):
        self.connection = connection

    def create_meal(self, meal):
        """ Lisää tietokantaan uuden aterian """
        cursor = self.connection.cursor()
        cursor.execute("insert into meals (name, calories, carbs, protein, fat) values (?, ?, ?, ?, ?)",
                       (meal.name, meal.calories, meal.carbs, meal.protein, meal.fat))
        self.connection.commit()
        return meal

meal_repository = MealRepository(get_database_connection())
