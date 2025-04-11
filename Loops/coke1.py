def main():
    x = int(input("Insert Coin: "))
    x = coin_check(x)
    x = running_total(x)


def coin_check(coin):
     coin = int(coin)
     if coin == 5 or coin == 10 or coin == 25:
        return coin 
     
def running_total(coin):
    total = 0 + coin 
    if total < 50:
        print(f"Amount Due: " + (50 - {total}))
    elif total > 50:
        print(f"Change Due: " + ({total}-50))
    elif total == 50:
        print("Change Due: 0")
    return total

main()