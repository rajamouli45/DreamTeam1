import pytest
import math
from schoolBounty import (
    calculate_gpa,
    assign_scholarship,
    normalize_scores,
    find_top_student,
    safe_divide
)
def test_calculate_gpa_normal():
    assert calculate_gpa([90, 95, 85]) == 4.0
    assert calculate_gpa([80, 85, 82]) == 3.5
    assert calculate_gpa([70, 75, 72]) == 3.0
    assert calculate_gpa([60, 65]) == 2.5
    assert calculate_gpa([50, 52]) == 2.0
    assert calculate_gpa([30, 40]) == 1.0
def test_calculate_gpa_boundary():
    assert calculate_gpa([90]) == 4.0
    assert calculate_gpa([80]) == 3.5
    assert calculate_gpa([70]) == 3.0
    assert calculate_gpa([60]) == 2.5
    assert calculate_gpa([50]) == 2.0
    assert calculate_gpa([49.9]) == 1.0
def test_calculate_gpa_empty():
    assert calculate_gpa([]) == 0
def test_assign_scholarship_eligible():
    assert assign_scholarship(3.5, 70) is True
    assert assign_scholarship(4.0, 80) is True
def test_assign_scholarship_ineligible():
    assert assign_scholarship(3.4, 75) is False
    assert assign_scholarship(3.6, 65) is False
    assert assign_scholarship(3.0, 60) is False
def test_normalize_scores_normal():
    assert normalize_scores([50, 100]) == [0.5, 1.0]
def test_normalize_scores_zero_max():
    assert normalize_scores([0, 0, 0]) == [0, 0, 0]
def test_normalize_scores_single_value():
    assert normalize_scores([80]) == [1.0]
def test_find_top_student_normal():
    students = [("Alice", 88), ("Bob", 95), ("Charlie", 80)]
    assert find_top_student(students) == "Bob"
def test_find_top_student_tie():
    students = [("Anna", 90), ("Ben", 90)]
    assert find_top_student(students) in ["Anna", "Ben"]
def test_find_top_student_single():
    assert find_top_student([("Solo", 100)]) == "Solo"
def test_safe_divide_normal():
    assert safe_divide(10, 3) == math.ceil(10 / 3)
    assert safe_divide(5, 5) == 1
def test_safe_divide_divide_by_one():
    assert safe_divide(7, 1) == 7
def test_safe_divide_zero_numerator():
    assert safe_divide(0, 5) == 0
def test_safe_divide_zero_denominator():
    with pytest.raises(ValueError):
        safe_divide(5, 0)
