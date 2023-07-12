from drink import Drink
from coffee_shop import CoffeeShop
from customer import Customer

customer_one = Customer("George",100)
drink_one = Drink("Coffee",5)
drink_two = Drink("beer",10)
coffee_shop_one = CoffeeShop("Costa",1000)

coffee_shop_one.add_drink_to_list(drink_one,drink_two)

# print(coffee_shop_one.drink_list)
coffee_shop_one.sell_a_drink(customer_one,drink_two)
print(customer_one.wallet)