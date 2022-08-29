'''
In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively)
and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits,
which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster
(e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.
'''
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
