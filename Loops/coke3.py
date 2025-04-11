

def main():
    amount_due = get_coin()
    # if amount_due < 50:
        # print(f"Amount Due: {amount_due}")
    # elif amount_due >=50:    
        # print(f"Change Due: {amount_due}")



def get_coin():    
    total = 0 
    while True:
        n = int(input("Instert Coin: "))
        if n == 5 or n == 10 or n == 25:
            total = total + n
            amount_due = 50 - total
            if amount_due > 0: 
                print(f"Amount Due: {amount_due}")
            elif amount_due <= 0:
                change_due = 0 - amount_due 
                print(f"Change Due: {change_due}")
                break

        elif n >= 0:
            total = total
            amount_due = 50 - total
            print(f"Amount Due: {amount_due}")
        # elif total > 50:
            # print("Change Due: ")
        # else:
            # return amount_due


main()