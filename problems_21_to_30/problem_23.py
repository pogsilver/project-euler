upper_limit = 28_123

sum_div = [0] * (upper_limit + 1)

# Calculating the sum of divisors for each a in our range
for i in range(1, upper_limit// 2 + 1):
    for j in range(2 * i, upper_limit, i):
        sum_div[j] += i

abundant_numbers = []
for num, divisors_sum in enumerate(sum_div):
    if num < divisors_sum:
        abundant_numbers.append(num)

s = upper_limit * (upper_limit + 1) // 2 # Arithmetic sum of 1 to upper_limit
sum_of_abundants = set()
n = len(abundant_numbers)
for i in range(n):
    for j in range(i, n):
        num_sum = abundant_numbers[i] + abundant_numbers[j]
        if num_sum < upper_limit + 1:
            sum_of_abundants.add(num_sum)

print(s - sum(sum_of_abundants))