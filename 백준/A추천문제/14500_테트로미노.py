# 백준 14500_테트로미노

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

# 가능한 모양 모두 정의
dic = [
    [(0,0), (0,1), (1,0), (1,1)], # 네모
    [(0,0), (0,1), (0,2), (0,3)], # 일자_1
    [(0,0), (1,0), (2,0), (3,0)], # 일자_2
    [(0,0), (0,1), (0,2), (1,0)], # ㄱ_1
    [(1,0), (1,1), (1,2), (0,2)], # ㄱ_2
    [(0,0), (1,0), (1,1), (1,2)], # ㄱ_3
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ_4
    [(0,0), (1,0), (2,0), (2,1)], # ㄱ_5
    [(2,0), (2,1), (1,1), (0,1)], # ㄱ_6
    [(0,0), (0,1), (1,0), (2,0)], # ㄱ_7
    [(0,0), (0,1), (1,1), (2,1)], # ㄱ_8
    [(0,0), (0,1), (0,2), (1,1)], # ㅗ_1
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ_2
    [(0,0), (1,0), (2,0), (1,1)], # ㅗ_3
    [(1,0), (0,1), (1,1), (2,1)], # ㅗ_4
    [(1,0), (2,0), (0,1), (1,1)], # 2꺾_1
    [(0,0), (1,0), (1,1), (2,1)], # 2꺾_2
    [(1,0), (0,1), (1,1), (0,2)], # 2꺽_3
    [(0,0), (0,1), (1,1), (1,2)] # 2꺾_4
]

ans = 0
for i in range (N): # 리스트를 모두 순회하며
    for j in range(M):
        for k in range(19): # 각 인덱스에서 가능한 모든형태 시도
            temp = 0
            for l in range(4):
                if 0<= i+dic[k][l][0] < N and  0<= j+dic[k][l][1] < M: #인덱스가 유효하면
                    ni = i+dic[k][l][0]
                    nj = j+dic[k][l][1]
                    temp += lst[ni][nj] # 값 만들기
            if temp > ans: #최댓값 갱신
                ans=temp

print(ans) # 답 출력









# def t1(i, j, di, dj):
#     ni = i
#     nj = j
#     sum = lst[ni][nj]
#     cnt = 1
#     while cnt <4:
#         ni += di
#         nj += dj
#         if 0<=ni<N and 0<=nj<N:
#             sum+=lst[ni][nj]
#             cnt+=1
#     return sum
#
# def t2(i, j):
#     sum = lst[i][j]
#     if N<=i+1 or N<=j+1:
#         return sum
#     sum += lst[i+1][j]
#     sum += lst[i][j+1]
#     sum += lst[i+1][j+1]
#     return sum
#
# def t3(i, j, di, dj):
#     ni = i
#     nj = j
#     sum = lst[ni][nj]
#     cnt = 1
#     while cnt <3:
#         ni += di
#         nj += dj
#         if 0<=ni<N and 0<=nj<N:
#             sum+=lst[ni][nj]
#             cnt+=1
#     if di==0:
#         if lst[][]

    # return sum
