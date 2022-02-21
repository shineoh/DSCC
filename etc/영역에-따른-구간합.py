# 영역에 따른 구간합
# 2022-02-21

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 리스트 받기
    lst = [list(map(int, input().split())) for _ in range(N)]
    
    # 방향 결정(우, 하, 좌, 상)
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    ans = 0 # 최대 구간합

    # 구간합1 = 3*3배열의 합, 구간합2 = 4방향 원소의 합
    for i in range(N):
        for j in range(N):
            sum_part_1 = 0 # 구간합1
            sum_part_2 = lst[i][j] # 구간합2 -> 해당 인덱스의 값으로 초기화
            sum_part_big = 0 # 구간합 1, 2 중 더 큰 값
            part_1_possible = 0 # 구간합 1을 구할 수 있는지 여부를 판단하기 위한 변수

            # 4방향 탐색
            for d in range(4):
                # 구간합1 구할 수 있는지 여부 판단하기 -> 4방향 요소가 유효하면 구간합1 구할 수 있음
                if 0 <= i+di[d] < N and 0 <= j+dj[d] < N: # 각 방향별 탐색 시 유효범위면
                    part_1_possible += 1 # 가능여부에 +1 카운트

                # 구간합2 구하기
                for ij in range(1, lst[i][j]+1): # 해당 방향에 대해 한칸씩 넓히며 탐색
                    if 0 <= i+(di[d]*ij) < N and 0 <= j+(dj[d]*ij) < N: # 유효인덱스이면
                        sum_part_2 += lst[i+(di[d]*ij)][j+(dj[d]*ij)] # 구간합2에 값 더하기

            # 구간합1 구하기
            if part_1_possible >= 4: # 4방향 요소가 모두 유효하면
                for k in range(i - 1, i + 2): # 3*3 범위내의 요소를 순회하며
                    for l in range(j - 1, j + 2):
                        sum_part_1 += lst[k][l] # 구간합1에 값 더하기

            # 더 큰 구간합 구하기
            if sum_part_1 < sum_part_2: # 구간합 2가 더 크면
                sum_part_big = sum_part_2 # 더 큰 구간합 = 구간합 2
            else: # 아닐 경우
                sum_part_big = sum_part_1 # 더 큰 구간합 = 구간합 1

            # 최대 구간합 구하기
            if ans < sum_part_big: # 기존 최대 구간합보다 새로 구한 구간합이 클 경우
                ans = sum_part_big  # 최대 구간합 갱신

    # 답출력
    print('#{} {}' .format(tc, ans))
