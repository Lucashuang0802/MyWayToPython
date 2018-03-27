def bubblesort(arr):
    if arr is None or len(arr) == 0:
        return arr


    # the number of comparisons is O(n ^ 2)
    # the number of exchange is O(n ^ 2)
    count = 1
    while count < len(arr):
        for j in range(len(arr) - 1, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
        count += 1
    return arr

print(bubblesort([3,6,8,10,1,2,1]))