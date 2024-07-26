# 백준 15649 N과 M(1)

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
rs =[]
chk = [False] * (N+1)

#외워라
def recur(num):
    if num == M:
        print(' '.join(map(str,rs)))
        return 
for i in range(1, N+1):
    if chk[i] ==False:
        chk[i] = True
        rs.append(i)
        recur(num+1)
        rs.pop()
recur(0)