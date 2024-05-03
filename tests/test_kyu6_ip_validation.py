import pytest

from kyu6_ip_validation.is_valid_ip import is_valid_IP


@pytest.mark.parametrize("input", [
    "",
    " ",
    ".",
    "127.0.0.1.",
    "256.0.0.1",
    "1.2.3.4 \n",
    "\n 1.2.3.4",
])
def test_is_valid_IP_when_invalid(input):
    assert not is_valid_IP(input)


@pytest.mark.parametrize("input", [
    "0.0.0.0",
    "127.0.0.1",
])
def test_is_valid_IP_when_valid(input):
    assert is_valid_IP(input)
