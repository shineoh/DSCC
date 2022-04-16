# 유기농배추
# 2022-04-16

# 커버링
def dfs(i, j):
    stack = [(i, j)]
    lst[i][j] = 0
    while stack:
        si, sj = stack.pop()
        for di, dj in dir:
            ni = si + di
            nj = sj + dj
            if 0 <= ni < N and 0 <= nj < M and lst[ni][nj] == 1:
                lst[ni][nj] = 0
                stack.append((ni, nj))
    return

T = int(input())
dir = [(1,0), (0,1), (0,-1), (-1, 0)]

ans_lst = []
for _ in range(T):
    M, N, K = map(int, input().split())
    lst = [[0]*M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        lst[r][c] = 1
    ans = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1 :
                dfs(i,j)
                ans +=1
    ans_lst.append(ans)

for ans in ans_lst:
    print(ans)

