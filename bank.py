'''
problem set conditionals
In a file called bank.py, implement a program that prompts the user for a greeting.
If the greeting starts with an “h” (but not “hello”), output $20.
Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
'''
greet = input("Greeting: ")
if "hello" in greet.lower():
    print("$0")

elif greet.lower().index("h") in [0]:
    print("$20")

else:
    print("$100")
