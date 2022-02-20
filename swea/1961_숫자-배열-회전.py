# 1961_숫자-배열-회전 풀이
# 2022-02-18

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst90 = [[0]*N for _ in range(N)]
    lst180 = [[0]*N for _ in range(N)]
    lst270 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            lst90[i][j] = lst[N-j-1][i]
            lst180[i][j] = lst[N-i-1][N-j-1]
            lst270[i][j] = lst[j][N-i-1]
    print('#{}' .format(tc))
    for ans1, ans2, ans3 in zip(lst90, lst180, lst270):
        print('{} {} {}' .format("".join(map(str, ans1)), "".join(map(str, ans2)), "".join(map(str, ans3))))