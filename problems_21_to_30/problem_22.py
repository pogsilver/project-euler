from pathlib import Path


def name_value(name):
    """Calculates the alphabetical value of the given
    name in "A" to "Z"

    Args:
        name (str): a string in capital alphabet

    Returns:
        int: the alphabetical value of the given name
    """
    A_ascii_val = 65
    s = 0
    for ch in name:
        s += (ord(ch) - A_ascii_val + 1)
    return s
names = []

this_dir = Path(__file__).resolve().parent
file_path = "problem_22.txt"

with open(this_dir / file_path, 'r') as fl:
    for line in fl:
        for name in line.strip().replace('"', "").split(","):
            names.append(name)  # noqa: PERF402


names = sorted(names)

s = 0

for i, name in enumerate(names):
    s += (i + 1) * name_value(name)

print(s)