#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """Determines the winner after x rounds of the Prime Game.
    Args:
        x (int): The number of rounds.
        nums (list): List of integers for each round.

    Returns:
        str: Name of the player that won the most rounds,
        or None if it's a tie.
    """
    if x <= 0 or not nums or x != len(nums):
        return None

    ben = 0
    maria = 0
    max_num = max(nums)

    a = [True] * (max_num + 1)
    a[0], a[1] = False, False

    for i in range(2, int(max_num**0.5) + 1):
        if a[i]:
            for multiple in range(i*i, max_num + 1, i):
                a[multiple] = False

    for n in nums:
        prime_count = sum(a[:n + 1])
        if prime_count % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None
