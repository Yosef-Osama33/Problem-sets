expression = (input("Expression: "))
x, y, z = expression.split(" ")
v = float(x)
c = float(z)
if y == "+":
    print(v + c)
elif y == "-":
    print(v - c)
elif y == "*":
    print(v * c)
elif y == "/":
    print(v / c)
