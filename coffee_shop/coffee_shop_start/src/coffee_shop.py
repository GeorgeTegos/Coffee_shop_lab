# from drink import Drink

class CoffeeShop:
	
	def __init__(self,name,till):
		self.name = name
		self.till = till 
		self.drink_list = []
	
	def add_drink_to_list(self,*args):
		self.drink_list.append(args)

	def sell_a_drink(self,customer,drink):
		if drink in self.drink_list:
			self.till += drink.price
		customer.reduce_wallet(drink.price)
	

		
	
	def whatever(self):
		print(self.drink_list)
	







