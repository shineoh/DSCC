# 4869_종이붙이기 풀이
# 2022-02-22

import sys

sys.stdin = open('input.txt', 'r')

# 종이붙이기 함수(재귀)
def stick_paper(n):
    if n == 1: # n이 1일 때 1반환
        return 1
    if n == 2: # n이 2일때 3반환
        return 3
    else:  # n>2일 때 n-1, n-2에 대한 함수를 실행한 값 받아오기
        return stick_paper(n-1) + 2*stick_paper(n-2)

T = int(input())
for tc in range(1, T+1):
    N = (int(input())/10) # 종이의 길이 받아서 10으로 나눈 값 저장
    ans = stick_paper(N) # 종이붙이기 함수 실행 결과
    # 답 출력
    print('#{} {}' .format(tc, ans))
