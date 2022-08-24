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