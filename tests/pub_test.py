import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Goose", 500)
        self.drink = Drink("Beer", 3.50, 2)
        self.food = Food("Burger", 6.00, 5)
        self.customer = Customer("Mike", 25.00, 30, 8)
    
# Tests 1 - 2 checking that the Pub has a name and till. Pass
    def test_has_name(self):
        self.assertEqual("The Goose", self.pub.name)

    def test_has_till(self):
        self.assertEqual(500, self.pub.till)

# Test 3 - Pub can sell drink. Pass
    def test_sell_drink(self):
        self.pub.sell_drink(self.customer, self.drink)
        self.assertEqual(503.50, self.pub.till)

# Test 4 & 5 - Checking customer age. Pass
    def test_customer_age__True(self):
        self.customer = Customer("Brian", 5.00, 15, 20)
        answer = self.pub.is_customer_underage(self.customer)
        self.assertEqual(True, answer)

    def test_customer_age__False(self):
        answer = self.pub.is_customer_underage(self.customer)
        self.assertEqual(None, answer)
    
# Test 6 - Pub refuses to serve over certain drunkeness level - Pass
    def test_drunkeness_level__True(self):
        self.customer = Customer("Brian", 5.00, 15, 10)
        answer = self.pub.is_customer_drunk(self.customer)
        self.assertEqual(True, answer)
    
    def test_drunkeness_level__False(self):
        answer = self.pub.is_customer_drunk(self.customer)
        self.assertEqual(None, answer) 

# Test 7 - Pub stock check
    def test_stock_check(self):
        answer = self.pub.stock_check()
        self.assertEqual("There are 100 servings of beer, 150 servings of wine and 50 servings of whisky. The total stock value is 1370.00", answer)


