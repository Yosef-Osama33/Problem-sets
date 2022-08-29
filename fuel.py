'''
In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y,
wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer,
how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is
essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.
'''
while True:

    x = input("Fraction: ")
    try:    
        [x, y, z] = x.split()
        if y == ("/"):
            new_x = int(x)
            new_z = int(z)
        c = (new_x/new_z)
        if c <= 1:
            break

        
    except (ValueError, ZeroDivisionError):
        pass

b = int(c * 100)

if b == 0:
    print("E")
elif b == 100:
    print("F")

else:
    print(b)
