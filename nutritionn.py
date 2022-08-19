
fruits = {
    "apple" : 130 ,
    "banana" : 110 ,
    "avocado" : 50 ,
    "sweet cherries" : 100
}



fruit =input("Item: ")


for s in fruits:
    if s == fruit:

        print("calories: " , fruits[s])