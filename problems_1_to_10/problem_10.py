from primefac import primegen

s = 0
upper_limit = 2_000_000

for p in primegen():
    if upper_limit < p:
        break
    s += p

print(s)