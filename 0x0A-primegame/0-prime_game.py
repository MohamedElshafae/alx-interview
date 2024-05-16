#!/usr/bin/python3


def isWinner(x, nums):
    if not nums or x < 1:
        return None

    def sieve(max_n):
        is_prime = [True] * (max_n + 1)
        p = 2
        while p * p <= max_n:
            if is_prime[p] == True:
                for i in range(p * p, max_n + 1, p):
                    is_prime[i] = False
            p += 1
        primes = []
        for p in range(2, max_n + 1):
            if is_prime[p]:
                primes.append(p)
        return primes

    max_n = max(nums)
    primes = sieve(max_n)

    def play_game(n):
        available = set(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben

        while True:
            move_made = False
            for prime in primes:
                if prime in available:
                    multiples = set(range(prime, n + 1, prime))
                    available -= multiples
                    move_made = True
                    break

            if not move_made:
                return 1 - turn  # The player who cannot make a move loses

            turn = 1 - turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
