# 1223_계산기2 풀이
# 2022-02-23

import sys

sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    form = [] # 후위 표기식 담을 리스트
    stack = [] # 빈 스택
    lst = list(input()) # 계산식 받기

    # 계산식을 후위 표기식으로 변환
    for elem in lst: # 계산식 내 요소를 순회하며
        if elem == '*': # *일 경우 스택에 push
            stack.append(elem)
        elif elem == '+': # +일 경우(두 연산자중 우선순위가 낮으므로)
            while stack: # 스택 내의 연산자들을 빼서 form에 넣고
                form.append(stack.pop())
            stack.append(elem) # 스택에 + push
        else: # 숫자일 경우 form에 int형으로 변환하여 담기
            form.append(int(elem))

    while stack: # 스택에 남아있는 연산자들 form에 담기
        form.append(stack.pop())

    for i in range(N): # 계산식을 순회하며
        if form[i] == '+': # + 일 경우 계산할 숫자들 빼서 계산
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b) # 계산 결과값 스택에 담기
        elif form[i] == '*': # * 일 경우 스택에서 숫자들 빼서 계산(*) 후 다시 담기
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        else: # 숫자 스택에 담기
            stack.append(form[i])

    # 답출력(최종 계산값 스택[0]에 담겨있음)
    print('#{} {}' .format(tc, stack[0]))