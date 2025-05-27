#LAB - 3
def min_coins(coins, target):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while target >= coin:
            target -= coin
            result.append(coin)
    return result

coins = [1, 5, 10, 25]
target = 75
change = min_coins(coins, target)
print(f"Target: {target}\nCoins used: {change}\nCoin Amount: {len(change)}")
#AV
