print("Amount Due: 50")

due = 50
cost = 0
while True:
    coin = int(input('Insert Coin: '))
    if coin == 25 or coin == 10 or coin == 5:
        due -= coin
        cost += coin
    if due < 0:
        due = -due
    if cost >= 50:
        print(f"Change owed: {cost - 50}")
        break
    else:
        print(f"Amount Due: {due}")
