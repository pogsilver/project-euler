
n = 1001
s = 0
for side in range(n, 1, -2):
    top_right = side ** 2
    for i in range(4):
        s += top_right - i * (side - 1)


print(s + 1)