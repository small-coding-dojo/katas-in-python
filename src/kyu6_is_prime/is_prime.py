# Python 3 program for
# implementation of
# Sieve of Atkin
import math


def SieveOfAtkin(limit):
    # 2 and 3 are known
    # to be prime
    if limit > 2:
        print(2, end=" ")
    if limit > 3:
        print(3, end=" ")

    # Initialise the sieve
    # array with False values
    sieve = [False] * (limit + 1)
    for i in range(0, limit + 1):
        sieve[i] = False

    '''Mark sieve[n] is True if
    one of the following is True:
    a) n = (4*x*x)+(y*y) has odd
    number of solutions, i.e.,
    there exist odd number of
    distinct pairs (x, y) that
    satisfy the equation and
    n % 12 = 1 or n % 12 = 5.
    b) n = (3*x*x)+(y*y) has
    odd number of solutions
    and n % 12 = 7
    c) n = (3*x*x)-(y*y) has
    odd number of solutions,
    x > y and n % 12 = 11 '''
    x = 1
    while x * x <= limit:
        y = 1
        while y * y <= limit:

            # Main part of
            # Sieve of Atkin
            n = (4 * x * x) + (y * y)
            if (n <= limit and (n % 12 == 1 or
                                n % 12 == 5)):
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True

            n = (3 * x * x) - (y * y)
            if (x > y and n <= limit and
                    n % 12 == 11):
                sieve[n] ^= True
            y += 1
        x += 1

    # Mark all multiples of
    # squares as non-prime
    r = 5
    while r * r <= limit:
        if sieve[r]:
            for i in range(r * r, limit + 1, r * r):
                sieve[i] = False

        r += 1

    # Print primes
    # using sieve[]
    primes = [2,3]
    for a in range(5, limit + 1):
        if sieve[a]:
            print(a, end=" ")
            primes.append(a)

    return primes

# This code is contributed
# by Smitha

def sieve_of_atkin(num):
    return SieveOfAtkin(num)



def is_prime(num):
    return is_prime_simple(num)
    print ("number: {}".format(num), flush=True)
    primes = sieve_of_atkin(num)
    return num in primes

def is_prime_simple(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0 :
            return False
    return True