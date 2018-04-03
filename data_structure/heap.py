# A Python program to demonstrate common binary heap operations
 
# Import the heap functions from python library
from heapq import heappush, heappop, heapify 
 
# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining
#             heap invarient
# heapify - transform list into heap, in place, in linear time

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) / 2

    def insertKey(self, k):
        heappush(self.heap, k)

    def extractMin(self):
        return heappop(self.heap)
