#!/usr/bin/python3

a = 10
b = 5

if __name__ == "__main__":
    """Print the sum, difference, product, and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    add_result = add(a, b)
    sub_result = sub(a, b)
    mul_result = mul(a, b)
    div_result = div(a, b)

    print("{} + {} = {}".format(a, b, add_result))
    print("{} - {} = {}".format(a, b, sub_result))
    print("{} * {} = {}".format(a, b, mul_result))
    print("{} / {} = {}".format(a, b, div_result))
