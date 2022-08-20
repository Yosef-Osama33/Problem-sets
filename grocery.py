d = {}

while True:
    try :
        key = input("")
        if key in d:
            d[key] += 1

        else:
            d[key] = 1

    except EOFError :

        for key in d:
            print(d[key] , key.capitalize())


        break

