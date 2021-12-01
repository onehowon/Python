def downheap(i, size):
    while 2*i <= size:
        k = 2*i
        if k < size and a[k] < a[k+1]:
            k+=1
            if a[i] >= a[k]:
                break
            a[i], a[k] = a[k], a[i]
            i = k

def create_heap(a):
    hsize = len(a) - 1
    for i in reversed(range(1, hsize//2+1)):
        downheap(i, hsize)

def heap_sort(a):
    N = len(a) - 1
    for i in range(N):
        a[1], a[N] = a[N], a[1]
        downheap(1, N-1)
        N -= 1
        
a = [-1,54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
print('정렬 전:\t', end='')
print(a)
create_heap(a)
print('최대힙:\t', end='')
print(a)
heap_sort(a)
print('정렬 후:\t', end='')
print(a)