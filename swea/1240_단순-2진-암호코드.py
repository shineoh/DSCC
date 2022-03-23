# 1240_단순-2진-암호코드 풀이
# 2022-03-23

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
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }
    return dic[num]


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input())) for _ in range(N)]

    # 암호 위치의 행열
    row = find(lst)[0]
    col = find(lst)[1]

    # 뒤에서부터 조사했으므로 원래 형태로 암호 표현
    password = lst[row][col - 55:col + 1]
    result = ''  # 해독결과 담을 변수

    for i in range(0, len(password), 7):  # 7개 단위로 순회
        temp = ''
        for j in range(i, i + 7):  # 해당 범위의 암호를 해독하여 담기
            temp += str(password[j])
        result += decode(temp)

    odd = even = 0  # 홀수,짝수자리 수 담을 변수

    for i in range(7):
        if i % 2:  # 홀수 --> 암호의 짝수
            even += int(result[i])  # 합 구하기
        else:  # 암호의 홀수
            odd += int(result[i])
    check = odd * 3 + even + int(result[7])  # 암호 조건 검증

    # 암호 조건이 안맞으면
    if check % 10:
        ans = 0
    else:  # 암호 조건이 맞으면(10의 배수이면)
        ans = 0
        for i in range(8):  # 각 자리수 더한 답 구하기
            ans += int(result[i])

    # 답 출력
    print("#{} {}".format(tc, ans))
