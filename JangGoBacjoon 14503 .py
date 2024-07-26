# 백준 14503 로봇 청소기
import sys
input = sys.stdin.readline
N ,M = (int, input().split())
y,x,d = map(int, input().split())
map = [list(map(int,input().split())) for _ in range(N)]
cnt = 0 
dy = [-1,0,1,0]
dx = [0,1,0,-1]

while 1:
    if map[y][x] ==0:
        map[y][x] =2
        cnt +=1
    sw = False
    for i in range(1,5):
        cnt += 1
        for i in range(1,5):
            print("d-i : :", d-i)
            ny = y + dy[d-i]
            nx = x + dx[d-i]
            if 0<=ny<N and 0 <=nx<M:
              if map[ny][nx] == 0:
                d = (d-i+4) %4
                # 그 방향으로 회전한 다음 한 칸을 전진하고 1부터 진행한다
                d = d-i
                y = ny
                x = nx
                break
    # 4방향 모두 있지 않은 경우
    if sw == False:
        # 뒤쪽 방향이 막혀있는지 확인
        ny = y - dy[d]
        nx = x - dx[d]
        if 0<ny<N and 0 <= nx <M:
           if map[ny][nx] == 1:
              break
           else:
               y = ny
               x = nx
        else:
           break
print(cnt)
