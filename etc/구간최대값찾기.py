# 구간 최대값 찾기 풀이
# 2022-02-21

T = int(input())
for tc in range(1, T+1):
    # N = 리스트의 길이, K = 구간의 길이
    N, K = map(int, input().split())
    # 리스트 받기
    lst = [list(map(int, input().split())) for _ in range(N)]
    ans = 0 # 최대 구간합

    for i in range(N):
        sum_part = 0  # 구간 합
        # i행의 구간합은 i행의 i번 째 열에서 부터 k 까지의 합임
        if i+K <= N: # i+K가 유효범위 내일 때
            k = i + K # k = i + K (i에서 i + 구간길이까지)
        else: # i+K가 N을 넘어가면
            k = N # N(마지막 인덱스) 까지만 더함

        # 구간합 구하기
        for j in range(i, k):  # i부터 k까지
            sum_part += lst[i][j] # 요소들을 구간합에 더하기

        # 최대 구간합 갱신하기
        if ans < sum_part: # 기존 최대 구간합보다 새로 구한 구간합이 클 경우
            ans = sum_part # 최대 구간합 갱신
    # 답출력
    print('#{} {}' .format(tc, ans))
