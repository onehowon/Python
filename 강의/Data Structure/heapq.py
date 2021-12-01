import heapq
a = [54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
print('정렬전:\t', a)

heapq.heapify(a)
print('힙:\t', a)

s = []
while a:
    s.append(heapq.heappop(a))

print('정렬후:\t', s)