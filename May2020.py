import numpy as np

N = 900

prev_array = np.arange(2,N+2)
print(prev_array)

for k in range(1,N):
    next_array = np.arange(k+2,N+2+k)

    for i in range(2*N):
        row_idx = np.floor(i/2)+1
        if (i%2 == 0):
            if k-row_idx >= 0:
                next_array[i] = prev_array[int(k-row_idx)]
            else:
                next_array[i] = prev_array[int(k+row_idx)]
                break
        else:
            next_array[i] = prev_array[int(k+row_idx)]

    if next_array[k+1] == 11:
        print('11 expelled in row ', k+2)
        break
    print('expelled in row ', k+2, ':', next_array[k+1])
    prev_array = next_array
    print(prev_array)