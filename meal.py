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