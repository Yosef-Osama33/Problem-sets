def main():
    x = input()
    result = convert(x)
    print(result)


def convert (x):
   x1 = x.replace(":)", '🙂')
   x2 = x1.replace(":(" ,'🙁')
   return x2

main()