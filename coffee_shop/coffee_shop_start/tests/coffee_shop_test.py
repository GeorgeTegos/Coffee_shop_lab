import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.coffee_shop = CoffeeShop("S&G",1000)
        self.geo = Customer("George",200,30,100)


    def test_coffee_shop_has_name(self):
        self.assertEqual("S&G", self.coffee_shop.name)

    def test_sell_a_drink(self):
        self.coffee_shop.till += 2
        self.assertEqual(self.coffee_shop.till,1002)
    

    def test_check_age(self):
        k = self.coffee_shop.check_age(self.geo.age)
        self.assertEqual(k,20)

    # def test_age_check(self):
    #     age = 20
    #     self.assertGreater(age,16,"You Can't Drink")
                        # 16 > 20

    def test_energy_check(self):
        self.energy = 115
        self.assertLess(self.energy,120)

    