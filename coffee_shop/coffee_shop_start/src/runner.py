from drink import Drink
from coffee_shop import CoffeeShop
from customer import Customer

customer_one = Customer("George",100,20,100)
drink_one = Drink("Coffee",5,111)
drink_two = Drink("beer",10,2)
coffee_shop_one = CoffeeShop("Costa",1000)

coffee_shop_one.add_drink_to_list(drink_one)
coffee_shop_one.add_drink_to_list(drink_two)


customer_one.add_energy(drink_two)
print(customer_one.energy)


coffee_shop_one.buy_a_drink(customer_one,drink_two)
print(customer_one.energy)
