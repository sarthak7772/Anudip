
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