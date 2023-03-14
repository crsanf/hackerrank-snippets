# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

date_string = input()
split_date = date_string.split(' ')
month,day,year = [int(x) for x in split_date]
day = calendar.weekday(year,month,day)

if day == 0:
    print("MONDAY")
elif day == 1:
    print("TUESDAY")
elif day == 2:
    print("WEDNESDAY")
elif day == 3:
    print("THURSDAY")
elif day == 4:
    print("FRIDAY")
elif day == 5:
    print("SATURDAY")
elif day == 6:
    print("SUNDAY")
