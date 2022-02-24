# 4874_Fourth 풀이
# 2022-02-24

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    lst = list(input().split())
    stack = []
    # 연산자일 경우 계산하도록 lambda식 정의
    operator = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
    }

    for elem in lst: # 리스트내 요소들 순회하며
        if elem in operator.keys(): # 연산자일 경우 계산할 숫자들 빼서 계산
            if len(stack) < 2: # 계산할 숫자 부족하면
                ans = 'error'
                break
            else: # 충분하면 계산
                b = stack.pop()
                a = stack.pop()
                c = operator[elem](a, b)
                stack.append(c)  # 계산 결과값 스택에 담기
        elif elem == '.': # 계산식 끝날 때
            if len(stack) != 1: # stack에 값이 없거나 1개 초과면
                ans = 'error' # 에러
            else:
                ans = stack[0] # 1개일 경우 답 담기
        else: # 숫자일 경우 스택에 추가
            stack.append(int(elem))

    # 답출력
    print('#{} {}' .format(tc, ans))