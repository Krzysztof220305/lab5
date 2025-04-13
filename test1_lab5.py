import pytest
from lab5 import add

@pytest.mark.parametrized("a ,b ,expected", [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
])
def tests_add(a, b, expected):
    assert add(a, b) == expected
