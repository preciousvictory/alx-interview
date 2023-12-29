#!/usr/bin/python3
"""prime_game.py
"""


def isPrimeNo(num):
    """
    Check if number is a prime number
    """
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
        return True
    else:
        return False

def isWinner(x, nums):
    """
    Maria and Ben are playing a game.
    Given a set of consecutive integers starting from 1 up to and including n,
    they take turns choosing a prime number from the set and removing that
    number and its multiples from the set.
    The player that cannot make a move loses the game.

    They play x rounds of the game, where n may be different for each round.
    Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is.
    
    Prototype: def isWinner(x, nums)
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """

    winner = {i: None for i in range(1, x + 1)}
    players = ['Maria', 'Ben']

    for rounds in range(1, x + 1):
        n = [i for i in range(1, nums[rounds - 1] + 1)]
        
        player = 0
        win = None
        len_ = len(n)

        while len(n) > 0:
            if len_ == 1:
                win = 1
                break
            if len(n) == 1:
                win = player

            pick = n[0]
            for i in n:
                print('-', i)
                if isPrimeNo(i):
                    pick = i
                    break
            print('pick', pick, n)

            for i in n:
                if i == pick or i % pick == 0:
                    n.remove(i)

            print('p', player)
            win = player

            if len(n) != 1:
                if player == 0:
                    player = 1
                else:
                    player = 0
        if win == None:
            winner[rounds] = None
        else:
            winner[rounds] = players[win]

    print(winner)
    M = 0
    B = 0
    for key, value in winner.items():
        if value == 'Ben':
            B += 1
        elif value == 'Maria':
            M += 1

    if M > B:
        return 'Maria'
    else:
        return 'Ben'
