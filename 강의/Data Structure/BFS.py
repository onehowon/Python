adj_list = [[2,1],[3,0],[3,0],[9,8,2,1],[5],[7,6,4],[7,5],[6,5],[3],[3]]

N = len(adj_list)
visited = [None] * N

def bfs(i):
    queue = []
    visited[i] = True
    queue.append(i)
    while len(queue) != 0:
        v = queue.pop(0)
        print(v, ' ', end='')
        for w in adj_list[v]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)

print('BFS 방문 순서:')
for i in range(N):
    if not visited[i]:
        bfs(i)