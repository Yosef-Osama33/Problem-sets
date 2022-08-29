'''
In a file called adieu.py, implement a program that prompts the user for names, one per line,
until the user inputs control-d. Assume that the user will input at least one name.
Then bid adieu to those names, separating two names with one and, three names with two commas and one and,
and  names with  commas and one and, as in the below:
'''
import inflect

d = {}
while True:
    try:
        key = input("Name: ")
        d.append(key)

    except EOFError:
        print()
        break
output = p.join(d)
print("Adieu, adieu, to" + output)
