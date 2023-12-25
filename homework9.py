#Task 1
# class TwoVariables:
#     def __init__(self, var1, var2):
#         self.var1 = var1
#         self.var2 = var2
#
#     def display_variables(self):
#         print("Variables: {}, {}".format(self.var1, self.var2))
#
#     def modify_variables(self, new_var1, new_var2):
#         self.var1 = new_var1
#         self.var2 = new_var2
#         print("Variables modified successfully.")
#
#     def sum_variables(self):
#         return self.var1 + self.var2
#
#     def max_variable(self):
#         return max(self.var1, self.var2)
#
# my_variables = TwoVariables(3, 7)
# my_variables.display_variables()
# my_variables.modify_variables(5, 10)
# my_variables.display_variables()
# print("Sum of variables:", my_variables.sum_variables())
# print("Max variable:", my_variables.max_variable())

#Task 2
# class DecimalCounter:
#     def __init__(self, min_value=0, max_value=9, initial_value=None):
#         self.min_value = min_value
#         self.max_value = max_value
#         if initial_value is None:
#             self.value = min_value
#         else:
#             self.set_value(initial_value)
#
#     def increment(self):
#         self.value = (self.value + 1) % (self.max_value + 1)
#
#     def decrement(self):
#         self.value = (self.value - 1) % (self.max_value + 1)
#
#     def get_value(self):
#         return self.value
#
#     def set_value(self, new_value):
#         if self.min_value <= new_value <= self.max_value:
#             self.value = new_value
#         else:
#             print("Error: Value {new_value} is out of range [{self.min_value}, {self.max_value}].")
#
# counter = DecimalCounter()
# counter.increment()
# print("Current value:", counter.get_value())
# counter.set_value(7)
# print("Current value:", counter.get_value())
# counter.decrement()
# print("Current value:", counter.get_value())

#Task 3
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Shop:
#     def __init__(self):
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#         print(f"Product '{product.name}' added to the shop.")
#
#     def remove_product(self, product_name):
#         for product in self.products:
#             if product.name == product_name:
#                 self.products.remove(product)
#                 print(f"Product '{product_name}' removed from the shop.")
#                 return
#         print(f"Product '{product_name}' not found in the shop.")
#
#     def find_product(self, product_name):
#         for product in self.products:
#             if product.name == product_name:
#                 return product
#         return None
#
#     def display_products(self):
#         print("Products in the shop:")
#         for product in self.products:
#             print(f"{product.name}: ${product.price}")
#
# shop = Shop()
# product1 = Product("Apple", 2.5)
# product2 = Product("Banana", 1.5)
# shop.add_product(product1)
# shop.add_product(product2)
# searched_product = shop.find_product("Banana")
# if searched_product:
#     print(f"Found: {searched_product.name}, Price: ${searched_product.price}")
# else:
#     print("Product not found.")
# shop.remove_product("Apple")
# shop.display_products()


#Task 4
# class MoneyBox:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.coins_count = 0
#
#     def can_add(self, v):
#         return self.coins_count + v <= self.capacity
#
#     def add(self, v):
#         if self.can_add(v):
#             self.coins_count += v
#             print(f"Added {v} coins to the money box. Total coins: {self.coins_count}")
#         else:
#             print("Cannot add more coins. Capacity exceeded.")
#
# money_box = MoneyBox(10)
# money_box.add(5)
# money_box.add(7)
# print("Can add 3 more coins:", money_box.can_add(3))

