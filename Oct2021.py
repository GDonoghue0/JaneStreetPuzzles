import numpy as np
import random


N = 8
M = 10000
num_zeros = 0
num_nonzeros = 0
for j in range(M):
    mat = np.zeros([3*N, N])

    for i in range(3*N):
        mat[i][random.randint(0,N-1)] = 1

    totals = np.sum(mat,0)
    # print(mat)
    # print(totals)
    num_empty_races = np.count_nonzero(totals == 0)
    if num_empty_races == 0:
        num_zeros += 1
    else:
        num_nonzeros += 1

print('Success:', num_nonzeros/M)
print('Fail:', num_zeros/M)
print()
print((N-1)*((N-1)/N)**(3*N-1))