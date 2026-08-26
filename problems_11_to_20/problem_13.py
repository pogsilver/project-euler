from pathlib import Path

this_dir = Path(__file__).resolve().parent
file_path = "problem_13.txt"

su = 0
with open(this_dir / file_path, 'r') as fl:
    for line in fl:
        if line.strip():
            # Since the maximal carry of the first 39 digits in
            # summing 100 50 digits numbers is 100 * 10^39 = 10^41, and
            # the sum of the 100 50 digits number is at least 10^51 
            su += int(line.strip()[:12])

print(str(su)[:10])