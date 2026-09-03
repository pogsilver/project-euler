
def sum_digits(n, power):
    """Finds the sum of the number digits to the given power
       For example, given n = 1634, power = 4 returns 
       1 ** 4 + 6 ** 4 + 3 ** 4 +  ** 4
    Args:
        n (int): a number
        power (int): the power to which the digits are raised

    Returns:
        int: The sum of the given number's digits raised to the given power
    """

    digits = [int(c) for c in str(n)]

    return sum([i ** power for i in digits])


def upper_lim(power):
    """Finds the upper limit of numbers which equal the 
    sum of their digits raised to the given power

    Args:
        power (int): The power to which the digits are raised

    Returns:
        int: The upper limit of numbers which equal the 
    sum of their digits raised to the given power
    """
    n = 1
    while 10 ** n - 1 <= n * (9 ** power):
        n += 1
    return 10 ** n

power = 5
upper_limit = upper_lim(power) 

s = 0
for n in range(2, upper_limit + 1):
    if n == sum_digits(n, power):
        s += n

print(s)