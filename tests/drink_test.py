import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Beer", 3.50, 2)

# Tests 1 - 3 checking that Drink has a name, price and alcohol level. Pass
    def test_has_name(self):
        self.assertEqual("Beer", self.drink.name)

    def test_has_price(self):
        self.assertEqual(3.50, self.drink.price)

    def test_has_alcohol_level(self):
        self.assertEqual(2, self.drink.alcohol_level)

    