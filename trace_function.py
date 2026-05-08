def trace(matrix):
    """
    Takes a square matrix and returns its trace
    """
    tr = 0
    for i in range(len(matrix)):
        tr += matrix[i][i]
    return tr

# number of columns
n_cols = 25

# create a square matrix
matrix = [[i*j for j in range(n_cols)] for i in range(n_cols)]

# print the trace
print('Trace:', trace(matrix))