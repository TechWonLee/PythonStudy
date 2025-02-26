# 백준 1197 최소 스패닝 트리
#코드를 외워라

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
edge = [[] for _ in range(V+1)]
chk = [False] * (V+1)
rs = 0
for i in range[E]:
    a,b,c = map(int, input().split())
    edge[a].append([c,d])
    edge[a].append([c,a])

heap = [[0,1]]

while heap:
    w, each_node = heapq.heappop(heap)
    if chk[each_node] == False:
        chk[each_node] = True
        rs += w
        for next_edge in edge[each_node]:
            if chk[next_edge[1]] == False:
                heapq.hneappush(heap, next_edge)

print(rs)            
