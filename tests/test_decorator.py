import pytest
import decorator as decorator

@pytest.mark.parametrize('a, answer',[
    (2, 4),
    (3, 9),
    ('va$9a', [])
])

def test_f2(a,answer):
    return decorator.f2(a) == answer

def test_f2Negative():
    return decorator.f2 == []

@pytest.mark.parametrize('a, b, answer',[
    (6, 5, 1),
    (8, 7, 1),
    (9, 9, 0),
    ('22','petya',[])
])

def test_f3(a, b, answer):
    return decorator.f3(a, b) == answer

def test_f3Negative():
    return decorator.f3 == []