# 백준 17144_미세먼지안녕
# 2022-03-13
import sys

input = sys.stdin.readline

R,C,T = map(int, input().split())
lst = []
cleaner_u = -1

# 공간 만들기
for i in range(R):
    lst_new = list(map(int, input().split()))
    lst.append(lst_new)
    # 공기청정기 윗부분 인덱스 찾기
    if lst[i][0] == -1 and cleaner_u == -1:
        cleaner_u = i

# 하 우 상 좌
dir = [(1,0), (0,1), (-1, 0), (0, -1)]

#미세먼지 확산
def spread(lst):
    temp = [[0] * C for _ in range(R)] # 임시 배열
    for r in range(R):
        for c in range(C):
            cnt = 0
            # 미세먼지가 있을 경우
            if lst[r][c] != -1 and lst[r][c] != 0:
                for di, dj in dir: # 각 방향을 순회하며
                    if 0 <= r + di < R and 0 <= c+dj < C and lst[r+di][c+dj] != -1: # 확산 가능하면
                        temp[r+di][c+dj] += lst[r][c]//5 # 확산량을 임시배열에 넣기
                        cnt += 1
            lst[r][c] -= (lst[r][c]//5)*cnt # 확산 후 남은양 반영
    
    # 확산량 기존 공간에 반영
    for r in range(R):
        for c in range(C):
            lst[r][c] += temp[r][c]
    return

def clean(r):
    # 위
    for cr in range(r-1, 0, -1): # 하
        lst[cr][0] = lst[cr-1][0]
    lst[0][0] = 0
    for cc in range(C-1): #좌
        lst[0][cc] = lst[0][cc+1]
    lst[0][C - 1] = 0
    for cr in range(r):  # 상
        lst[cr][C-1] = lst[cr+1][C-1]
    lst[r][C-1] = 0
    for cc in range(C-1, 1, -1): #우
        lst[r][cc] = lst[r][cc-1]
    lst[r][1] = 0
    # 아래
    for cr in range(r+3, R):  # 상
        lst[cr-1][0] = lst[cr][0]
    lst[R-1][0] = 0
    for cc in range(C - 1):  # 좌
        lst[R-1][cc] = lst[R-1][cc + 1]
    lst[R-1][C - 1] = 0
    for cr in range(R-1, r+1, -1): # 하
        lst[cr][C-1] = lst[cr-1][C-1]
    lst[r+1][C-1] = 0
    for cc in range(C-1, 1, -1): #우
        lst[r+1][cc] = lst[r+1][cc-1]
    lst[r+1][1] = 0
    return


for _ in range(T): # T번 반복
    spread(lst)
    clean(cleaner_u)

ans = 2
for r in range(R):
    for c in range(C):
        ans += lst[r][c]

print(ans)
