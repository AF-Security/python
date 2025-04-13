# taqueria 

# enables a user to place an order, prompting them for items, one per line, until the user inputs control-d
# After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places
# Treat the user’s input case insensitively
# Ignore any input that isn’t an item
# Assume that every item on the menu will be titlecased

def main():
    total = 0
    while True:
        try:
            x = input("Item: ")
            x = x.casefold().title()
            x = price_check2(x)
            total = total + x
            print(f"Running Total: ${total:.2f}")
        except ValueError:
             pass
        except NameError:
             pass
        except TypeError:
             pass
        except EOFError:
             print("\n")
             break
        

def price_check(item):
        prices = {
                "Baja Taco": 4.25,
                "Burrito": 7.50,
                "Bowl": 8.50,
                "Nachos": 11.00,
                "Quesadilla": 8.50,
                "Super Burrito": 8.50,
                "Super Quesadilla": 9.50,
                "Taco": 3.00,
                "Tortilla Salad": 8.00
        }
        for price in prices:
            if price == item:
                return prices[price]
                # total = total + prices[price]
                # print(f"${total:.2f}")
            

def price_check2(item):
    prices = {
                "Baja Taco": 4.25,
                "Burrito": 7.50,
                "Bowl": 8.50,
                "Nachos": 11.00,
                "Quesadilla": 8.50,
                "Super Burrito": 8.50,
                "Super Quesadilla": 9.50,
                "Taco": 3.00,
                "Tortilla Salad": 8.00
                }
    if item in prices:
         return prices[item]
    elif KeyError:
         pass
          

main()