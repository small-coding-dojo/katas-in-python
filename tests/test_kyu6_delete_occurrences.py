import pytest

from kyu6_delete_occurrences.delete_nth import delete_nth


@pytest.mark.parametrize('input_order, input_max_e, expected', [
    pytest.param([1], 1, [1], id="reproduce input for [1]"),
    pytest.param([2], 1, [2], id="reproduce input for [2]"),
    pytest.param([3, 4, 5], 1, [3, 4, 5], id="reproduce input for [3, 4, 5]"),
])
def test_reproduce_input(input_order, input_max_e, expected):
    assert delete_nth(input_order, input_max_e) == expected


@pytest.mark.parametrize('input_order, input_max_e, expected', [
    pytest.param([1, 1], 1, [1], id="remove last of [1, 1]"),
])
def test_remove_last(input_order, input_max_e, expected):
    assert delete_nth(input_order, input_max_e) == expected

