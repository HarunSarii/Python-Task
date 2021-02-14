#leap year

year = int(input("enter the year: "))

leap = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


if leap:
    print(year, "is a leap year!")
else:
    print(year, "is not a leap year!")
