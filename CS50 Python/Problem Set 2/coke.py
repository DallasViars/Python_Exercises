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