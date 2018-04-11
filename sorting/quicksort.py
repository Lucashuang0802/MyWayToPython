
class QuickSort:
    def __init__(self, data):
        self.data = data

    def perform(self):
        self.quicksort(self.data, 0, len(self.data) - 1)

    def quicksort(self, arr, left, right):
        index = self.partition(arr, left, right)
        if (left < index - 1):
            self.quicksort(arr, left, index - 1)
        if (index < right):
            self.quicksort(arr, index, right)

    def partition(self, arr, left, right):
        pivot = arr[(left + right) // 2]

        while left <= right:
            while arr[left] < pivot:
                left += 1
            while pivot < arr[right]:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return left

quicksort = QuickSort([45,7,10,101,100,8,12,23])
print(quicksort.data)
quicksort.perform()
print(quicksort.data)
