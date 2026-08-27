from math import factorial

n = 100
# Pythonic approach:
print(sum(int(digit) for digit in str(factorial(n))))
# A bit cleverer and faster approach, since multiplying by 10 doesn't change the digits sum:

mult = 1
for i in range(1, 100):
    if i % 10 == 0:
        mult *= (i // 10)
    else:
        mult *= i


print(sum(int(digit) for digit in str(mult)))
