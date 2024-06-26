import pytest

from kyu6_is_prime.is_prime import is_prime


@pytest.mark.parametrize('test_input', [-1, 0, 1, 4, 6, 8, 9, 10])
def test_not_prime(test_input):
    assert not is_prime(test_input)


@pytest.mark.parametrize('test_input', [2, 3, 5, 7, 11, 5009, 12345653, 999999999989, 1000000000000279]) # 12345653
def test_prime(test_input):
    assert is_prime(test_input)
