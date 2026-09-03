upper_limit = 1_000
max_period = -1
max_d = -1

for d in range(2, upper_limit + 1):
    r = 1
    # Ensure r will have a repeating period
    for _ in range(d):
        r = (10 * r) % d

    d_0 = r
    period_len = 0
    while True:
        r = (10 * r) % d
        period_len += 1
        if r == d_0:
            break
    if max_period < period_len:
        max_d = d
        max_period = period_len
print(max_d)