
def selectionsort(arr):
    if arr is None or len(arr) == 0:
        return arr

    # the number of comparisons is O(n ^ 2)
    # the number of exchange is O(n)
    for i in range(len(arr)):
        max_i = i
        for j in range(i + 1, len(arr)):
            if arr[max_i] > arr[j]:
                max_i = j
        arr[max_i], arr[i] = arr[i], arr[max_i]

    return arr

print(selectionsort([3,6,8,10,1,2,1]))
