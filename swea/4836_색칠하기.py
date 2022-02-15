# 4836 색칠하기 풀이
# 2022-02-15
import sys

sys.stdin = open('input.txt', 'r')

# 색칠하기 함수
def painting(x1, y1, x2, y2, c):
    for i in range(x1, x2 + 1):  # 제시된 범위를 순회하며 색칠
        for j in range(y1, y2 + 1):
            # 해당 칸이 색칠하려는 색(c)과 같거나, 보라색(3)이면 continue
            if lst[i][j] == c or lst[i][j] == 3:
                continue
            else: # 유효할 경우 색칠하기
                lst[i][j] += c
    return


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 색이 칠해져있지않은 10*10 공간 만들기
    lst = [[0] * 10 for _ in range(10)]
    cnt = 0  # 보라색 영역을 카운트할 변수
    # 제시된 색칠횟수 N만큼 순회하며 색칠
    for _ in range(N):
        # 좌측상단모서리(x1, x2), 우측하단모서리(x2, y2), 색칠하려는 색(c) 받기
        x1, y1, x2, y2, c = map(int, input().split())
        painting(x1, y1, x2, y2, c) # 색칠하기

    # 10*10 리스트를 순회하며 보라색 영역 카운팅
    for k in range(10):
        for l in range(10):
            if lst[k][l] == 3:
                cnt += 1
    # 답 출력
    print('#{} {}'.format(tc, cnt))
