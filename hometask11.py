#Task 1
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
# n = int(input("Enter the number of Fibonacci numbers you want to generate: "))
# for number in fib(n):
#     print(number)

#Task 2
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def simple(n):
#     current_number = 2
#     while current_number <= n:
#         if is_prime(current_number):
#             yield current_number
#         current_number += 1
#
# try:
#     n = int(input("Enter a number: "))
#     for prime_number in simple(n):
#         print(prime_number)
# except KeyboardInterrupt:
#     print("Process interrupted by the user.")

#Task 3
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def perfect_numbers_generator(limit):
#     p = 2
#     while True:
#         mersenne_number = 2**p - 1
#         if is_prime(mersenne_number):
#             perfect_number = 2**(p-1) * mersenne_number
#             if perfect_number <= limit:
#                 yield perfect_number
#             else:
#                 break
#         p += 1
#
# limit = 1000000000
# for perfect_number in perfect_numbers_generator(limit):
#     print(perfect_number)

#Task 4
# def process_string(input_str):
#     start_index = input_str.find('{')
#
#     if start_index != -1:
#         end_index = input_str.find('}', start_index)
#
#         if end_index != -1:
#             processed_str = input_str[:start_index] + input_str[end_index + 1:]
#         else:
#             processed_str = input_str[:start_index]
#     else:
#         processed_str = input_str
#
#     most_common_char = max(set(processed_str), key=processed_str.count)
#     print(f"Processed String: {processed_str}")
#     print(f"Most Common Character: {most_common_char}")
#
#
# input_string = "abc{def}gh{ij}kl"
# process_string(input_string)

#Task 5
# class Server:
#     def __init__(self):
#         self.data = []
#
#     def process_command(self, command):
#         if command.startswith("POST"):
#             data = " ".join(command.split(" ")[1:])
#             self.data.append(data)
#
#         elif command == "GET":
#             if not self.data:
#                 return "None"
#             return f"{self.data[-1]}"
#
#         elif command == "DELETE":
#             if not self.data:
#                 return "None"
#             deleted_data = self.data.pop()
#             return f"{deleted_data}"
#
#         else:
#             return "Invalid command"
#
# server = Server()
#
# commands = []
# while True:
#     command = input().strip()
#     if command == ".":
#         break
#     server.process_command(command)
#
# if server.data:
#     print("\n".join(server.data))
# else:
#     print("None")

#Task 6
# class ContactBook:
#     def __init__(self):
#         self.contacts = {}
#
#     def add_contact(self, name, numbers):
#         if name not in self.contacts:
#             self.contacts[name] = []
#         self.contacts[name].extend(numbers)
#
#     def get_numbers(self, name):
#         if name in self.contacts:
#             if not self.contacts[name]:
#                 return "Not found"
#             return ", ".join(self.contacts[name])
#         else:
#             return "Not found"
#
#     def view_contact_book(self):
#         if not self.contacts:
#             print("Contact book is empty.")
#         else:
#             for contact, numbers in self.contacts.items():
#                 if numbers:
#                     print(f"{contact}: {', '.join(numbers)}")
#
# def main():
#     contact_book = ContactBook()
#
#     while True:
#         print("Choose an action:")
#         print("1. Add numbers to the contact book")
#         print("2. Get numbers of a person from the contact book")
#         print("3. View the entire contact book")
#         print("4. Exit")
#
#         choice = input("Enter the action number: ")
#
#         if choice == "1":
#             name = input("Enter the name: ")
#             numbers = input("Enter the numbers separated by commas: ").split(", ")
#             contact_book.add_contact(name, numbers)
#         elif choice == "2":
#             name = input("Enter the name: ")
#             result = contact_book.get_numbers(name)
#             print(result)
#         elif choice == "3":
#             contact_book.view_contact_book()
#         elif choice == "4":
#             break
#         else:
#             print("Invalid choice. Please try again.")
#
# if __name__ == "__main__":
#     main()
