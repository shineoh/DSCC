# 1961_숫자-배열-회전 풀이
# 2022-02-21

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 파스칼의 삼각형의 높이(행의 수)
    lst = [[0] * N for _ in range(N)] # 파스칼의 삼각형을 담을 리스트(값=0으로 초기화)

    for i in range(N):
        for j in range(i+1): # 0~i+1까지(행+1의 길이만큼)
            if j==0 or j==i: # 양 끝 값은
                lst[i][j] = 1 # 1을 주고
            else: # 중간 값들은 위 행의 j-1, j 번째 열의 수를 더한 값을 준다
                lst[i][j] = lst[i-1][j-1] + lst[i-1][j]

    # 답 출력
    print('#{}' .format(tc))
    # 이차원 리스트 -> 이중포문을 통해 출력
    for ans_lst in lst:
        for ans in ans_lst:
            if ans: # 0이 아닌 수들을 출력
                print(ans, end='')
        print() # 행을 넘겨주기 위함