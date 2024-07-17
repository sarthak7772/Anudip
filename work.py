# time convert

# a = int(input("enter time in seconds"))
# if a >= 0:
#     hour = a // 3600
#     y = a % 3600
#     m = y // 60
#     s = y % 60
# else:
#     print("invalid")
# print(hour, "hour", m, "minutes", s, "seconds")

# greater b/w two number

# a = int(input("enter numbers"))
# b = int(input("enter numbers"))
# if a > b:
#     print(a)
# else:
#     if a == b:
#         print("equal")
#     else:
#         print(b)

# profit and loss

# cp = int(input("enter cost price in rs :"))
# sp = int(input("enter selling price in rs:"))
# if (sp > 0) and (cp > 0):
#     if (sp - cp) > 0:
#         print("profit", (sp - cp))
#     elif (sp - cp) == 0:
#         print("no profit/loss")
#     else:
#         print("loss", (cp - sp))
# else:
#     print("invalid input ")

# itereation

# for x in [80,99,90,50,30,40,50,302,200]:
#     print(x)

# find sum and avg

# sum=0
# l=[80,90,30,20,70,80,39,87]
# for x in l:
#     sum+=x
# avg=sum/len(l)
# print("sum=",sum,"avg=",avg)

# find out the number divisible by 10 and 7 both b/w 10 to 500

# for x in range(10, 500):
#     if (x % 10 == 0) and (x % 7 == 0):
#         print(x)

# count the number b/w 100 to 1000 which is even and divisible by 3

# count=0
# for x in range(100, 1000):
#     if (x % 3 == 0) and (x % 2 == 0):
#         count+=1
# print("count=",count)

# use of end and \n

# count=0
# for x in range(100, 1000):
#     if (x % 3 == 0) and (x % 2 == 0):
#         print(x,end=',')
#         count+=1
# print("\n---------------------------------------------")
# print("\ncount=",count)

# while loop

# x=100
# count=0
# while (x<1000):
#     if (x % 3 == 0) and (x % 2 == 0):
#         print(x,end=',')
#         count+=1
#     x+=1
# print("\n---------------------------------------------")
# print("\ncount=",count)


# students = [
#     ["Aarav", "aarav@example.com", 75],
#     ["Vihaan", "vihaan@example.com", 62],
#     ["Vivaan", "vivaan@example.com", 68],
#     ["Ananya", "ananya@example.com", 45],
#     ["Diya", "diya@example.com", 70],
#     ["Ishaan", "ishaan@example.com", 35],
#     ["Sara", "sara@example.com", 78],
#     ["Rohan", "rohan@example.com", 72],
#     ["Arya", "arya@example.com", 60],
#     ["Aditi", "aditi@example.com", 69],
#     ["Kavya", "kavya@example.com", 74],
#     ["Arjun", "arjun@example.com", 40],
#     ["Mira", "mira@example.com", 73],
#     ["Reyansh", "reyansh@example.com", 77],
#     ["Sneha", "sneha@example.com", 54],
#     ["Ayaan", "ayaan@example.com", 79],
#     ["Ira", "ira@example.com", 59],
#     ["Nisha", "nisha@example.com", 29],
#     ["Karan", "karan@example.com", 63],
#     ["Tanvi", "tanvi@example.com", 21],
#     ["Sahil", "sahil@example.com", 55],
#     ["Priya", "priya@example.com", 68],
#     ["Riya", "riya@example.com", 72],
#     ["Krishna", "krishna@example.com", 32],
#     ["Neha", "neha@example.com", 48],
#     ["Laksh", "laksh@example.com", 75],
#     ["Kunal", "kunal@example.com", 67],
#     ["Pooja", "pooja@example.com", 41],
#     ["Tara", "tara@example.com", 58],
#     ["Aakash", "aakash@example.com", 70]
# ]

# without any formatting

list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(list)
# print(*list)

#  accessing the member of the list

# count=0
# for x in list :
#      print(x)
#      count+=1
# print(count)

# aceesing  the index

# print("3 element", list[2])
# print("4 last element", list[-4])

# sciling

# print ("3 to 7",list[2:7])
# print (" alternate 3 to 7",list[2:7:2])

# print the elements in backward direction from forward indexing

# method 1

# n = len(list)
# for i in range(0, n):
#     print(list[n - i - 1],end=',')
# print("\n")

# method 2

# for i in range(n-1, 0, -1):
#     print(list[i], end=" ")
# print("\n")

# method 3

# print(list[9::-1])

#append function
 
# x=int(input("enter the number"))
# list.append(x)
# print(list)

# extend function 

# list1=[110,120,130]
# list.extend(list1)
# print(list)

# insert function 

# print ( "insert 200 at 2 ")
# list.insert(2,200)
# print (list)

#find a method to insert all the elements of another squence datatype at particular index in the list 
#but all the elelments must be inserted one by one 

# l=list[0:3]+[120,130,140]+list[3:]
# print(l)

#pop function 
# print ( "remove at 2 ")
# list.pop(2)
# print (list)

# print ( "remove at last")
# list.pop()
# print (list)

# remove()
list.remove(90)
print(list)
    