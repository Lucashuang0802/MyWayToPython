
def insertionsort(arr):
    if arr is None or len(arr) == 0:
        return arr

    # the number of comparisons is O(n ^ 2)
    # the number of exchange is O(n ^ 2)
    for i in range(0, len(arr)):
        value = arr[i]
        insert_position = i

        # find the insertion point
        while insert_position > 0 and arr[insert_position - 1] > value:
            arr[insert_position] = arr[insert_position - 1]
            insert_position -= 1

        # insert to the designated point
        arr[insert_position] = value

    return arr

print(insertionsort([3,6,8,10,1,2,1]))
