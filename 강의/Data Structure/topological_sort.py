adj_list = [[1],[3,4],[0,1],[6],[5],[7],[7],[8],[]]
N = len(adj_list)
visited = [None] * N
s = []

def dfs(v):
    visited[v] = True
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)
    s.append(v)

for i in range(N):
    if not visited[i]:
        dfs(i)
s.reverse()
print('위상정렬:')
print(s)