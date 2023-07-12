import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.geo = Customer("George",200,30,100)

    
    def test_customer_name(self):
        self.assertEqual("George",self.geo.name)

    def test_wallet_amount(self):
        self.assertEqual(200,self.geo.wallet)

    def test_reduce_wallet_ammout(self):
        self.geo.reduce_wallet(20)
        self.assertEqual(180,self.geo.wallet)

    def test_age_check(self):
        self.geo.age

    def test_add_energy(self):
        self.customer_energy = 0
        self.customer_energy += 10
        self.assertEqual(self.customer_energy,10)