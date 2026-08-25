

def is_palindrome(n):
    return str(n) == str(n)[::-1]



range_min = 99
range_max = 999
max_pal = -1

for i in range(range_max, range_min, -1):
    for j in range(range_max, i, -1):
        curr = i * j
        if curr < max_pal:
            break
        if is_palindrome(curr):
            max_pal = curr

print(max_pal)