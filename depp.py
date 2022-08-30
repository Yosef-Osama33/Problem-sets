'''
problem set conditional
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
'''
answer = input("What is the Answer to the Great Question of life, the Universe, and Everything? ")
if answer == ("42") :
    print("Yse")

elif answer.lower().strip() == ("forty two") or  ("forty-two") :
    print("Yes")
else:
    print("no")

