# 4864_문자열-비교 풀이
# 2022-02-17

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    str1 = input() # 첫 번째 문자열
    str2 = input() # 두 번째 문자열
    ans = 0 # 담을 담을 변수

    # 두 번째 문자열 내에 첫 번째 문자열이 있는지 찾기
    for i in range(len(str2)): # 두 번째 문자열을 순회하며
        if str2[i] == str1[0]: # 첫 번째 문자열의 첫째글자와 같을 경우
            # i를 기준으로 찾아야할 문자열의 길이만큼 비교하여 일치하면 ans = 1
            if str2[i:i+len(str1)] == str1:
                ans = 1

    # 답출력
    print('#{} {}'.format(tc, ans))

