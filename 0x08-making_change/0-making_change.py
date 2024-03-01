#!/usr/bin/python3
"""makeChange function"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    coins = sorted(coins)
    i = len(coins) - 1
    count = 0
    while total >= 0 and i >= 0:
        if coins[i] > total:
            i -= 1
            continue
        else:
            count += total // coins[i]
            total = total % coins[i]
            if coins[i] <= total:
                continue
            else:
                i -= 1
    if total == 0:
        return count
    return -1
