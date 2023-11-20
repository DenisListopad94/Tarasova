# Task 1
# numbers = list(map(float, input("Please enter three numbers (separated by space):").split()))
# if numbers[0] < 0 or numbers[1] < 0 or numbers[2] < 0:
#    print("True")
# else:
#    print("False")

# Task 2
# numbers = list(map(int, input("Please enter two numbers (separated by space):").split()))
# if (numbers[0] % 2 == 0 and numbers[1] % 2 == 0) or (numbers[0] % 2 != 0 and numbers[1] % 2 != 0):
#    print("These numbers have the same parity")
# else:
#    print("These numbers have different parity")


# Task 3:
# numbers = map(int, input("Please enter three numbers (separated by space):").split())
# count = 0
# for i in numbers:
#    if i % 2 == 0: count += 1
# print(count, "even number(s) was(were) entered")

# Task 4:
# number = int(input("Please enter two-digit number:"))
# first_digit = number // 10
# second_digit = (number - (first_digit * 10))
# new_number = (first_digit + second_digit)
# if len(str(new_number)) == 2:
#    print("Sum of digits of the entered number is a double-digit")
# else:
#    print("Sum of digits of the entered number is NOT a double-digit")

# Task 5:
# s = "10"
# for i in range(20):
#    print(s)


# Task 6:
# n =int(input("Please enter your number:"))
# ниже поставила n+1, чтобы включало число n, если включать не нужно, то будет просто n
# for i in range (1,n+1):
#    print (i**3)

# Task 7
#n = 1
#for i in range(5, 21): n *= i
#print("Product of all numbers from 5 up to 20 equals:", n)

#Task 8
#n = int(input("Please enter your number:"))
#for i in range (1,n):
#    if i**2 <n:
#        print (i**2)

#Task 9
#n = map(int, input("Please enter your number:"))
#print("Minimal digit from the entered number is ",min(n))

#Task 10
#year = int(input("Please enter your year:"))
#if (year%4==0 and year%100!=0) or year%400==0:
#    print (year, "is a leap year")
#else: print (year, "is NOT a leap year")

