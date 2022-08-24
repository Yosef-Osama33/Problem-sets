from pyfiglet import Figlet
import sys
figlet = Figlet()


if len(sys.argv)  == 1:
    israndom = True

elif len (sys.argv) == 3:
    israndom = False


else:
    print("Invalid syntax")
    sys.exit(1)

x = input("Input: ")

figlet.getFonts()

if israndom == False:
    figlet.setFont(font=sys.argv[2])


print(f"Output: "(figlet.renderText(x)))

    



