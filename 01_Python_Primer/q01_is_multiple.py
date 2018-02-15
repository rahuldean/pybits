"""
find if n is a multiple of m
"""

def is_multiple(n, m):
    if not m:
        return False
    
    return n % m == 0
