

class Customer:
    
    def __init__(self,name,wallet,age,energy):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy = energy
    
    def reduce_wallet(self,amount):
        self.wallet -= amount
        return amount
    
    def add_energy(self,energy_to_add):
        self.energy += energy_to_add.caffeine_level

    
    

    
