import unittest
from entities.meal import Meal
from repositories.meal_repository import meal_repository


class TestMeal(unittest.TestCase):
    def test_create_meal(self):
        meal = meal_repository.create_meal(Meal("jauheliha", 200, 0, 20, 10))
        self.assertEqual(meal.name, "jauheliha")
        self.assertEqual(meal.calories, 200)
        self.assertEqual(meal.carbs, 0)
        self.assertEqual(meal.protein, 20)
        self.assertEqual(meal.fat, 10)

    def test_get_meal_by_name(self):
        meal_repository.create_meal(Meal("jauheliha", 200, 0, 20, 10))
        retrieved_meal = meal_repository.get_meal_by_name("jauheliha")
        self.assertEqual(retrieved_meal.name, "jauheliha")
        self.assertEqual(retrieved_meal.calories, 200)
        self.assertEqual(retrieved_meal.carbs, 0)
        self.assertEqual(retrieved_meal.protein, 20)
        self.assertEqual(retrieved_meal.fat, 10)
