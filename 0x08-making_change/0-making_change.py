#!/usr/bin/python3
'''making change'''


def makeChange(coins: list, total):
    '''Given a pile of coins of different values,
    determine the fewest number of coins needed to
    meet a given amount `total` '''
    if total <= 0:
        return 0
    if coins == []:
        return -1

    change_count = 0
    remainder = total
    sorted_coin = sorted(coins, reverse=True)
    for i in sorted_coin:
        change_count += remainder // i
        remainder = remainder % i
        if remainder == 0:
            return change_count

    return -1
