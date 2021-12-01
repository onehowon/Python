def shell_sort(a):
    h = 4
    while h >= 1:
        for i in range(h, len(a)): # h- 정렬 수행
            j = i
            while j >= h and a[j] < a[j-h]:
                a[j], a[j-h] = a[j-h], a[j]
                j -= h
            h //= 3
a = [54,88,77,26,93,17, 49, 10, 17, 77, 11, 31, 22 ,44 ,17, 20]
print('정렬 전:\t', end='')
print(a)
shell_sort(a)
print('정렬 후:\t', end='')
print(a)