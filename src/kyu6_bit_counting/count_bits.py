from math import log, floor


def count_bits(n):
    if n == 0:
        return 0

    highest_bit = floor(log(n, 2))
    bits = range(highest_bit, -1, -1)
    set_bits = [1 if n & 2 ** bit else 0 for bit in bits]
    return sum(set_bits)


if __name__ == "__main__":
    print(count_bits(12345))
