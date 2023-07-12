import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink= Drink("Coffee", 10)

    # def test_drink_name (self):
    #     self.assertEqual (self.drink.name, "Coffee")

    # def test_drink_price(self):
    #     self.assertEqual(self.drink.price, 10)

    