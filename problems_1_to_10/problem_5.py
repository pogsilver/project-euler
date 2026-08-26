import math


def lcm(a,b):
    """Calculates the lcm of a and b

    Args:
        a (int): an integer
        b (int): an integer
    Returns:
        int: the lowest common multiple of a and b
    """
    return (a * b) // math.gcd(a,b)

n = 20
curr_lcm = 1

for i in range(2, n + 1):
    curr_lcm = lcm(i, curr_lcm)

print(curr_lcm)