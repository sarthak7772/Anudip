# Time Conversion
sec = int(input("enter time in seconds"))
if sec >= 0:
    hour = sec // 3600
    y = sec % 3600
    m = y // 60
    s = y % 60
else:
    print("invalid")
print(hour, "hour", m, "minutes", s, "seconds")