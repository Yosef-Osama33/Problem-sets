'''
In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively)
and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits,
which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster
(e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.
'''
calories ={"apple": 130,
"avocado":50,
"banana":110,
"cantaloupe":60,
"Grapefruit":60,
"grapes":90,
"Honeydew melon":50,
"Kiwifruit":90,
"lemon":15,
"nectarine":60,
"orange":80,
"peach":60,
"pear":100,
"pine apple":50,
"plums":70,
"Strawberries":50,
"sweet cherries":100,
"water melon":80,
"tangerine":50
}


fruits =input("Item: ").lower()
for fruit in calories:
    if fruit == fruits:
        print("Calories: ",calories[fruits] )
