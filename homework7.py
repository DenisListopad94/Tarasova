#task 1
# find_substring = lambda substring, full_string: full_string.find(substring)
# input_string = input("Enter your string: ")
# input_substring = input("Enter your substring: ")
# result = find_substring(input_substring, input_string)
# if result !=-1:
#     print("Substring was found at the position number", result)
# else:
#     print("Substring was not found")

#task 2
# check_even = lambda x: x % 2 == 0
#
# number = int(input("Enter your number: "))
# if check_even(number):
#     print(number,"is an even number.")
# else:
#     print(number,"is an odd number")

#task 3
# greet_user = lambda name: name.capitalize()
# entered_name = input("Enter your name: ")
# result = greet_user(entered_name)
# if entered_name.isalpha():
#     print("Hello,",result)
# else:
#     print("Name entered is wrong")

#task 4
# def digits(n):
#     if n < 10:
#         return str(n)
#     else:
#         return str(n % 10) + " " + digits(n // 10)
#
# number = int(input("Enter your number: "))
# result = digits(number)
# print(result)

#task 5
# def is_power(n):
#     if n == 1:
#         return True
#     elif n % 2 != 0 or n == 0:
#         return False
#     else:
#         return is_power(n // 2)
# number = int(input("Enter your number: "))
# result = is_power(number)
# if result:
#     print("True")
# else:
#     print("False")

#task 6
# def sum_of_digits(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum_of_digits(n // 10)
# number = int(input("Enter your number: "))
# result = sum_of_digits(number)
# print(result)

#task 7
# import time
# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print("Function's execution took",execution_time,"seconds")
#         return result
#     return wrapper
#
# @timing_decorator
# def print_prime_numbers():
#     primes = []
#     for num in range(2, 101):
#         for i in range(2, int(num**0.5) + 1):
#             if (num % i) == 0:
#                 break
#         else:
#             primes.append(num)
#     print("Simple number from 1 to 100:", primes)
#
# print_prime_numbers()

#task 8
# def password_decorator(func):
#     def wrapper(*args, **kwargs):
#         password = input("Enter password: ")
#
#         if check_password(password):
#             result = func(*args, **kwargs)
#             return result
#         else:
#             print("Wrong password.")
#
#     return wrapper
# def check_password(password):
#     known_password = "qatestpass!!"
#     return password == known_password
# @password_decorator
# def protected_function():
#     print("Welcome!")
#
# protected_function()
