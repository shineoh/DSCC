# 테두리그물낚시
# 2022-04-04

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    # 방향 증감자
    dir = [(0,1), (1, 0), (0, -1), (-1, 0)]
    ans = 0 # 답 담을 변수
    # 이차원리스트를 순회하며 각 인덱스에서 시행
    for i in range(N):
        for j in range(M):
            ni, nj = i, j
            temp=0 # 부분합 담을 변수
            for di, dj in dir: # 각 방향에 대해
                check = 0
                for k in range(K-1): # k번 반복하며
                    ni += di # 해당 방향으로 ni 이동
                    nj += dj # 해당 방향으로 nj 이동
                    if 0<=ni<N and 0<=nj<M: # 이동한 인덱스가 유효하면
                        temp+= lst[ni][nj] # 부분합에 추가
                    else: # 유효범위를 벗어날 경우
                        check = 1 # 체크하고 break
                        break
                if check == 1: # 유효범위를 벗어났을 경우 break
                    break
            if check==0 and ans<temp: # 부분합 탐색이 정상종료됐고 부분합이 답보다 클 경우
                ans = temp # 최대값 갱신
    # 답 출력
    print('#{} {}' .format(tc, ans))