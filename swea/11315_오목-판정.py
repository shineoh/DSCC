# 11315_오목-판정 풀이
# 2022-02-18

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]

    # 방향 결정(우, 우하, 하, 좌하, 좌, 좌상, 상, 상우)
    di = [1, 1, 0, -1, -1, -1, 0, 1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]
    ans = 'NO' # 답 = 'NO' 로 초기화

    # 이중for문을 통해 리스트를 순회하며 돌('o')이 있는지 탐색
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 'o': # 돌이 있으면
                # 각 방향별로 오목판단을 위한 while문 시행
                for d in range(8):
                    cnt = 1 # 연속된 돌 카운트 = 1로 초기화

                    # 탐색할 인덱스가 유효할 경우 시행
                    while 0 <= i+di[d] < N and 0 <= j+dj[d] < N:
                        # 돌이 없으면 break
                        if lst[i+di[d]][j+dj[d]] == '.':
                            break
                        else: # 돌이 있을 경우, 탐색방향으로 한칸 이동하고
                            i += di[d]
                            j += dj[d]
                            cnt += 1  # +1 카운트
                        if cnt == 5: # 5개 이상 연속될 경우
                            ans = 'YES' # 답에 'YES' 담고 break
                            break

    #답 출력
    print('#{} {}' .format(tc, ans))