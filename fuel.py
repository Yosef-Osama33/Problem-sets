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
