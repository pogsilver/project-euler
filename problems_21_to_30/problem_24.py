
factorials = [1]
for i in range(1, 10):
    factorials.append(factorials[-1] * i)
options = [i for i in range(10)]
total = 1_000_000 - 1
perm = ""
for i in range(10):
    q = total // factorials[9-i]
    perm += str(options[q])
    options.remove(options[q])
    total = total - q * factorials[9-i]
print(perm)