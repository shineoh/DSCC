# 농장 속 토끼
# 2022-03-28

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split()) # N:농장 크기, M:토끼 수
    lst = [list(map(int, input().split())) for _ in range(M)] # 인풋리스트
    farm = [[0]*N for _ in range(N)] # 농장 초기화
    # 방향 -> 상하좌우
    dir = [(-1, 0), (1, 0), (0, -1), (0,1)]
    cnt = 0 # 카운트 담을 변수
    for i, j, d, p in lst: # 각 리스트를 순회하며
        if farm[i][j] == 0: # 농장의 해당 위치가 0이면
            farm[i][j] = 1 # 방문 표시(1)
            cnt += 1       # 카운트 + 1
        di, dj = dir[d] # 인덱스 증감 변수
        ni = i+di*p   # 토끼의 이동 방향과 점프 거리를 반영한 이동예정 위치
        nj = j+dj*p
        while 0<=ni<N and 0<=nj<N: # 농장 범위를 벗어날 때까지
            if farm[ni][nj] == 0: # 이동하려는 위치가 0이면
                farm[ni][nj] = 1 # 방문표시
                cnt += 1  # 카운트 +1
            ni += di*p # 다음 이동할 위치
            nj += dj*p

    # 답출력
    print('#{} {}' .format(tc, cnt))
