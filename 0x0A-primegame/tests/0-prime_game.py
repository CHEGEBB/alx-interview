#!/usr/bin/python3
def sieve(n):
    """Uses the Sieve of Eratosthenes to find all prime numbers up to n."""
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def prime_game(n):
    """Plays the prime game and returns the winner."""
    primes = sieve(n)
    moves = [0] * (n + 1)
    for prime in primes:
        for multiple in range(prime, n + 1, prime):
            moves[multiple] += 1
    return moves


def isWinner(x, nums):
    """Determines the winner of the Prime Game after x rounds."""
    max_num = max(nums)
    moves = prime_game(max_num)
    maria_wins = 0
    ben_wins = 0
    for num in nums:
        if moves[num] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
