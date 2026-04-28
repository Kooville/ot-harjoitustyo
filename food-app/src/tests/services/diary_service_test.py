import unittest
from entities.user import User
from entities.meal import Meal
from entities.item import Item
from services.diary_service import DiaryService

class FakeUserRepository:
    def __init__(self):
        self.users = []

    def create_user(self, user):
        self.users.append(user)
        return user

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

class FakeItemRepository:
    def __init__(self):
        self.items = []

    def create_item(self, item):
        self.items.append(item)
        return item

    def get_all_items(self):
        return self.items
    
class FakeMealRepository:
    def __init__(self):
        self.meals = []

    def create_meal(self, meal):
        self.meals.append(meal)
        return meal

    def get_all_meals(self):
        return self.meals

class TestDiaryService(unittest.TestCase):
    def setUp(self):
        self.diary_service = DiaryService(
            FakeUserRepository(),
            FakeItemRepository(),
            FakeMealRepository()
        )
        self.user_ville = User("ville", "salasana")
        self.item_leipä = Item("leipä", 200, 40, 5, 2)
        self.meal_aamiainen = Meal("aamiainen", 300, 50, 10, 5)

    def test_create_user(self):
        user =self.diary_service.create_user("ville", "salasana", "salasana")
        self.assertEqual(user.username, "ville")
        self.assertEqual(user.password, "salasana")
