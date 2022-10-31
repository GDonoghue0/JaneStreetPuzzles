from itertools import product
from numpy import prod
import numpy as np
import random

def get_pdf(C, level):
    if level < N:
        for k in range(N):
            C[level] = k+1
            get_pdf(C, level+1)
            if level == N-1:
                temp = ''.join(str(e) for e in sorted(C))
                if temp in T:
                    T[temp] += 1
                else:
                    T[temp] = 1
    return T

def convert_sample(sample):
    result = [0]*N
    for i in range (N):
        result[i] = [item for item in sample[i*N:(i+1)*N]]
        result[i] = ''.join(str(e) for e in result[i])
    return result

def is_valid(arr):
    count = 0
    result = [False]*N
    counts = np.zeros([N,N])
    for i in range(N):
        for j in range(N):
            counts[i][j] = arr[i].count(str(j+1))
    print(arr)
    print(counts)

    # maxs = np.amax(counts, axis=0)
    for i in range(N): # for each child
        for j in range(N): # for each candy
            print(counts[i][j], 'i = ', i, 'j = ', j)
            result[i] = ([counts[i][j] > counts[k%N][j] for k in range(i+1, i + N)])
            if any(result[i]):
                break
            # for k in range(i+1, i + N):

            #     if counts[i][j] < counts[k%N][j]:
            #         result[i] = False
            #         print(result)
            #         break


        # result[i] = np.argwhere(counts[:,i] == np.amax(counts[:,i]))
    print(result)
    # valid = True#not any(result)
    return any(result)


def result_via_loops_3(T, N):
    prob_valid = 0
    prob_invalid = 0
    for i1 in T:
        for i2 in T:
            for i3 in T:
                    if (i1+i2+i3).count('1') == N and (i1+i2+i3).count('2') == N and (i1+i2+i3).count('3') == N:
                        if is_valid([i1, i2, i3]):
                            print(i1, i2, i3, ":", T[i1], T[i2], T[i3])
                            prob_valid += T[i1] * T[i2] * T[i3]
                        else:
                            prob_invalid += T[i1] * T[i2] * T[i3]

    # print(prob_valid/(prob_valid + prob_invalid), prob_valid, prob_valid + prob_invalid)
    # print(0.2928334)
    return prob_valid/(prob_valid + prob_invalid)

def result_via_loops_4(T, N):
    prob_valid = 0
    prob_invalid = 0
    for i1 in T:
        for i2 in T:
            for i3 in T:
                for i4 in T:
                    if (i1+i2+i3+i4).count('1') == N and (i1+i2+i3+i4).count('2') == N and (i1+i2+i3+i4).count('3') == N and (i1+i2+i3+i4).count('4') == N:
                        if is_valid([i1, i2, i3, i4]):
                            print(i1, i2, i3, i4, ":", T[i1], T[i2], T[i3], T[i4])
                            prob_valid += T[i1] * T[i2] * T[i3] * T[i4]
                        else:
                            prob_invalid += T[i1] * T[i2] * T[i3] * T[i4]

    # print(prob_valid/(prob_valid + prob_invalid), prob_valid, prob_valid + prob_invalid)
    return prob_valid/(prob_valid + prob_invalid)


def monte_carlo(num_samples):
    total_valid = 0
    arr = []
    for i in range(N):
        for j in range(N):
            arr.append(i+1)
    for i in range(num_samples):
        sample = random.sample(arr, len(arr))
        valid = int(is_valid(convert_sample(sample)))
        print(sample, valid)
        total_valid += valid

    print('total_valid/num_samples = ', total_valid/num_samples)
    return total_valid/num_samples



N = 3
C = [1]*N
T = {}
T = get_pdf(C, 0)

num_samples = 1000000


y = list(T.keys())
z = [product(y, repeat=N)]
count_valid = 0
count_invalid = 0
prob_valid = 0
prob_invalid = 0
for i in product(y, repeat=N):
    j = ' '.join(i)
    if j.count('1') == N and j.count('2') == N and j.count('3') == N and j.count('3') == N :
        prob_list = [T[e] for e in j.split(' ')]
        if is_valid(list(i)):
            print(j, ':', prob_list)
            prob_valid += prod(prob_list)
            count_valid += 1
        else:
            count_invalid += 1
            prob_invalid += prod(prob_list)


print(count_valid, count_invalid, count_valid + count_invalid)

# print(monte_carlo(num_samples))
print(prob_valid/(prob_valid + prob_invalid), prob_valid, prob_valid + prob_invalid)


N = 5
test = ['11223', '13333', '24444', '12455', '12555']
print(test)
print(is_valid(test))


# There are only 126 ways for each child to pick 5 pieces of candy
# Therefore, we can naively check 126**5 = 31,757,969,376 combinations

# For N = 3 10 million samples gives a fraction of 0.2928334 \approx 41/140



