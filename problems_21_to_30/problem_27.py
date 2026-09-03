from primefac import primegen, isprime

upper_limit = 1_000


b_s = [p for p in primegen(upper_limit)]


max_n = 0
max_a = 0
max_b = 0
for b in b_s:
    # 2 <= 1 + a + b <=> -b + 1 <= a
    a_lower_bound = -b + 1

    if b % 2 == 1:
        a_lower_bound += 1
        step = 2
    else:
        step = 1
    for a in range(a_lower_bound, upper_limit, step):
        n = 0
        while isprime(n ** 2 + a * n + b):
            n += 1

        if max_n < n:
            max_n = n
            max_a = a
            max_b = b

print(f"a: {max_a}, b: {max_b}, ab = {max_a * max_b}")
    