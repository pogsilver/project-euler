

min_len = 1_000
a, b= 0, 1
n = 1
while True:
    # in the nth iteration, b is the nth Fibonacci number 
    a,b = b, a + b
    n += 1
    if len(str(b)) >= min_len:
        print(n)
        break