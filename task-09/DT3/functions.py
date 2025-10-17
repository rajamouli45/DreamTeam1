def add_numbers(a, b):
    return a + b


def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


def get_first_element(lst):
    if not lst:
        return None
    return lst[0]


def divide_numbers(a, b):
    return a / b


def contains_keyword(text, keyword):
    if not isinstance(text, str) or not isinstance(keyword, str):
        return None
    return keyword in text
