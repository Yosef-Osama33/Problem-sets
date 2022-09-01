'''
problem set loops
In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time,
each time informing the user of the amount due. Once the user has inputted at least 50 cents, 
output how many cents in change the user is owed. Assume that the user will only input integers,
and ignore any integer that isn’t an accepted denomination.
'''
amount = 50
while amount > 0:
    print(f"Amount Due: {amount}")

    coin = int(input("Insert coin: "))

    if coin in [5, 15, 25]:
        amount = amount - coin


owed =  abs(amount)
print(f"Change Owed: {owed}")



