'''
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements
or Invalid if it does not. Assume that any letters in the user’s input will be uppercase.
Structure your program per the below, wherein is_valid returns True if s meets all requirements and
False if it does not. Assume that s will be a str. You’re welcome to implement additional functions
for is_valid to call (e.g., one function per requirement).
'''
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) < 6:

        return False
    if s[0].isalpha() == False  or s[1].isalpha() == False :
                return False 

    for c in  s :
        if c == ["." , "-" , " " , "!" , "?"]  :
            return False
    


main()
