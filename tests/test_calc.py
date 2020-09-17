import pytest
from calc import line


@pytest.mark.parametrize('a, b, answer', [
    (1, 2, [-2.0]),
    (1, -3, [3.0]),
    (1, 'Masha', [])
])
def test_line(a, b, answer, human):
    assert line(a, b) == answer


def test_lineNegative(human):
    assert line() == []
