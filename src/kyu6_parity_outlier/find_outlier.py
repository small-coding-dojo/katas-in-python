def is_odd(integer):
    return integer % 2 == 1


def is_even(integer):
    return integer % 2 == 0


def find_outlier(integers):
    count_of_odds = integers[0] % 2 + integers[1] % 2 + integers[2] % 2

    if count_of_odds < 2:
        predicate = is_odd
    else:
        predicate = is_even

    return next(filter(predicate, integers))
