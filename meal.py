'''
In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.
If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour 
time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, 
whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
'''
def main():
    x =input(("What time is it? "))
    time = convert (x)
    if 8 >=(time)>= 7:
        print("breakfast time")
    elif 13>=(time)>=12:
        print ("lunch time")
    elif 19>=(time)>=18:
        print("dinner time")

    else:
        print("")



def convert(time):
    c, z = time.split(":")
    hours = (c)
    minutes = float(z) /60
    return minutes + float(hours)



if __name__ == "__main__":
    main()
