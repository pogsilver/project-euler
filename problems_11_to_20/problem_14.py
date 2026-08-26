

upper_limit = 1_000_000

dic = {1:1}
max_length = 1
best_start = 1

for i in range(1, upper_limit):
    n = i
    path = []

    # Go through the Collatz sequence
    while n not in dic:
        path.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    curr_len = dic[n]

    # Backtrack the path
    while path:
        num = path.pop()
        curr_len += 1
        dic[num] = curr_len

    if max_length < dic[i]:
        max_length = dic[i]
        best_start = i

print(best_start)
