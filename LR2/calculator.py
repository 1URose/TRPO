"""Basic arithmetic operations."""


def add(first, second):
    """Return the sum of two numbers.

    Args:
        first: The first addend.
        second: The second addend.

    Returns:
        The value of ``first + second``.
    """
    return first + second


def subtract(first, second):
    """Return the difference between two numbers.

    Args:
        first: The number from which to subtract.
        second: The number to subtract.

    Returns:
        The value of ``first - second``.
    """
    return first - second


def multiply(first, second):
    """Return the product of two numbers.

    Args:
        first: The first factor.
        second: The second factor.

    Returns:
        The value of ``first * second``.
    """
    return first * second


def divide(first, second):
    """Return the quotient of two numbers.

    Args:
        first: The dividend.
        second: The divisor.

    Returns:
        The value of ``first / second``.

    Raises:
        ZeroDivisionError: If ``second`` is zero.
    """
    return first / second


def power(base, exponent):
    """Return a number raised to a specified power.

    Args:
        base: The number to raise to a power.
        exponent: The power to apply; it can be positive, zero, or negative.

    Returns:
        The value of ``base ** exponent``.

    Raises:
        ZeroDivisionError: If ``base`` is zero and ``exponent`` is negative.
    """
    if base == 0 and exponent < 0:
        raise ZeroDivisionError("0 cannot be raised to a negative power")
    return base ** exponent
