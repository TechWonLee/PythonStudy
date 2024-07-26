# 백준 11047 동전O

import sys

input = sys.stdin.readline

N,L = map(int, input().split())
coins = [list(input()) for _ in range(N)]
coins.reverse()
cnt = 0

for each_coin in coins:
    cnt += K // each_coin
    K = K % each_coin

print(cnt)