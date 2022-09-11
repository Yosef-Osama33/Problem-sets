'''
In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text
    but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
'''
word = input("Input: ")
print("Output: ", end="")
for letter in word:
    if not letter.lower()in ["a", "u", "i", "o", "e"]:
        print(letter, end="")

