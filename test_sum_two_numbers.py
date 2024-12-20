# Import the function to be tested
from sum_two_numbers import sum_two_numbers

# Test for adding positive numbers
def test_sum_positive_numbers():
    result = sum_two_numbers(3, 5)
    assert result == 8, f"Expected 8, but got {result}"

# Test for adding negative numbers
def test_sum_negative_numbers():
    result = sum_two_numbers(-3, -5)
    assert result == -8, f"Expected -8, but got {result}"

# Test for summing positive and negative numbers
def test_sum_positive_and_negative():
    result = sum_two_numbers(5, -3)
    assert result == 2, f"Expected 2, but got {result}"

# Test for summing zero with a number
def test_sum_with_zero():
    result = sum_two_numbers(0, 5)
    assert result == 5, f"Expected 5, but got {result}"

# Test for summing two zeros
def test_sum_two_zeros():
    result = sum_two_numbers(0, 0)
    assert result == 0, f"Expected 0, but got {result}"
