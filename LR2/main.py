"""Run a short demonstration of the calculator."""

from calculator import add, divide, multiply, power, subtract


def main():
    """Print results of the supported operations."""
    first, second = 10, 2
    print(f"{first} + {second} = {add(first, second)}")
    print(f"{first} - {second} = {subtract(first, second)}")
    print(f"{first} * {second} = {multiply(first, second)}")
    print(f"{first} / {second} = {divide(first, second)}")
    print(f"{first} ** {second} = {power(first, second)}")


if __name__ == "__main__":
    main()
