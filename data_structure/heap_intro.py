
from heapq import heappush, heappop, heapify 

data = [100, 12, 23, 7, 101, 8, 10, 45];
print(data)
print(heappop(data))   # 100
print(heappop(data))   # 12
print(heappop(data))   # 7
print(heappop(data))   # 8

heapify(data)
print(heappop(data))   # 7
print(heappop(data))   # 8
print(heappop(data))   # 10

heappush(data, 2)
heappush(data, 1)
heappush(data, 11)
heappush(data, 37)
print(data)
print(heappop(data))   # 1
print(heappop(data))   # 2
print(heappop(data))   # 11
print(heappop(data))   # 37
print(heappop(data))   # 101
