def lsd_sort(a):
    WIDTH = 3
    N = len(a)
    R = 128
    temp = [None] * N
    for d in reversed(range(WIDTH)):
        count = [0] * (R+1)
        for i in range(N):
            count[ord(a[i][d])+1] += 1
        for j in range(1, R):
            count[j] += count[j-1]
        for i in range(N):
            p = ord(a[i][d])
            temp[count[p]] = a[i]
            count[p] += 1
        for i in range(N):
            a[i] = temp[i]
        print("%d번째 문자:\t" % d, end='')
        for x in a: print(x, ' ', end='')
        print()
a = ['ICN', 'SFO', 'LAX', 'FRA', 'SIN', 'ROM', 'HKG', 'TLV',
'SYD', 'MEX', 'LHR', 'NRT', 'JFK', 'PEK', 'BER', 'MOW']
print('정렬 전:\t', end='')
for x in a: print(x, ' ', end='')
print()
lsd_sort(a)