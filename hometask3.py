#Task 1
#string=input("Please enter your string (6 symbols minimum):")
#print("Third symbol of the string is:", string[2])
#print("Penultimate symbol of the string is:", string[-2])
#print("First 5 symbols of the string are:", string[:5])
#print("All the symbols, except for the last two:", string[:-2])
#print("All symbols with even index:", string[::2])
#print("All symbols with uneven index:", string[1::2])
#print("Reversed string:", string[::-1])
#print("Reversed string with even index:", string[::-2])
#print("Symbols' quantity in the string:", len(string))

#Task 2
#word=input("Please enter your word:")
#if (word[0]==word[-1]): print("First and last letter of the word are the same")
#else:print ("First and last letter of the word are NOT the same")

#Task 3
#word=input("Please enter your word:")
#print("New word formed from 2-4th letters:", word[1:4])

#Task 4
#word="яблоко"
#print("New words formed are:", word[1:-1], word[3:])

#Task 5
#word="Ivanou Ivan"
#print(word[7:],word[:6])

#Task 6
#string=input("Please enter your string to analyze:")
#if (string[::-1]==string):print("Your string is a palindrome")
#else: print("Your string is NOT a palindrome")

#Task 7
#spisok=list(input("Please enter your list of symbols:"))
#print("2nd symbols from the list is:", spisok[1])

#Task 8
#string1=input("Please enter your first string:")
#string2=input("Please enter your second string:")
#if string1 not in string2:print("Second string does NOT contain first string")
#else: print ("Second string contains first string")

#Task 9
#string=input("Please enter your string wtih more than 2 'f' symbols in it:")
#if string.count("f")>=2: print (string.find('f', string.find('f')+1))
#else: print("'f' symbol was not found or it's used less than 2 times")

#Task 10
school= dict({"1A":[17],"2Б":[16],"3В":[18],"4Г":[14],"5A":[21],"6Б":[23],"7В":[19],"8Г":[17],"9A":[22],"9Б":[17]})
#в одном из классов изменилось количество учащихся
school["1A"]=19
#в школе появился новый класс.
school["9В"]=20
#в школе был расформирован (удален) другой класс.
del school["4Г"]
#Вычислите общее количество учащихся 9 классов в школе.
#тут я сломалась и не понимаю как вытянуть значения ключей,
#что начинаются на 9 (т.е. в девятых классах) и потом их суммировать
