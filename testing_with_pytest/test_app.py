# test_app.py
import pytest
from app import add_numbers
from app import divide_numbers
 

def test_add_numbers():
    # Test cases
    assert add_numbers(1, 2) == 3, "1 + 2 should be 3"
    assert add_numbers(-1, -1) == -2, "-1 + -1 should be -2"
    assert add_numbers(0, 0) == 0, "0 + 0 should be 0"
    assert add_numbers(100, 200) == 300, "100 + 200 should be 300"


def test_add_numbers_with_non_numbers():
    with pytest.raises(TypeError):
        add_numbers("1", 2), "This should raise a TypeError"


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(1, 0), "This should raise a ZeroDivisionError"


### In short
# - Write your function in a `.py` file.
# - Write test cases in a separate `test_*.py` file using `assert` statements.
# - Use pytest to run the tests and verify the outputs.
# - Enhance tests with parameterized cases and exception handling if needed.


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -1, -2),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add_numbers_param(a, b, expected):
    assert add_numbers(a, b) == expected
