adj_list = [[3],[6,10],[7,11],[0,6,8],[13],[14],
[1,3,8,10,11],[2,11],[3,6,10,12],[13],[1,6,8],[2,6,7],[8],[4,9],[5]]
N = len(adj_list)
CCList= []
visited = [None] * N

def dfs(v):
    visited[v] = True
    cc.append(v)
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)

for i in range(N):
    if not visited[i]:
        cc =[]
        dfs(i);
        CCList.append(cc);

print('연결성분 리스트:');
print(CCList)