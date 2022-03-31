# 1865_동철이의-일분배
# 2022-03-31

import sys

sys.stdin = open('input.txt', 'r')

def DFS(i,end,result):
    global ans
    if i == end:
        if result > ans: # 최대값 갱신
            ans = result
        return
    if result <= ans: # 가지치기 - 값을 곱할 수록 작아질수밖에 없으므로
        return
    for j in range(N):
        if not visited[j]: # 방문 하지 않았다면
            new_result = result * lst[i][j] * 0.01
            visited[j] = 1 # 방문 표시
            DFS(i+1,end,new_result)
            visited[j] = 0 # 방문 배열 초기화

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    ans = 0
    DFS(0, N, 1)
    # 답 출력
    print("#{} {}".format(tc, format(ans * 100, ".6f")))





# 2차원리스트 조합
# def DFS(L,x):
#
#     if L == r:
#         print(result)
#     else:
#         for i in range(len(a)):
#             if checklist[i] == 0:
#                 result[L] = a[x][i]
#                 checklist[i] = 1
#                 DFS(L+1, x+1)
#                 checklist[i] = 0
#
#
# a = [0, 1, 2], [3, 4, 5], [6, 7, 8]
#
# r = 3
#
# result = [0] * r
#
# checklist = [0] * len(a)
#
# DFS(0, 0)