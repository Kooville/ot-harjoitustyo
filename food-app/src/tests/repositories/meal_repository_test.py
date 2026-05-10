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

    def test_get_meal_by_id(self):
        meal = meal_repository.create_meal(Meal("jauheliha", 200, 0, 20, 10))
        retrieved_meal = meal_repository.get_meal_by_id(meal.id)
        self.assertEqual(retrieved_meal.name, "jauheliha")
        self.assertEqual(retrieved_meal.calories, 200)
        self.assertEqual(retrieved_meal.carbs, 0)
        self.assertEqual(retrieved_meal.protein, 20)
        self.assertEqual(retrieved_meal.fat, 10)

    def test_delete_meal(self):
        meal = meal_repository.create_meal(Meal("jauheliha", 200, 0, 20, 10))
        meal_repository.delete_meal(meal.id)
        retrieved_meal = meal_repository.get_meal_by_id(meal.id)
        self.assertIsNone(retrieved_meal)

    def test_get_all_meals(self):
        meal1 = meal_repository.create_meal(Meal("jauheliha", 200, 0, 20, 10))
        meal2 = meal_repository.create_meal(Meal("kana", 150, 0, 30, 5))
        meals = meal_repository.get_all_meals()
        self.assertIn(meal1.id, [m.id for m in meals])
        self.assertIn(meal2.id, [m.id for m in meals])

    def test_add_meal_to_diary(self):
        meal = meal_repository.create_meal(Meal("jauheliha", 200, 0, 20, 10))
        meal_repository.add_meal_to_diary(meal.id, 1, "2024-06-01")
        meals = meal_repository.get_todays_meals(1, "2024-06-01")
        self.assertIn(meal.id, [m.id for m in meals])

    def test_delete_meal_from_diary(self):
        meal = meal_repository.create_meal(Meal("jauheliha", 200, 0, 20, 10))
        meal_repository.add_meal_to_diary(meal.id, 1, "2024-06-01")
        meal_repository.delete_meal_from_diary(meal.id, 1, "2024-06-01")
        meals = meal_repository.get_todays_meals(1, "2024-06-01")
        self.assertNotIn(meal.id, [m.id for m in meals])
