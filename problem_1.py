


max_num = 1000
total_sum = 0

for num in range(1, max_num):
    if num % 3 == 0 or num % 5 == 0:
        total_sum += num

print(total_sum)

