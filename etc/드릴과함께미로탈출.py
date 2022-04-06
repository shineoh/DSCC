# 드릴과 함께 미로탈출
# 2022-04-04

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    # 방향 증감자
    dir = [(0,1), (1, 0), (0, -1), (-1, 0)]
    ans = -1 # 답 담을 변수

    # 출발지점 찾기
    tmp = 0
    for i in range(N): # 리스트를 순회하며
        for j in range(N):
            if lst[i][j] == 2: # 출발지점 찾으면 break
                start_i, start_j = i,j
                tmp=1
                break
        if tmp==1:
            break

    stack = [(i,j,0, 0)] # 스택 생성 (행 인덱스, 열 인덱스, 이동거리, 벽제거횟수)
    ans_lst=[] # 답 후보 리스트
    while stack: # 스택이용
        si, sj, cnt, delW = stack.pop(0)
        for di, dj in dir: # 각 방향을 순회하며
            ni = si + di
            nj = sj + dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0: #인덱스가 유효하고 방문하지 않았으면 시행
                visited[ni][nj] = 1 # 방문 표시
                cnt += 1 # 이동거리 카운트
                if lst[ni][nj] == 3:  # 도착했을 경우
                    if cnt == abs(ni - start_i) + abs(nj - start_j):  # 이동거리가 최소거리면
                        ans = cnt  # 답에 담고 break
                        break
                    else:  # 최소거리가 아닐경우
                        ans_lst.append(cnt)  # 답후보 리스트에 추가
                if lst[ni][nj] ==0: # 통로일 경우 이동
                    stack.append((ni, nj, cnt, delW))
                elif lst[ni][nj] ==1: # 벽일 경우
                    if delW>=2: # 벽 제거 기회를 다썼으면 continue
                        continue
                    else: # 벽 제거 가능하면 제거 후 이동
                        stack.append((ni, nj, cnt, delW+1))
        if ans != -1 : # 이동거리 최소로 종료되었으면 break
            break
    if ans == -1: # 이동거리 최소로 종료되지 않았으면
        if ans_lst == []: # 답후보 리스트 비었을 경우
            ans=-1 # -1 담아서 출력
        else: # 비어있지 않으면
            ans = min(ans_lst) # 최소값 담아서 출력

    # 답출력
    print('#{} {}' .format(tc, ans))



