# 2667 단지번호붙이기
# 2022-04-16

N = int(input())
lst = [list(map(int, input())) for _ in range(N)]

def dfs(i,j):
    stack = [(i, j)]
    cnt = 1
    lst[i][j] = 0
    while stack:
        si, sj = stack.pop()
        for di, dj in dir:
            ni = si + di
            nj = sj + dj
            if 0 <= ni < N and 0 <= nj < N and lst[ni][nj] == 1:
                stack.append((ni,nj))
                lst[ni][nj] = 0
                cnt +=1
    return cnt

cnt_danji = 0
dir = [(1,0), (0,1), (0,-1), (-1, 0)]
cnt_lst = []

for i in range(N):
    for j in range(N):
        if lst[i][j] == 1 :
            cnt_lst.append(dfs(i,j))
            cnt_danji +=1

cnt_lst.sort()
print(cnt_danji)
for ans in cnt_lst:
    print(ans)

