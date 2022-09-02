'''
problem set File I/O
'''
import sys
import csv
from tabulate import tabulate

def main():
    check_command_line_arg()
    table =[]
    try:
        with open(sys.argv[1], "r")as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)

    except FileNoteFoundError:
        sys.exit("File does not exist")

    print(tabluate(table[1:], headers= table[o]))
def check_command_line_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a csv file")

if __name__ == "__main__":
    main()
