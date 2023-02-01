import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Burger", 6.00, 5)
    
# Tests 1 - 3 checking that Food has a name, price and rejuvination level. Pass
    def test_has_name(self):
        self.assertEqual("Burger", self.food.name)
    
    def test_has_price(self):
        self.assertEqual(6, self.food.price)

    def test_has_rejuvination_level(self):
        self.assertEqual(5, self.food.rejuvination_level)