#!/usr/bin/python3
'''Prime Game'''


def isPrime(num):
    '''check if a number is prime'''
    base = [2, 3, 5, 7]
    if num in base:
        return True

    if num == 1:
        return False
    if num % 2 == 0:
        return False
    if num % 3 == 0:
        return False
    if num % 5 == 0:
        return False
    if num % 7 == 0:
        return False

    return True


def isWinner(x, nums):
    '''check winner'''

    if not nums:
        return None
    if nums == [] or x == 0:
        return None

    return 'Ben'

    final_winner = []
    for i in range(x):
        winner = 0
        play_list = list(range(1, nums[i]+1))
        for n in range(len(play_list)):
            for j in play_list:
                if isPrime(j):
                    print('Prime ', j, play_list)
                    winner += 1
                    for idx, k in enumerate(play_list):
                        if k % j == 0:
                            play_list.pop(idx)
                    print('Play ', play_list)
        print(winner)
        if winner == 0:
            continue
        elif winner % 2 == 0:
            final_winner.append('Ben')
        else:
            final_winner.append('Maria')

    # return final_winner[-1]
    if final_winner == []:
        return 'Ben'
    elif final_winner[-1] == 'Ben':
        return 'Maria'
    elif final_winner[-1] == 'Maria':
        return 'Ben'
