calculator.py - Version 1

def add(a, b):
    """Additionne deux nombres"""
    return a + b

def multiply(a, b):
    """Multiplie deux nombres"""
    return a * b

def divide(a, b):
    """Divise a par b"""
    if b == 0:
        raise ValueError("Division par zéro")
    return a / b 
