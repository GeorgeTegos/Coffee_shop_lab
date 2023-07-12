from drink import Drink
from coffee_shop import CoffeeShop
from customer import Customer

customer_one = Customer("George",100,20,10)
drink_one = Drink("Coffee",5,111)
drink_two = Drink("beer",10,2)
drink_three = Drink("Deluxe",500,2)
coffee_shop_one = CoffeeShop("Costa",1000)

coffee_shop_one.add_drink_to_list(drink_one)    
coffee_shop_one.add_drink_to_list(drink_two)
coffee_shop_one.add_drink_to_list(drink_three)


customer_one.add_energy(drink_two)
print(customer_one.energy)


coffee_shop_one.buy_a_drink(customer_one,drink_two)
print(customer_one.energy)

print(coffee_shop_one.drink_names())

print(coffee_shop_one.drinks_customer_can_afford(customer_one))
