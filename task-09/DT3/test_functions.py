import pytest
from functions import add_numbers, check_even_odd, get_first_element, divide_numbers, contains_keyword

def test_add_numbers_normal():
    assert add_numbers(3, 4) == 7
    assert add_numbers(-2, 5) == 3
    assert add_numbers(0, 0) == 0


def test_add_numbers_edge_cases():
    assert add_numbers(1e10, 1e10) == 2e10
    assert add_numbers(-1e10, 1e10) == 0


def test_add_numbers_type_error():
    with pytest.raises(TypeError):
        add_numbers("a", 2)

def test_check_even_odd_normal():
    assert check_even_odd(4) == "Even"
    assert check_even_odd(7) == "Odd"


def test_check_even_odd_edge_cases():
    assert check_even_odd(0) == "Even"
    assert check_even_odd(-2) == "Even"
    assert check_even_odd(-3) == "Odd"


def test_get_first_element_normal():
    assert get_first_element([1, 2, 3]) == 1
    assert get_first_element(["a", "b"]) == "a"


def test_get_first_element_empty():
    result = get_first_element([])
    assert result is None  
    assert result == None  


def test_get_first_element_edge_cases():
    assert get_first_element([0]) == 0
    assert get_first_element([[1, 2], [3, 4]]) == [1, 2]

def test_divide_numbers_normal():
    assert divide_numbers(10, 2) == 5
    assert divide_numbers(9, 3) == 3


def test_divide_numbers_precision():
    result = divide_numbers(1, 3)
    assert result < 0.34
    assert result > 0.32


def test_divide_numbers_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(5, 0)


def test_contains_keyword_normal():
    assert contains_keyword("hello world", "world") is True
    assert contains_keyword("python pytest", "java") is False


def test_contains_keyword_case_sensitive():
    assert contains_keyword("Hello", "hello") is False 


def test_contains_keyword_edge_cases():
    assert contains_keyword("", "") is True
    assert contains_keyword(" ", " ") is True
    assert contains_keyword("something", "") is True


def test_contains_keyword_invalid_inputs():
    assert contains_keyword(None, "test") is None
    assert contains_keyword("hello", None) is None
    assert contains_keyword(123, "1") is None
