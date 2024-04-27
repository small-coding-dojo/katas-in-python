from math import log, floor


def count_bits(n):
    if n == 0:
        return 0

    highest_bit = floor(log(n, 2))
    possible_bits = range(highest_bit, -1, -1)
    binary_representation = [n & 2 ** bit > 0 for bit in possible_bits]

    return binary_representation.count(True)


if __name__ == "__main__":
    print(count_bits(12345))
