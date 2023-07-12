import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.geo = Customer("George",200)
        # self.coffee_shop = CoffeeShop("S&G",1000)

    
    def test_customer_name(self):
        self.assertEqual("George",self.geo.name)

    def test_wallet_amount(self):
        self.assertEqual(200,self.geo.wallet)

    def test_reduce_wallet_ammout(self):
        self.geo.reduce_wallet(20)
        self.assertEqual(180,self.geo.wallet)

