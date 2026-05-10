import unittest
from entities.item import Item
from repositories.item_repository import item_repository


class TestItem(unittest.TestCase):
    def test_create_item(self):
        item = Item("jauheliha", 200, 0, 20, 10)
        self.assertEqual(item.name, "jauheliha")
        self.assertEqual(item.calories, 200)
        self.assertEqual(item.carbs, 0)
        self.assertEqual(item.protein, 20)
        self.assertEqual(item.fat, 10)

    def test_get_item_by_name(self):
        item = Item("jauheliha", 200, 0, 20, 10)
        item_repository.create_item(item)
        retrieved_item = item_repository.get_item_by_name("jauheliha")
        self.assertEqual(retrieved_item.name, "jauheliha")
        self.assertEqual(retrieved_item.calories, 200)
        self.assertEqual(retrieved_item.carbs, 0)
        self.assertEqual(retrieved_item.protein, 20)
        self.assertEqual(retrieved_item.fat, 10)

    def test_get_all_items(self):
        item1 = Item("jauheliha", 200, 0, 20, 10)
        item2 = Item("kana", 150, 0, 30, 5)
        item_repository.create_item(item1)
        item_repository.create_item(item2)
        items = item_repository.get_all_items()
        self.assertIn(item1.name, [i.name for i in items])
        self.assertIn(item2.name, [i.name for i in items])

    def test_get_item_by_multiplier(self):
        item = Item("jauheliha", 200, 0, 20, 10)
        item_repository.create_item(item)
        retrieved_item = item_repository.get_item_by_multiplier(item, 2)
        self.assertEqual(retrieved_item.name, "jauheliha")
        self.assertEqual(retrieved_item.calories, 200*2/100)
        self.assertEqual(retrieved_item.carbs, 0.0)
        self.assertEqual(retrieved_item.protein, 20*2/100)
        self.assertEqual(retrieved_item.fat, 10*2/100)
