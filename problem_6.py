

def squares_sum(n):
    """calculates the sum of the squares of 1 to n

    Args:
        n (int): a natural number

    Returns:
        int: the sum of 1^2 + 2^2 + ... + n^2
    """
    return (n * (n+1) * (2 * n + 1)) // 6

def arithmetic_sum(n):
    """calculates the sum of the of 1 to n
    
        Args:
            n (int): a natural number
    
        Returns:
            int: the sum of 1 + 2 + ... + n
        """
    return (n * (n + 1)) // 2


n = 100
print(arithmetic_sum(n) ** 2 - squares_sum(n))