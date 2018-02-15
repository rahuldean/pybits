"""
Check if the value is even, without using *, / or %
"""

def is_even(val):
    if not val:
        return True
    
    if val < 2:
        return False

    # val - 1 has all bits except msb to be 1
    # if val is even, msb = 1 and all are 0
    # if val is even val & val-1 is 0

    return not val & (val-1)
    