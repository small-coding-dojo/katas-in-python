import pytest

from kyu6_persistent_bugger.persistence import persistence


@pytest.mark.parametrize("test_input,expected", [
    (0, 0),
    (10, 1),
    (25, 2),
    (999, 4),
])
def test_persistence(test_input, expected):
    assert persistence(test_input) == expected
