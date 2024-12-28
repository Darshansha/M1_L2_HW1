day = int(input("When is your birthday(dd)?"))
m = int(input("When is your birthday(mm)?"))
y = int(input("When is your birthday(yyyy)?"))
if day == 11 and m == 12:
    print("Happy Birthday!")
elif day > 11 and m == 12:
    print("Your birthday is soon")
else:
    print("Your birthday is", day,"/",m,"/",y)
