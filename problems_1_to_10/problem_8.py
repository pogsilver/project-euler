from collections import deque
from pathlib import Path


window_size = 13
this_dir = Path(__file__).resolve().parent
number_file = "problem_8.txt"

def fill_window(fl, size):
    """Read from fl (resuming at its current position) until `size`
        digits are queued, resetting on any 0 encountered along the way.
        Returns (queue, product), or (None, None) if EOF is hit first.

    Args:
        fl (file): the file from which we read the digits
        size (int): the max size of the the queue

    Returns:
        (deque, int): a tuple of the queue and multiple of the queue's items
    """
    q = deque(maxlen=size)
    product = 1
    while len(q) < size:
        char = fl.read(1)
        if not char:
            return None, None
        n = int(char)
        if n == 0:
            q.clear()
            product = 1
            continue
        q.appendleft(n)
        product *= n
    return q, product


with open(this_dir / number_file, 'r') as fl:
    q, curr_mult = fill_window(fl, window_size)
    if q is None:
        raise ValueError("not enough digits in file")
    
    max_mult = curr_mult

    while True:
        char = fl.read(1)
        if not char:
            break
        n = int(char)
        if n == 0:
            q, curr_mult = fill_window(fl, window_size)
            if q is None:
                break
            max_mult = max(max_mult, curr_mult)
        else:
            tail = q.pop()
            curr_mult = curr_mult // tail * n
            q.appendleft(n)
            max_mult = max(max_mult, curr_mult)

print(max_mult)


    

