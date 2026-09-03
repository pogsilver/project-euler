
upper_limit = 10_000

sum_div = [0] * upper_limit

# Calculating d(a) for each a in our range
for i in range(1, upper_limit// 2 + 1):
    for j in range(2 * i, upper_limit, i):
        sum_div[j] += i

s = 0
for a in range(1, upper_limit):
    b = sum_div[a]
    if a < b < upper_limit and a == sum_div[b]:
        s += a + b

print(s)
