x =input("What is the Great Question of Life, the Universe, and every thing? ")
if x.strip()== "42":
    print("Yes")
elif x.strip().lower() == ("forty-two"):
    print ("yes")
elif x.lower().strip() == ("forty two"):
    print ("yes")
else:
    print ("no")