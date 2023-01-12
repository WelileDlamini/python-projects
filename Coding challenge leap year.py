year = int(input("Which year do you want to check? "))

if year % 4 == 0 and year % 100 != 0:
    print(year, "leap year")
elif year % 4 == 0 and year % 100 == 0:
    if year % 400 == 0:
        print(year, "leap year")
    else:
        print(year, "Not leap year")
else:
    print(year, "Not leap year")
