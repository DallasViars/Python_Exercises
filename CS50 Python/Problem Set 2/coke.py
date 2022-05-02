# Coke Machine
# CS50 Coke Bottle
# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.


def main():
    vend()


def vend():
    cost = 50
    paid = 0
    change = 0
    while True:
        coin = int(input("Insert Coin: "))
        if coin == 5 or coin == 10 or coin == 25:
            paid += coin
            if paid < 50:
                print(f"Amount due: {cost - paid}")
            else:
                print(f"Change owed: {paid - cost}")
                break
        else:
            print(f"Amount due: {cost - paid}")



main()