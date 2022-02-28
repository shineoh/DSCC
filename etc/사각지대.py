# 사각지대 풀이
# 2022-02-28

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    # 방향
    di = [1, 0, -1, 0]
    dj = [0, -1, 0, 1]
    # 이중for문 순회하며
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 2: # 경비원이 있을 경우(2)
                d = 0 # 방향 0으로 초기화
                ni = i # 탐색을 위한 인덱스 ni, nj 를 각각 i, j로 초기화
                nj = j
                while True:
                    ni += di[d] # 해당 방향탐색
                    nj += dj[d]
                    if  ni < 0 or nj < 0 or ni >= N or nj >= N or lst[ni][nj]==1: # 인덱스가 유효하지 않거나 벽(1)일 경우
                        if d == 3: # 방향을 모두 탐색했으면 break
                            break
                        else: # 아닐경우 방향 전환하고 인덱스를 i, j 로 초기화
                            d+=1
                            ni = i
                            nj = j
                    # 0일 경우 1로 바꿔주기
                    if lst[ni][nj] == 0:
                        lst[ni][nj] = 1
    cnt = 0 # 사각지대 카운트할 변수
    # 이중 for문 순회하며 시야에 들어가지 않은 통로가 있을 경우 cnt +1 카운트
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 0:
                cnt+=1
    
    # 답 출력
    print('#{} {}' .format(tc, cnt))