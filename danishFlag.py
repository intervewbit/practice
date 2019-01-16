
def threeWayQuickSort(arr, start, end):

    if start >= end:
        return
    elif end-start == 1:
        if arr[end] < arr[start]:
            arr[end], arr[start] = arr[start], arr[end]
        return

    key = arr[end]
    left = start - 1
    eq = 1  # which is the end element
    for i in range(start, end):
        if arr[i] < key:
            left = left+1
            arr[left], arr[i] = arr[i], arr[left]
        elif arr[i] == key:
            eq = eq+1

    # add the eq elements
    target = end
    for i in range(left+1, left+1+eq):
        arr[target] = arr[i]
        target = target-1
        arr[i] = key

    threeWayQuickSort(arr, start, left)
    threeWayQuickSort(arr, left+eq+1, end)


def danish(arr):
    threeWayQuickSort(arr, 0, len(arr)-1)


arr = [28, 34, 12, 6, 5, 9, 2, 6, 11, 90, 6, 17, 6, 5, 27]
#arr = [2, 7, 1, 0, 88]
danish(arr)
print(arr)
