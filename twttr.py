'''
In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text
    but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
'''
x = input("Input: ")
print("Out put: ", end="")

for letter in x:

    if not letter.lower() in [ "o", "a" , "e", "i" , "u"]:
        print(letter, end ="")

