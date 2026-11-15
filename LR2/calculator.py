"""Basic arithmetic operations."""


def add(first, second):
    """Return the sum of two numbers."""
    return first + second


def subtract(first, second):
    """Return the difference between two numbers."""
    return first - second


def multiply(first, second):
    """Return the product of two numbers."""
    return first * second


def divide(first, second):
    """Return the quotient of two numbers.

    Python raises ZeroDivisionError when ``second`` is zero.
    """
    return first / second


def power(base, exponent):
    """Return ``base`` raised to ``exponent``.

    Raising zero to a negative power is undefined, so a clear standard
    arithmetic exception is raised instead of relying on implementation detail.
    """
    if base == 0 and exponent < 0:
        raise ZeroDivisionError("0 cannot be raised to a negative power")
    return base ** exponent
