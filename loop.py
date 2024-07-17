
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

count=0
for x in range(100, 1000):
    if (x % 3 == 0) and (x % 2 == 0):
        count+=1
print("count=",count)