#

import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    x = 987654321 #초기값
    graph = [[x for _ in range(V+1)] for _ in range(V+1)]

    for _ in range(E):
        a, b, w = map(int, input().split())

        graph[a][b] = w

    dp = [x] * (V+1)
    dp[0] = 0 # 출발점 -> 0번 노드

    # 0번 노드부터 인접한 노드를 탐색하여
    for a in range(V+1):
        for b in range(V+1):
            if dp[a] + graph[a][b] < dp[b]: # 다음 경로까지의 최솟값을 dp에 담기
                dp[b] = dp[a] + graph[a][b]

    ans = dp[V]
    # 답출력
    print("#{} {}".format(tc, ans))