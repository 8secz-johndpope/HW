import pytest
import calc as calc

@pytest.mark.parametrize('a, b, answer', [
    (1, 2, [-2.0]),
    (1, -3, [3.0]),
    (1, 'Masha', [])
])
def test_line(a, b, answer, human):
    assert calc.line(a, b) == answer


def test_lineNegative(human):
    assert calc.line() == []

@pytest.mark.parametrize('a, b, c, answer', [
    (1, 2, 1, [-1]),
    (1, -2, -3, [3, -1]),
    ('vasya', 'petya', 'slava', []),
    (-1, -2, 15, [-5, 3])
])
def test_square(a, b, c, answer):
    assert calc.square(a, b, c) == answer

def test_squareNegative(woman):
    assert calc.square() == []

@pytest.mark.parametrize('a, b, c, d, answer',[
    (2, -11, 12, 9, [-0.5000000000000002, 3, 3]),
    ('petya', 3, 'vasya', 4, []),
    (1, 2, 1, 0, [-1.0])
])

def test_cube(a, b, c, d, answer):
    assert calc.cube(a, b, c, d) == answer

def test_cubeNegative(woman):
    assert calc.cube(woman) == []

