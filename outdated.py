'''
In a file called outdated.py, implement a program that prompts the user for a date, anno Domini,
in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format,
prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
'''
months =  [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date ")
    try:
         month , day , year = date.split("/")

         if (int(month) >=1 and int(month) <= 12 and 1 <=int(day) <=31 ):
            break

    except:
        try:
            new_month, new_day, year = date.split()
            for i in range(len(months)):
                if new_month == months[i]:
                    month = i + 1

                day = new_day.replace(",","")
            if (int(month) >=1 and int(month) <= 12 and 1 <=int(day) <=31 ):
                break

        except:
            print()
            pass

print (f"{year}-{month}-{day}")
