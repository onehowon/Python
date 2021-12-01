def merge(a, b, low, mid, high):
    i = low
    j = mid+1
    for k in range(low, high+1):
        if i > mid:
            b[k] = a[j]
            j += 1
        elif j > high:
            b[k] = a[i]
            i += 1
        elif a[j] < a[i]:
            b[k] = a[j]
            j += 1
        else:
            b[k] = a[i]
            i += 1
    for k in range(low, high+1):
        a[k] = b[k]

def merge_sort(a, b, low, high):
    if high <= low:
        return
    mid = low + (high - low) // 2
    merge_sort(a, b, low, mid)
    merge_sort(a,b, mid+1, high)
    merge(a,b, low, mid, high)

a = [54,88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
b = [None] * len(a)
print('정렬 전:\t', end='')
print(a)
merge_sort(a,b,0,len(a)-1)
print('정렬 후:\t', end='')
print(a)