from pathlib import Path

this_dir = Path(__file__).resolve().parent
file_path = "problem_18.txt"
pyramid = []

with open(this_dir / file_path, 'r') as fl:
    for line in fl:
        if line.strip():
            row = [int(num) for num in line.split()]
            pyramid.append(row)

n = len(pyramid)
for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        pyramid[i][j] += max(pyramid[i + 1][j], pyramid[i + 1][j + 1])

print(pyramid[0][0])