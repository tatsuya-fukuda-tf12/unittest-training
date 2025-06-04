from fizzbuzz.fizzbuzz import fizzbuzz
import pytest

# 3の倍数
def test_fizzbuzz_multiple_of_3():
    # Arrange
    input_value = 3
    expected_output = "Fizz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output

# 5の倍数
def test_fizzbuzz_multiple_of_5():
    # Arrange
    input_value = 5
    expected_output = "Buzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output

# 3かつ5の倍数
def test_fizzbuzz_multiple_of_15():
    # Arrange
    input_value = 15
    expected_output = "FizzBuzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output

# 上記以外の整数
def test_fizzbuzz_other_number():
    # Arrange
    input_value = 7
    expected_output = str(input_value)

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output

# 境界値
def test_fizzbuzz_number_of_1():
    # Arrange
    input_value = 1
    expected_output = str(input_value)

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


def test_fizzbuzz_number_of_1000():
    # Arrange
    input_value = 1000
    expected_output = "Buzz"

    # Act
    result = fizzbuzz(input_value)

    # Assert
    assert result == expected_output


def test_fizzbuzz_number_of_0():
    # Arrange
    input_value = 0
    with pytest.raises(ValueError):
        fizzbuzz(input_value)


def test_fizzbuzz_number_of_1001():
    # Arrange
    input_value = 1001
    with pytest.raises(ValueError):
        fizzbuzz(input_value)

def test_fizzbuzz_not_integer():
    # Arrange
    input_value = 0.5
    with pytest.raises(TypeError):
        fizzbuzz(input_value)
