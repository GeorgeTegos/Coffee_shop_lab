# from drink import Drink
# from customer import Customer


class CoffeeShop:
	
	def __init__(self,name,till):
		self.name = name
		self.till = till 
		self.drink_list = []
	
	def add_drink_to_list(self,drink_to_add):
		self.drink_list.append(drink_to_add)

	def sell_a_drink(self,customer,drink):
		if drink in self.drink_list:
			self.till += drink.price
		customer.reduce_wallet(drink.price)
	
	def check_age(self,customer_age):
		if customer_age < 16:
			return False
		else:
			return True
	
	def energy_check(self,customer):
		if customer.energy > 120:
			return False
		else:
			return True
		
	def buy_a_drink(self,customer,drink):
		if self.check_age(customer.age):
			if self.energy_check(customer):
				self.sell_a_drink(customer,drink)
				print("enjoy")
				customer.add_energy(drink)
			else:
				print("We Can't serve you")
		else:
			print("You are underaged")
		
	def drink_names(self):
		drinks_names = [drink.name for drink in self.drink_list]
		return drinks_names
	
	def drinks_customer_can_afford(self,customer):
		can_afford = [drink.name for drink in self.drink_list if drink.price <= customer.wallet]
		return can_afford
		

	
		



