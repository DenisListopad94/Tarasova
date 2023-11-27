# task 1
# def gen2(x,y,z):
#    for i in range (x, y+1):
#        print(i**z)

# gen2(1,10,2)


# task 2
#def krat35(x, y):
#    for i in range(x, y):
#        if i % 3 == 0 and i % 5 == 0:
#            print(i)

#krat35(100, 1000)

#task 3
# def gen(numbers):
#     for i in range(numbers[0], numbers[1] + 1):
#         print(i ** numbers[2])
#
# input_numbers = list(map(int, input('Please enter three numbers separated by space:').split()))
# gen(input_numbers)


#task 4
# def line(string1):
#     string2 = []
#     if len(string1) > 1:
#         for i in range(len(string1)):
#             r = string1[i-1] + string1[(i+1) % len(string1)]
#             string2.append(r)
#         print(string2)
#     else:
#         print(string1)
# input_numbers = input("Please enter your numbers (separated by space): ")
# numbers_list = list(map(int, input_numbers.split()))
# line(numbers_list)


#task 5
#def find_min(a,b):
#    return min(a,b)

#print("Minimal of all four numbers is:",find_min(find_min(23,34), find_min(82,112)))

#task 6
# def distance(x1, y1, x2, y2):
#     return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
# input_str = input("Enter four real numbers separated by space: ")
# x1, y1, x2, y2 = map(float, input_str.split())
#
# print("The distance between points",x1,":",y1,"and",x2,":",y2,"is", distance(x1, y1, x2, y2))

# task 7
# def fib(n):
#     fibonacci = [0, 1]
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         for i in range(2, n):
#             result = fibonacci[i - 1] + fibonacci[i - 2]
#             fibonacci.append(result)
#         return result
#
# n = int(input("Enter Fibonacci number you want to know: "))
# print("Fibonacci number requested is:", fib(n))





# task 8
# def closest_mod_5(x):
#     y = x
#     while y % 5 != 0:
#         y += 1
#     return y
#
# x = int(input("Enter your number: "))
# result = closest_mod_5(x)
# print("Closest number being multiple of 5 and >= than", x,"is", result)

#task 9
# def modify_list(lst):
#     i = 0
#     while i < len(lst):
#         if lst[i] % 2 == 0:
#             lst[i] //= 2
#             i += 1
#         else:
#             del lst[i]
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# modify_list(my_list)
# print(my_list)

