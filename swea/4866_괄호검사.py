# 4863_괄호검사 풀이
# 2022-02-22

import sys

sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    sentence = input() # 주어진 문장
    stack = [] # 빈 스택 생성
    last = '' # 가장 위에 담겨있던 값(pop했을 때 나오는 값)
    ans = 0 # 답 (0으로 초기화)
    check = 1 # 조건 충족여부 확인 (1로 초기화)

    for s in sentence: # 주어진 문장의 요소들을 순회하여
        if s == '{' or s == '(': # 여는 괄호면
            stack.append(s)  # 스택에 넣기
        elif s == '}' or s == ')': # 닫는 괄호면
            # 스택이 비었는지 확인
            if stack: # 값이 있을 경우
                last = stack.pop() # pop해서 last에 담기
            else: # 스택이 비었다면 check=0 주고 break
                check = 0
                break
            # 여는괄호와 닫는 괄호가 안맞으면 check=0 주고break
            if last == '{' and s == ')':
                check = 0
                break
            if last == '(' and s == '}':
                check = 0
                break

    # for문 종료 후 스택이 비었는지 여부와 조건 충족 여부 확인
    if not stack and check == 1: # 스택이 비어있고 조건을 충족했으면
        ans = 1 # 답 = 1

    # 답 출력
    print("#{} {}".format(tc, ans))
