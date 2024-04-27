from kyu6_bit_counting.count_bits import count_bits


def test_count_bits():
    assert count_bits(0) == 0


def test_count_bits_():
    assert count_bits(1) == 1


def test_count_bits__():
    assert count_bits(2) == 1


def test_count_bits___():
    assert count_bits(3) == 2


def test_count_bits____():
    assert count_bits(4) == 1


def test_count_bits_____():
    assert count_bits(5) == 2


def test_count_bits______():
    assert count_bits(7) == 3
