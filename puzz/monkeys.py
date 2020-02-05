import functools

def simul():
    A = [1] * 100
    for i in range(2, 100, 2):
        A[i] = 0

    for i in range(3, 100):
        for j in range(i, 100, i):
            if A[j] == 1:
                A[j] = 0
            else:
                A[j] = 1

    print(A.count(1))


simul()
