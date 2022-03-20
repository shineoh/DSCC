# 17070 파이프 옮기기
# 2022-03-20


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

pipe = [(0,0), (0,1)] # 파이프 초기 위치
stack = []
stack.append(pipe) # 스택 이용
cnt = 0
# 각 방향에 따른 인덱스 증가량 --> 대각선 방향은 조건 따로 적용
dir_r=[(0, 1)]
dir_c=[(1, 0)]
dir_cross=[(0, 1), (1, 0)]

while stack:
    p = stack.pop()
    bi, bj = p[0] # 파이프 뒷부분
    ci ,cj = p[1] # 파이프 앞부분(이동 방향)

    if ci == N-1 and cj == N-1: # 목적지 도달하면 카운트
        cnt+=1

    elif bi + 1 == ci and bj == cj: # 가로방향일 때
        for di, dj in dir_c:
            if ci + di<N and cj + dj < N and lst[ci+di][cj+dj] != 1:
                stack.append(([(ci, cj),(ci + di, cj + dj)]))

    elif bi == ci and bj + 1 == cj: # 세로방향
        for di, dj in dir_r:
            if ci + di < N and cj + dj < N and lst[ci + di][cj + dj] != 1:
                stack.append(([(ci, cj), (ci + di, cj + dj)]))

    elif bi + 1 == ci and bj + 1 == cj: # 대각선 방향
        for di, dj in dir_cross:
            if ci + di < N and cj + dj < N and lst[ci + di][cj + dj] != 1:
                stack.append(([(ci, cj), (ci + di, cj + dj)]))

    # 대각선 방향으로 이동할때 -> 3칸이 빈칸이어야 함
    if ci + 1 < N and cj + 1 < N and lst[ci + 1][cj + 1] != 1 and lst[ci][cj +1] != 1 and lst[ci + 1][cj] != 1:
        stack.append(([(ci, cj), (ci + 1, cj +1)]))

# 답 출력
print(cnt)