from functools import reduce
from operator import mul


def persistence(n):
    if n <= 9:
        return 0

    digits = [int(c) for c in str(n)]
    product = reduce(mul, digits)

    return 1 + persistence(product)
