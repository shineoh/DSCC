# 1213_String 활용 풀이
# 2022-02-16
import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')

for _ in range(10):
    tc = int(input())
    str_find = input()  # 찾아야할 문자열
    str_gived = input() # 제시된 문자열
    cnt = 0 # 담을 담을 변수

    # 제시된 문자열을 순회하며
    for i in range(len(str_gived)):
        if str_gived[i] == str_find[0]: # 찾아야할 문자열의 첫째글자와 같을 경우
            # i를 기준으로 찾아야할 문자열의 길이만큼 비교하여 일치하면 카운팅
            if str_gived[i:i+len(str_find)] == str_find:
                cnt += 1
    # 답출력
    print('#{} {}' .format(tc, cnt))
