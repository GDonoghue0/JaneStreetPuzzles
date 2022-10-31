import numpy as np

A = np.zeros([10,10])
combos = {}
for i in range(1,10):
    for j in range(i,10):
        gcd = np.gcd(i,j)
        A[i][j] = gcd
        if gcd != 1 and gcd < 5:
            combos.setdefault(str(gcd), []).append([i,j])

print(A)
print(combos)

count = 0
possible_diviors = []
possible_quotients = []
possible_dividends = []
for i1 in [3,6,9]:
    for i2 in range(10):
        for i3 in [2,4,6,8]:
            for i4 in [2,4,6,8]:
                for i5 in [4,8]:
                    for i6 in range(10):
                        for i7 in [2,4,6,8]:
                            divisor = i1*1000 + i2*100 + i3*10 + i4
                            quotient = i5*100 + i6*10 + i7
                            dividend = divisor * quotient
                            print(divisor, quotient, dividend, dividend//100000 % 10, dividend//10%10, dividend//10%10 == 2 or dividend//10%10 == 4 or dividend//10%10 == 6 or dividend//10%10 == 8, dividend%10, dividend%10 == 3 or dividend%10 == 6 or dividend%10 == 9)
                            if (dividend//100000%10) == 7:
                                # and (dividend%10 == 3 or dividend%10 == 6 or dividend%10 == 9) and
                                # (dividend//10%10 == 2 or dividend//10%10 == 4 or dividend//10%10 == 6 or dividend//10%10 == 8)):
                                # print(divisor, dividend)
                                possible_diviors.append(divisor)
                                possible_quotients.append(quotient)
                                possible_dividends.append(dividend)
                                count += 1

print(possible_diviors)
print(possible_quotients)
print(possible_dividends)
print(count)