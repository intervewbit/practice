matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

B = [row for row in matrix]
A = [row[i] for row in matrix for i in range(4)]

print(B)
print(A)