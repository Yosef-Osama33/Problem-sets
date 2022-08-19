x = input("Greeting: ")

x = x.lower()

if "hello" in x:
    print("$0")
elif x[0] == "h":
    print("$20")
else:
    print("$100")