amount =  50
while amount > 0:
    print ("Amount Due" , amount)

    coin = int(input("Insert Coin: "))

    if coin in [10 , 25 , 5]:
        amount = (amount - coin)
        print(amount)
 




