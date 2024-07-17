# count=0
# for x in range(100, 1000):
#     if (x % 3 == 0) and (x % 2 == 0):
#         print(x,end=',')
#         count+=1
# print("\n---------------------------------------------")
# print("\ncount=",count)

# while loop

x=100
count=0
while (x<1000):
    if (x % 3 == 0) and (x % 2 == 0):
        print(x,end=',')
        count+=1
    x+=1
print("\n---------------------------------------------")
print("\ncount=",count)