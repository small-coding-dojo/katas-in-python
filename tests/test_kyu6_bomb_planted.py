import pytest

from array import *

from kyu6_bomb_planted.bomb_has_been_planted import bomb_has_been_planted


def space(distance):
    return ['0' for _ in range(distance)]


def create_empty_matrix(width, height):
    return [['0' for _ in range(width)] for _ in range(height)]


class BombAndCounterTerroristInSameRow:
    left = "TODO: set left to 'B' or 'CT'"
    right = "TODO: set right to 'B' or 'CT'"
    row = 0  # TODO: set row to an integer number

    @pytest.mark.parametrize('distance,time', [
        (1, 0),
        (1, 1),
        (1, 10),
        (2, 11),
        (3, 12)
    ])
    def test_bomb_defused_when_time_too_short(self, distance, time):
        m = create_empty_matrix(distance + 1, self.row + 1)
        m[self.row][0] = self.left
        m[self.row][distance] = self.right
        assert not bomb_has_been_planted(m, time)

    @pytest.mark.parametrize('distance,time', [
        (1, 11),
        (2, 12),
        (3, 13)
    ])
    def test_bomb_defused_when_time_sufficient(self, distance, time):
        m = create_empty_matrix(distance + 1, self.row + 1)
        m[self.row][0] = self.left
        m[self.row][distance] = self.right
        assert bomb_has_been_planted(m, time)


class TestBombLeftCounterTerroristRightInRow0(BombAndCounterTerroristInSameRow):
    left = 'B'
    right = 'CT'
    row = 0


class TestBombLeftCounterTerroristRightInRow1(BombAndCounterTerroristInSameRow):
    left = 'B'
    right = 'CT'
    row = 1


class TestCounterTerroristLeftBombRightInRow5(BombAndCounterTerroristInSameRow):
    left = 'CT'
    right = 'B'
    row = 5


class TestVertical:
    top = 'B'
    bottom = 'CT'
    column = 0

    @pytest.mark.parametrize('distance,time', [
        (1, 0),
        (1, 10),
    ])
    def test_bomb_defused_when_time_too_short(self, distance, time):
        m = create_empty_matrix(self.column + 1, distance + 1)
        m[0][self.column] = self.top
        m[distance][self.column] = self.bottom

        assert not bomb_has_been_planted(m, time)

    @pytest.mark.parametrize('distance,time', [
        (1, 11),
    ])
    def test_bomb_defused_when_time_sufficient(self, distance, time):
        m = [[self.top]] + [['0']] * (distance - 1) + [[self.bottom]]
        assert bomb_has_been_planted(m, time)


class TestDefuseKit:
    def test_bomb_defused_when_time_sufficient(self):
        m = create_empty_matrix(3, 3)
        m[0][0] = 'B'
        m[0][1] = 'K'
        m[1][1] = 'CT'
        assert bomb_has_been_planted(m, 7)
