
def merge(left, right):
    i = 0
    j = 0

    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1

    return res

def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[mid:]
    right = arr[:mid]

    return merge(mergesort(left), mergesort(right))

print(mergesort([3,6,8,10,1,2,1]))
