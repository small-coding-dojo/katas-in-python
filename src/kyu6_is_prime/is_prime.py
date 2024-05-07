def sieve_of_atkin(num):
    """Sieve of Atkin IS TOO SLOW ...

    See: https://www.geeksforgeeks.org/sieve-of-atkin/
    """
    sieve = [False] * (num + 1)
    if num >= 2:
        sieve[2] = True
    if num >= 3:
        sieve[3] = True

    x = 1
    while x * x <= num:
        y = 1
        while y * y <= num:
            n = (4 * x * x) + (y * y)
            if n <= num and (n % 12 == 1 or n % 12 == 5):
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if n <= num and n % 12 == 7:
                sieve[n] ^= True

            n = (3 * x * x) - (y * y)
            if x > y and n <= num and n % 12 == 11:
                sieve[n] ^= True

            y += 1
        x += 1

    r = 5
    while r * r <= num:
        if sieve[r]:
            for i in range(r * r, num + 1, r * r):
                sieve[i] = False

    result = [i for i, value in enumerate(sieve) if value]
    return result


def is_prime(num):
    print ("number: {}".format(num), flush=True)
    primes = sieve_of_atkin(num)
    return num in primes
