import primefac

n = 10_001
prime = 0
for counter, num in enumerate(primefac.primegen(), start = 1):
    if counter == n:
        prime = num
        break

print(prime)