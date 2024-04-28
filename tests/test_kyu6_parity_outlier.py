import pytest

from kyu6_parity_outlier.find_outlier import find_outlier


def id_func(param):
    return repr(param)


@pytest.mark.parametrize('test_input, expected', [
    ([1, 2, 4], 1),
    (([3, 2, 4]), 3),
    ([231, 2, 4], 231),
],
                         ids=id_func)
def test_find_outlier_when_three_values_and_first_is_odd(test_input, expected):
    assert find_outlier(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ([2, 1, 1], 2),
    (([4, 1, 3]), 4),
],
                         ids=id_func)
def test_find_outlier_when_three_values_and_first_is_even(test_input, expected):
    assert find_outlier(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ([2, 1, 2], 1),
],
                         ids=id_func)
def test_find_outlier_when_three_values_and_second_is_odd(test_input, expected):
    assert find_outlier(test_input) == expected
