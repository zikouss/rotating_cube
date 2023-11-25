def matrix_product(A, B):
    n = len(A)
    r = len(B)
    m = len(B[0])
    mat = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(r):
                mat[i][j] += A[i][k] * B[k][j]
    return mat
