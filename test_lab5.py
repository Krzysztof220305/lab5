import pytest
from lab5 import add

@pytest.fixture
def data():
    return (8, 2)
def test_add_with_data(data):
    a, b = data
    assert add(8, 2) == 10