#Задание 1
#print (17/2*3+2)
#print (2+17/2*3)
#print (19%4+15/2*3)
#print (15+6-10*4)
#print (17/2%2*3**3)

#Задание 2
#print (17/2*(3+2))
#print ((2+17)/2*3)
#print (19%(4+15)/2*3)
#print ((15+6-10)*4)
#print (17/2%(2*3**3))

#Задание 3
#print (11-(1.5*3))

#Задание 4
#Anna = 2
#Paul = 5
#print (Anna, Paul)

#Задание 5
#days = int(input("Please enter days quantity to convert:"))
#print (days,"days =", days*24,"hours =", days*24*60,"minutes =", days*24*60*60,"seconds")

#Задание 6
#days = int(input("Please enter days quantity to convert into full weeks:"))
#print ("Full weeks =", days//7)

#Задание 7
#rectangle = list(map(int, input("Please enter Side A and Side B separated by space:").split()))
#print ("You can cut",rectangle[0]*rectangle[1]//(30*30),"squares")

#Задание 8
#seconds = int(input("Please enter seconds quantity to convert:"))
#print ("",seconds//60//60, "hour(s)\n",seconds//60, "minute(s)\n", seconds, "seconds" )

#Задание 9
#price = int(input("Please enter the price:"))
#hundreds = price//100
#fifty = (price-hundreds*100)//50
#tens = (price - hundreds*100 - fifty*50)//10
#ones = (price - hundreds*100 - fifty*50 - tens*10)//1
#print ("", hundreds, "bills of 100\n",fifty,"bills of 50\n", tens,"bills of 10\n", ones, "bills of 1\n")

#Задание 10
#height = int(input("Please enter pole's height in meters:"))
#up = int(input("Please enter the amount of meters that snail goes up during the day:"))
#down =  int(input("Please enter the amount of meters that snail goes down during the night:"))
#days = height//(up-down)
#print("Snail will get to the top of the pole on the",days,"day")

#Задание 11
#length = 56
#speed = int(input("Please enter biker's speed in km/h:"))
#time = list(map(int, input("Please enter the amount of Hours and Minutes separated by space:").split()))
#timeinh = ((time[0]*60)+time[1])/60
#print("After",time[0],"hours and",time[1],"minutes biker will stop at the",speed*timeinh,"kilometer of the road")

