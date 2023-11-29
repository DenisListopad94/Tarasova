# Task 1
# numbers = (6, 2, 7, 28, 8)
# for i in numbers:
#    s = 0
#    for j in range(1, (i // 2 + 1)):
#        if i % j == 0:
#            s += j
#            if s == i:
#                print(i)

# Task 2
# numbers = (5, 2, -2, 7, -8, -9, 1)
# counter = 0
# for i in range(0, len(numbers)-1):
#    if numbers[i] < 0 < numbers[i + 1] or numbers[i] > 0 > numbers[i + 1]:
#        counter += 1
# print("Знак менялся",counter,"раз")


# Task 3
# list1 = [4, 1, 6, 9]
# list2 = [8, 1, 2, 4, 9, 5, 7, 6]
# list3 = []

# for i in list1:
#    if i not in list2 and i not in list3:
#        list3.append(i)
# if len(list3) == 0:
#    print("Таких чисел нет")
# else:
#    print("Наименьшее число первого списка, которое не входит во второй список:", min(list3))


# Task 4
# numbers = list(map(int, input("Please enter three numbers (separated by space):").split()))
# numbers1 = []
# for i in numbers:
#    numbers1.append(i)
#    if i % 2 == 0:
#        r = str(i)[::-1]
#        numbers1.append(int(r))
# print(numbers1)

# Task 5
#spisok = list(map(int, input("Please enter your list of numbers (separated by space):").split()))
#for i in set(spisok):
#    print("Number", i, "appears", spisok.count(i), "time(s)")

# Task 6
#numbers = list(map(int, input("Please enter three numbers (separated by space):").split()))
#for i in range(len(numbers)-1):
#    i+=(i+1)
#    numbers.insert(i, 0)
#print(numbers)

# Task 7
#spisok = list(map(int, input("Please enter your list of numbers (separated by space):").split()))
#appeared = set()
#for i in spisok:
#    if i in appeared:
#        print (i, "-Yes")
#    else: print (i, "-No")
#    appeared.add(i)


# Task 8 - тут у меня ничего толкового не вышло :(
# помню, что на уроке она обсуждалась,
# но не было возможности пересмотреть записи пока

# Task 9
#dictionary = {'hard':'complex','simple':'easy','empty':'hollow', 'bold':'brave'}
#word = input('Please enter the word to find synonym for: ')
#if word in dictionary:
#    synonym = dictionary[word]
#    print('Synonym of the word "',word,'"','is', '"',synonym,'"')
#else:
#    print('Word is not found in the dictionary')
