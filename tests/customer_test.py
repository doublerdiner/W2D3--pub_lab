import unittest
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Mike", 25.00, 30, 8)
        self.drink = Drink("Beer", 3.50, 2)
        self.food = Food("Burger", 6.00, 5)

# Tests 1-4 checking that the Customer has a name, wallet, age and drunkeness. Pass
    def test_has_name(self):
        self.assertEqual("Mike", self.customer.name)

    def test_has_wallet(self):
        self.assertEqual(25.00, self.customer.wallet)

    def test_has_age(self):
        self.assertEqual(30, self.customer.age)

    def test_has_drunkeness(self):
        self.assertEqual(8, self.customer.drunkeness)

# Test 4 - Customer can buy a drink - Pass
    def test_buy_drink(self):
        self.customer.buy_drink(self.drink)
        self.assertEqual(21.50, self.customer.wallet)

# Test 5 - Increase drunkeness level - Pass
    def test_drunkeness_level(self):
        self.customer.increase_drunkeness(self.drink)
        self.assertEqual(10, self.customer.drunkeness)

# Test 6 - Buying food / rejuvination decreases drunkeness level - Pass
    def test_buy_food(self):
        self.customer.buy_food(self.food)
        self.assertEqual(3, self.customer.drunkeness)