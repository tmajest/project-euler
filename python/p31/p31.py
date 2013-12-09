# http://projecteuler.net/problem=31


def solve(total, currCoin, coins):
    if total == 200:
        return 1
    elif total >= 200:
        return 0

    solutions = 0 
    for coin in coins:
        if coin >= currCoin:
            solutions += solve(total + coin, coin, coins)

    return solutions


coins = [1, 2, 5, 10, 20, 50, 100, 200]
print solve(0, 1, coins)
