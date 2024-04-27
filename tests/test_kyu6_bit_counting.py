import pytest

from kyu6_bit_counting.count_bits import count_bits


@pytest.mark.parametrize('value, expected', [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 1),
    (5, 2),
    (7, 3),
])
def test_count_bits(value, expected):
    assert count_bits(value) == expected
