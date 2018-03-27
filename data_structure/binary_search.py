def binary_search(array, target):
    if array is None or len(array) == 0: return False
    start,end=0,len(array)-1
    while start <= end:
        middle = start + (end - start) // 2
        if array[middle] == target: return True
        if target > array[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return False


array = [1, 2, 12, 20, 23, 45, 46, 48]
targets = [1, 3, 11, 13, 20, 24, 45, 47]

res = []
for target in targets:
    found = binary_search(array, target)
    res.append("binary search found {}".format(target)) if found else res.append("binary search did not find {}".format(target))
        

print("array: {}".format(array))
for obj in res:
    print(obj)
