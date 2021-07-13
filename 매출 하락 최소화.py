import math

Children = [[] for _ in range(300000)]
Cost = [[0,0] for _ in range(300000)]

def traversal(sales, node):
    Cost[node][0] = 0
    Cost[node][1] = sales[node]

    if not Children[node]:
        return

    extraCost = math.inf
    for child in Children[node]:
        traversal(sales, child)
        if Cost[child][0] < Cost[child][1]:
            Cost[node][0] += Cost[child][0]
            Cost[node][1] += Cost[child][0]
            extraCost = min(extraCost, Cost[child][1] - Cost[child][0])
        else:
            Cost[node][0] += Cost[child][1]
            Cost[node][1] += Cost[child][1]
            extraCost = 0
    Cost[node][0] += extraCost


def solution(sales, links):
    for link in links:
        Children[link[0]-1].append(link[1]-1)

    traversal(sales, 0)
    return min(cost[0][0], Cost[0][1])