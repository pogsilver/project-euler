import primefac

def num_of_divisors(n):
    """calculates the number of divisors of a given integer n

    Args:
        n (int): The integer we want to calculate its number of divisors

    Returns:
        int: number of divisors of n
    """
    dic = {}
    for p in primefac.primefac(n):
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1

    d = 1
    for val in dic.values():
        d *= (val + 1)

    return d


# In this solution we use the fact that the divisors function is multiplicative
# and triangular numbers are of the form n * (n +1) / 2

min_divisors = 500

dic = {}
n = 1
divisors = 1
while True:
    if n % 2 == 0:
        if n + 1 not in dic:
            dic[n + 1] = num_of_divisors(n + 1)
        if n // 2 not in dic:
            dic[n // 2] = num_of_divisors(n // 2)
        divisors = dic[n + 1] * dic[n // 2]
        if min_divisors <= divisors:
            break
    else:
        if n not in dic:
            dic[n] = num_of_divisors(n)
        if (n + 1) // 2 not in dic:
            dic[(n + 1) // 2] = num_of_divisors((n + 1) // 2)
        divisors = dic[(n + 1)// 2] * dic[n]
        if min_divisors <= divisors:
            break
    n += 1

triangular = n * (n + 1) // 2

print(triangular)

