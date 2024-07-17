# Profit and L oss

cp = int(input("enter cost price in rs :"))
sp = int(input("enter selling price in rs:"))
if (sp > 0) and (cp > 0):
    if (sp - cp) > 0:
        print("profit", (sp - cp))
    elif (sp - cp) == 0:
        print("no profit/loss")
    else:
        print("loss", (cp - sp))
else:
    print("invalid input ")