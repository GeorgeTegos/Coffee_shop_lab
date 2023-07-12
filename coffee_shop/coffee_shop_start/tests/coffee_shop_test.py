import unittest
from src.coffee_shop import CoffeeShop


class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.coffee_shop = CoffeeShop("S&G",1000)

    def test_coffee_shop_has_name(self):
        self.assertEqual("S&G", self.coffee_shop.name)

    def test_sell_drink(self):
        self.coffee_shop.till += 2
        self.assertEqual(self.coffee_shop.till,1002)

    