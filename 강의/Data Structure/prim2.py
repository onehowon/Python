import sys
N = 8
s = 0
g = [None] * N
g[0] = [(1,1), (3,2)]
g[1] = [(0,1), (2,4), (3,3), (4,1), (5,6)]
g[2] = [(1,4), (5,1), (6,1), (7,2)]
g[3] = [(0,2), (1,3), (4,5)]
g[4] = [(1,1), (3,5), (6,2)]
g[5] = [(2,1), (4,2), (7,1)]
g[6] = [(2,2), (5,9),(6,1)]

visited = [False] * N
D = [sys.maxsize] * N
D[s] = 0
previous = [None] * N
previous[s] = s

for k in range(N):
    m = -1
    min_value = sys.maxsize
    for j in range(N):
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j
    visited[m] = True
    for v, wt in list(g[m]):
        if not visited[v]:
            if D[m]+wt < D[v]:
                D[v] = D[m] + wt
                previous[v] = m

print('정점', s, '(으)로부터 최단거리:')
for i in range(N):
    if D[i] == sys.maxsize:
        print(s,'와(과)', i, ' 사이에 경로 없음.')
    else:
        print('[%d, %d]'%(s,i), '=', D[i])

print('\n정점', s, '(으)로부터의 최단 경로')
for i in range(N):
    back = i
    print(back, end='')
    while back != s:
        print(' <-', previous[back], end='')
        back = previous[back]
    print()