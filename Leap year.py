def is_leap(year):
    year = int( input( "What your year" ) )
    leap = False
    not_leap = True
    if year % 4 == 0:
        print(leap)
    elif year % 100 == 0:
        print(not_leap)
    elif year % 400 == 0:
        print(leap)
    return leap
is_leap("year")

# year = int(input("What your year"))