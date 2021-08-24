from exceptional import convert

# convert("one three three seven".split())
#
# DIGIT_MAP = {
#     'zero': '0',
#     'one': '1',
#     'two': '2',
#     'three': '3',
#     'four': '4',
#     'five': '5',
#     'six': '6',
#     'seven': '7',
#     'eight': '8',
#     'nine': '9',
# }
#
#
# def convert(s):
#     try:
#         number = ''
#         for token in s:
#             number += DIGIT_MAP[token]
#         x = int(number)
#         print(f"Conversion succeeded! x = {x}")
#     except KeyError:
#         print("Conversion failed")
#         x = -1
#     return x
#
#
# print(convert("three four".split())


def sqrt(x):
    """Complete square roots using the method
    of Heron of Alexandria.

    Args:
        x: The number for which the square root is to be computed.

    Returns:
        The square root of x.

    Raises:
          ValueError: If x is negative.
    """

    if x < 0:
        raise ValueError(
            "Cannot compute square root of "
            f"negative number {x}")
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
    return guess


chocolate = sqrt(1)
print(chocolate)
