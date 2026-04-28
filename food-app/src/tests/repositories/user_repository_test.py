import unittest
from entities.user import User
from repositories.user_repository import user_repository


class TestUser(unittest.TestCase):
    def test_create_user(self):
        user = User("ville", "salasana")
        self.assertEqual(user.username, "ville")
        self.assertEqual(user.password, "salasana")

    def test_add_user_to_repository(self):
        user = User("ville", "salasana")
        user_repository.create_user(user)
        retrieved_user = user_repository.get_user_by_username("ville")
        self.assertEqual(retrieved_user.username, "ville")
        self.assertEqual(retrieved_user.password, "salasana")

    def test_get_user_by_username(self):
        user_repository.create_user(User("pekka", "salasana"))
        retrieved_user = user_repository.get_user_by_username("pekka")
        self.assertEqual(retrieved_user.username, "pekka")
        self.assertEqual(retrieved_user.password, "salasana")
