import pytest

from kyu5_rgb_to_hex.rgb import rgb


@pytest.mark.parametrize('r, g, b, expected', [
    (0, 0, 0, "000000"),
    (9, 9, 9, "090909"),
    (10, 10, 10, "0A0A0A"),
    (10, 10, 16, "0A0A10"),
    (10, 255, 16, "0AFF10"),
    (255, 0, 26, "FF001A"),
    (256, 0, 0, "FF0000"),
    (-3, -3, 299, "0000FF"),
])
def test_rgb(r, g, b, expected):
    assert rgb(r, g, b) == expected
