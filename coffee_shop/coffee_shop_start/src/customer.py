# from coffee_shop import CoffeeShop

class Customer:
    
    def __init__(self,name,wallet):
        self.name = name
        self.wallet = wallet
        # self.age = 0
        # self.energy = 0
    
    def reduce_wallet(self,amount):
        self.wallet -= amount
        return amount
    

    
