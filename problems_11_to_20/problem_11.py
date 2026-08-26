from pathlib import Path



def max_row_multiple(mat, window_size):
    """calculates the max multiple of the given window size adjacent elements in the same row
    in a square matrix. 

    Args:
        mat (ls): a list of lists that represents a square matrix
        window_size (int): the number of adjacent elements in the multiple

    Returns:
        int: The max multiple of window_size adjacent numbers in the same row in the matrix 
    """
    n = len(mat)
    max_mult = -1

    for i in range(n):
        for j in range(n - window_size + 1):
            curr_mult = 1
            for k in range(window_size):
                curr_mult *= mat[i][j + k]
            max_mult = max(max_mult, curr_mult)
    return max_mult



def max_column_multiple(mat, window_size):
    """calculates the max multiple of the given window size adjacent elements in the same
    column in a square matrix. 

    Args:
        mat (ls): a list of lists that represents a square matrix
        window_size (int): the number of adjacent elements in the multiple

    Returns:
        int: The max multiple of window_size adjacent numbers in the same column in the matrix 
    """
    n = len(mat)
    max_mult = -1

    for j in range(n):
        for i in range(n - window_size + 1):
            curr_mult = 1
            for k in range(window_size):
                curr_mult *= mat[i + k][j]
            max_mult = max(max_mult, curr_mult)
    return max_mult


def max_up_diag_multiple(mat, window_size):
    """calculates the max multiple of the given window size adjacent elements in the same
    upward diagonal in a square matrix. 

    Args:
        mat (ls): a list of lists that represents a square matrix
        window_size (int): the number of adjacent elements in the multiple

    Returns:
        int: The max multiple of window_size adjacent numbers in the same upward diagonal in the matrix 
    """
    n = len(mat)
    max_mult = -1

    for i in range(window_size - 1, n):
        for j in range(n - window_size + 1):
            curr_mult = 1
            for k in range(window_size):
                curr_mult *= mat[i - k][j + k]
                max_mult = max(max_mult, curr_mult)

    return max_mult


def max_down_diag_multiple(mat, window_size):
    """calculates the max multiple of the given window size adjacent elements in the same
    downward diagonal in a square matrix. 

    Args:
        mat (ls): a list of lists that represents a square matrix
        window_size (int): the number of adjacent elements in the multiple

    Returns:
        int: The max multiple of window_size adjacent numbers in the same downward diagonal in the matrix 
    """
    n = len(mat)
    max_mult = -1

    for i in range(n -window_size + 1):
        for j in range(n - window_size + 1):
            curr_mult = 1
            for k in range(window_size):
                curr_mult *= mat[i + k][j + k]
            max_mult = max(max_mult, curr_mult)

    return max_mult



n = 20
num_of_digits = 2
window = 4
this_dir = Path(__file__).resolve().parent
file_path = "problem_11.txt"
grid = []

with open(this_dir / file_path, 'r') as fl:
    for line in fl:
        if line.strip():
            row = [int(num) for num in line.split()]
            grid.append(row)

max_c = max_column_multiple(grid, window)
max_r = max_row_multiple(grid, window)
max_du = max_up_diag_multiple(grid, window)
max_dd = max_down_diag_multiple(grid, window)
print(max(max_c, max_r, max_du, max_dd))