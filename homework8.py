#Task 1
# file_path = 'D:/pythonprojects/tekstfile.txt'
# with open(file_path, 'r') as file:
#     lines = file.readlines()
# modified_lines = [line.rstrip() + '!' for line in lines]
# with open(file_path, 'w') as file:
#     file.write('\n'.join(modified_lines))

#Task 2
# with open('input.txt', 'w') as file:
#     numbers = ' '.join(map(str, range(1, 11)))
#     file.write(numbers)
# with open('input.txt', 'r') as file:
#     numbers_str = file.read()
#     numbers_list = list(map(int, numbers_str.split()))
# product = 1
# for num in numbers_list:
#     product *= num
# with open('output.txt', 'w') as file:
#     file.write(str(product))

#Task 3
# from datetime import datetime, timedelta
# products = [
#     ("Product1", 100, 150, datetime(2023, 10, 1)),
#     ("Product2", 50, 30000, datetime(2023, 11, 15)),
#     ("Product3", 200, 5000, datetime(2023, 12, 1))]
# current_date = datetime.now()
# for product in products:
#     name, quantity, price, date = product
#     delta = current_date - date
#     total_cost = quantity * price
#
#     if delta.days > 30 and total_cost > 1000000:
#         print("Product that cost in total more than 1000000 and were stored for more than 30 days are:",name)

#Task 4
# import json
#
# data = {
#     12345: ("John", 25),
#     67890: ("Eva", 30),
#     54321: ("Michael", 22),
#     98765: ("Alex", 35),
#     45678: ("Alice", 28)}
# with open('data.json', 'w') as json_file:
#     json.dump(data, json_file)

#Task 5
# import json
# import csv
#
# with open('data.json', 'r') as json_file:
#     data = json.load(json_file)
# csv_filename = 'data.csv'
# with open(csv_filename, 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=';')
#     csv_writer.writerow(['person', 'name', 'age'])
#     for key, (name, age) in data.items():
#         csv_writer.writerow(['person', name, age])

#Task 6
# try:
#     x = (1, 2, 5, 7)
#     x = x / 2
#     print(x)
# except TypeError as e:
#     print("Error:",e)
# except Exception as e:
#     print("Unexpected error", e)

#Task 7
# try:
#     my_list = [1, 2, 3]
#     index_to_access = 5
#     value = my_list[index_to_access]
#     print("Index to access:", index_to_access,value)
# except IndexError as e:
#     print("Error:",e)
# except Exception as e:
#     print("Unexpected error", e)

#Task 8
# try:
#     string_value = "Hello, "
#     numeric_value = 42
#     result = string_value + numeric_value
#     print(f"Concatenation result: {result}")
# except TypeError as e:
#     print(f"Error: {e}. Attempt to concatenate a string and a number.")
# except Exception as e:
#     print(f"Unexpected error: {e}")

#Task 9
# try:
#     file_path = "nonexistent_file.txt"
#     with open(file_path, "r") as file:
#         content = file.read()
#     print("Content of the file:",content)
# except FileNotFoundError as e:
#     print("Error:",e)
# except Exception as e:
#     print("Unexpected error:",e)

#Task 10
# try:
#     my_list = [1, 2, 3, 4, 5]
#     element_to_remove = int(input("Enter the element you want to remove: "))
#
#     if element_to_remove in my_list:
#         my_list.remove(element_to_remove)
#         print("List after removing {}: {}".format(element_to_remove, my_list))
#     else:
#         raise TypeError("The element {} is not in the list.".format(element_to_remove))
# except TypeError as e:
#     print("Error: {}".format(e))
# except Exception as e:
#     print("Unexpected error: {}".format(e))

