import calendar

year = int(input("Enter an year:"))
if (year % 4 == 0):
    if (year % 400 == 0 and year % 100 ==0):
        print("Leap year")
    else:
        print("Not a Leap year")
else:
    print("Not a leap year")

print("Calender leap: ",calendar.isleap(year))