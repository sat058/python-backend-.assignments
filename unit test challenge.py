def perimeter(length, breadth):
    if not length or not breadth:
        raise ValueError("Undefined")
    
    if not isinstance(length, (int, float)):
        raise ValueError("Not a number")
    
    if not isinstance(breadth, (int, float)):
        raise ValueError("Not a number")
    
    if length < 0 or breadth < 0:
        raise ValueError("Dimension cannot be negative")
    
    return 2 * (length + breadth)
import pytest
from your_module import perimeter  # Replace 'your_module' with the actual module name

def test_valid_perimeter():
    assert perimeter(5, 10) == 30  # Valid inputs

def test_missing_length():
    with pytest.raises(ValueError, match="Undefined"):
        perimeter(None, 10)

def test_missing_breadth():
    with pytest.raises(ValueError, match="Undefined"):
        perimeter(5, None)

def test_length_not_number():
    with pytest.raises(ValueError, match="Not a number"):
        perimeter("five", 10)

def test_breadth_not_number():
    with pytest.raises(ValueError, match="Not a number"):
        perimeter(5, "ten")

def test_negative_length():
    with pytest.raises(ValueError, match="Dimension cannot be negative"):
        perimeter(-5, 10)

def test_negative_breadth():
    with pytest.raises(ValueError, match="Dimension cannot be negative"):
        perimeter(5, -10)
