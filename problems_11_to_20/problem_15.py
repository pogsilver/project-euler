from math import comb

# This solution relies on the fact that given a n by n grid, where we must go right or down,
# The number of paths is equivalent to the number of times we choose to go right n times out of 2n
# options. Thus, the solution is 2n choose n.

n = 20
print(comb(2 * n, n))