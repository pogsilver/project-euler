base = 2
power = 1_000
# Pythonic approach:
print(sum(int(digit) for digit in str(base ** power)))


#General solution:
def multi_nums_as_arrays(num1, num2):
    """multiplies two numbers written in reverse - the the ith significant
    digit is in the ith place of the list

    Args:
        num1 (ls): a list representing the first number
        num2 (ls): a list representing the seconde number

    Returns:
        ls: the result of num1 * num2 saved in reverse order or digits
    """
    n = len(num1)
    m = len(num2)
    result = [0] * (n + m)

    for i in range(n):
        carry = 0
        for j in range(m):
            temp = result[i + j] + num1[i] * num2[j] + carry
            result[i + j] = temp % 10
            carry = temp // 10

        if carry > 0:
            result[i + m] += carry
    # remove trailing zeroes
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result


def fast_exponentiation_sum(base, power):
    """calculates the sum of digits of base ** power

    Args:
        base (int): base of the power
        power (int): the exponent of the power
    
    Returns:
            int: the sum of digits of base ** power
    """
    result = [1]
    base_as_ls = [base]

    while power > 0:
        if power % 2 == 1:
            result = multi_nums_as_arrays(result, base_as_ls)

        base_as_ls = multi_nums_as_arrays(base_as_ls, base_as_ls)
        power //= 2

    return sum(result)


print(fast_exponentiation_sum(base, power))
