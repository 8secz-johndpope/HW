import pytest
from people.Human import Human
from people.Woman import Woman

@pytest.fixture
def human():
    return Human()

@pytest.fixture
def woman():
    return Woman()
