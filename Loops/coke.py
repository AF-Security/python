# coke machine

# prompt a user to input a coin, one at a time
# each time informing the user of the amount due
# once the user has input at least 50 cents, output how many cents in change the user is owed
# assume the user will only input integers, and ignore any integer that isn't an accepted denomination

def main():
    user_coins = input("Insert Coin: ")
    user_coins = int(user_coins)
    if coin_check(user_coins):  
        total_input(user_coins)
    else:
        print("Amount Due: 50")

def coin_check(coin):
    if coin == 5 or coin == 10 or coin == 25:
        return coin 
        
def total_input(change):
    if change < 50:
        print("Amount Due: ")
   #total = total + change
    
main()


def main():
    x = input("Insert Coin: ")
    coin_check(x)


def coin_check(coin):
     coin = int(coin)
     if coin == 5 or coin == 10 or coin == 25:
        return coin 
     
def running_total(coin):
    total = total + coin
    if total < 50:
        print("Amount Due: " + 50-total)

main()