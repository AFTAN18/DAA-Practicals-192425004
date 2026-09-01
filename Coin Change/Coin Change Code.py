coins = [25, 10, 5, 1]
amount = int(input("Enter amount: "))
coins_used = []
for coin in coins:
    while amount >= coin:
        amount -= coin
        coins_used.append(coin)
print("Coins used:", coins_used)
print("Number of coins:", len(coins_used))
