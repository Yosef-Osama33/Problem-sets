'''
In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins, , that they would like to buy.
If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
'''
import sys
import requests

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    
    except:
        print("Command-line argument is not a number")
        sys.exit(1)

else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = r.json()
    bitcoin = response['bpi']['USD']['rate_float']
    total = bitcoin * value
    print(f"${total:,.4f}")

except requests.RequestException:
    print("RequestExceptoin")
    sys.exit(1)
