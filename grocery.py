'''
In a file called grocery.py, implement a program that prompts the user for items, one per line,
until the user inputs control-d (which is a common way of ending one’s input to a program).
Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times
the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.
'''
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

