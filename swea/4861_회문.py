# 4861_회문 풀이
# 2022-02-17

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # N = 글자판 한 변의 길이, M = 회문의 길이
    N, M = map(int, input().split())
    # lst = [input() for _ in range(N)]

    txt = '' # 제시되는 글자판 담을 변수
    for _ in range(N): # 문자열로 이어받기
        txt += input()
    ans = '' # 답 담을 변수

    # 이중 for문을 돌며 회문 탐색
    for i in range(N):
        for j in range(N):
            # 가로 방향 탐색
            if j+M<=N and txt[(N*i)+j] == txt[(N*i)+(j+M-1)]: # 인덱스가 유효하고 문자열의 첫 글자와 끝 글자가 같을 때
                if j+M<=N and txt[(N*i)+j:(N*i)+(j+M)] == txt[(N*i)+j:(N*i)+(j+M)][::-1]: # 해당 문자열이 회문인지 판단하여 회문이면
                    ans = txt[(N*i)+j:(N*i)+(j+M)] # 답에 담기

            # 세로 방향 탐색(N단위로 슬라이싱)
            # 인덱스 유효성과 문자열의 첫 글자와 끝 글자가 같은지 판단
            if j+M<=N and 0<=(N*(j+M-1))+i<N*N and txt[(N*j)+i] == txt[(N*(j+M-1))+i]:
                # 해당 문자열이 회문인지 판단 -> 답에 담기
                if txt[(N*j)+i:(N*(j+M-1))+i+1:N] == txt[(N*j)+i:(N*(j+M-1))+i+1:N][::-1]:
                    ans = txt[(N*j)+i:(N*(j+M-1))+i+1:N]

    # 답 출력
    print('#{} {}'.format(tc, ans))
