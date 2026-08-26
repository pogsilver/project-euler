

max_num = 4_000_000
total_sum = 0

a, b= 0, 1
while (b < max_num):
    # in the nth iteration, b is the nth Fibonacci number 
    a,b = b, a + b 
    if b % 2 == 0:
        total_sum += b

print(total_sum)