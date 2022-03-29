# 5202_화물도크
# 2022-03-29
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [tuple(map(int, input().split())) for _ in range(N)]
    # 리스트 정렬 : 종료시간 - 시작시간 기준으로 정렬
    lst.sort(key = lambda x : (x[1], x[0]))
    ans = 0 # 답 담을 변수
    stack=[(0,1)] # 스택(현재위치, 사용화물차 수)
    while stack:
        ci, cnt = stack.pop() # 현재위치, 사용화물차 수
        if cnt> ans: # 최대값 갱신
            ans = cnt
        for i in range(ci, N): # 현재 위치부터 탐색하며
            if lst[ci][1] <= lst[i][0]: # 현재 종료시간이후 사용가능한 스케쥴이 있다면
                stack.append((i,cnt+1)) # 스택에 push

    # 답출력
    print('#{} {}'.format(tc, ans))
