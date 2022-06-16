def calculate_sum(str_nums):
    """
    Calculates and returns the sum of all numbers in the input
    :param str_nums: a string consisting of comma separated numbers e.g, "10, 20, 30"
    :return: total value of the numbers in the input string
    """
    def value_of(n):
        try:
            return float(n)
        except ValueError:
            return 0

    nums = [value_of(n) for n in str_nums.split(',')]
    return sum(nums)


def factorial(num):
    """
    This is a function to calculate the factorial of an input number
    :param num: non-negative number for which we are generating the factorial
    :return: factorial of the input
    :raises: ValueError if the input number is negative
    :raises: TypeError if the input is not a number
    """

    if type(num) is not int:
        raise TypeError(f'Expected int, but got {type(num)}')

    if num < 0:
        raise ValueError('Cannot calculate factorial of negative input')

    f = 1
    while num > 1:
        f *= num
        num -= 1

    return f

