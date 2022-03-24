# 1242_암호코드 스캔 풀이
# 2022-03-24

import sys

sys.stdin = open('input.txt', 'r')


# 암호의 첫 인덱스 찾는 함수
def find(lst):
    for i in range(N):
        for j in range(M - 1, 0, -1):  # 뒤에서부터 1 찾기
            if lst[i][j]:
                row = i
                col = j
                return row, col


# 암호해독 함수 정의
def decode(num):
    dic = {
        (2, 1, 1): 0,
        (2, 2, 1): 1,
        (1, 2, 2): 2,
        (4, 1, 1): 3,
        (1, 3, 2): 4,
        (2, 3, 1): 5,
        (1, 1, 4): 6,
        (3, 1, 2): 7,
        (2, 1, 3): 8,
        (1, 1, 2): 9,
    }
    nums=[]
    n1 = n2 = n3 = 0  # 각 비율 담을 변수
    cnt = 0 # 암호 자리수
    odd = even = 0 # 홀수, 짝수 자리
    temp = ''
    ans = 0 # 답 담을 변수
    for code in lst: # 리스트의 각 코드 내부를 순회하며
        for i in range(len(code)): # 각 비율 구하기
            if code[i] == '1' and n2 == 0:
                n1 += 1
            elif code[i] == '0' and n1 != 0 and n3 == 0:
                n2 += 1
            elif code[i]  == '1' and n2 != 0:
                n3 += 1
            elif n3 != 0: # 3개의 비율을 구했으면
                cnt+= 1
                min_n = min(n1, n2, n3) # 최솟값 구하기
                pw = dic[(n1//min_n, n2//min_n, n3//min_n)] # 비율을 이용해서 암호 가져오기
                temp += str(pw) # 임시변수에 더하기
                if cnt == 8: # 암호길이만큼 확인하면
                    if (odd * 3 + even + pw) % 10 == 0 and temp not in nums: # 해당 암호가 유효한지 조건 판별
                        ans += odd + even + pw # 유효하면 답에 담기
                    nums.append(temp) # 방문 표시
                    odd=even=cnt=0 # 변수 초기화
                    temp='' # 변수  초기화
                # 암호를 확인하며 홀수/짝수 값 더하기
                elif cnt % 2:
                    odd += pw
                else:
                    even += pw
                n1 = n2= n3 =0 # 변수 초기화
    return ans


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().strip().split())
    lst = list(set([input().strip() for _ in range(N)]))
    # print(lst)

    # 전체를 4bit 2진수로 바꾼 값들을 모아둘 문자열
    bit = ''
    # 입력 받은 16진수 하나하나 순회해서 변경
    for i in range(len(lst)):
        bit = ''
        for j in range(len(lst[i])):
            # 각 값을 10진수로 먼저 바꾸기
            tmp = int(lst[i][j], 16)
            # 10진수를 다시 2진수로 바꾸기
            tmp = bin(tmp).replace('0b', '')
            # 길이가 4인 2진수가 필요
            while len(tmp) != 4:
                tmp = '0' + tmp
            bit += tmp
        lst[i] = bit # 변환한 값으로 리스트 변경
    ans = decode(lst) # 리스트 해독하여 답에 담기
    # 답출력
    print('#{} {}' .format(tc, ans))



