# 4873_반복문자-지우기 풀이
# 2022-02-22

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    sentence = input() # 문자열 받기
    i = 0 # 문자열 순회를 위한 index
    while i<len(sentence)-1:
        if sentence[i] == sentence[i+1]: # 문자가 연속되면
            sentence = sentence[:i] + sentence[i+2:] # 연속되는 문자를 제거하여 문자열 구성
            i = 0 # index = 0 으로 초기화
        else: # 문자가 연속되지 않으면
            i += 1 # 다음 누자 탐색
    ans = len(sentence) # 완성된 문자열의 길이를 답에 담기

    # 답 출력
    print('#{} {}'.format(tc, ans))



    ## 스택으로 풀기
    # T = int(input())
    #
    # for tc in range(1, T + 1):
    #     Sentence = list(input())
    #     stack = []
    #     # 문자열 내 문자들을 순회하며
    #     for i in range(len(Sentence)):
    #         if stack and stack[-1] == Sentence[i]: # 문자가 최근 값과 같으면(스택에 값이 있을 때)
    #             stack.pop() # 최근 값 pop
    #         else: # 아닐 경우
    #             stack.append(Sentence[i]) # 문자를 스택에 추가
    #
    #     print('#{} {}'.format(tc, len(stack)))