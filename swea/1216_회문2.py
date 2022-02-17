# 1216_회문2 풀이
# 2022-02-17
# import sys
# sys.stdin = open('input.txt', 'r')

T = 10
for _ in range(1, T+1):
    tc = int(input())
    txt = ''
    for _ in range(100): # 문자열로 이어받기
        txt += input()

    cnt = 0  # 회문의 길이
    max_cnt =0 # 최댓값
    N = 100 # 변의 길이

    # 이중 for문을 돌며 회문 탐색
    for i in range(100):
        for j in range(100):
            for k in range(100 - j, -1, -1):
                # 가로 방향 탐색
                if txt[(N*i)+j] == txt[(N*i)+(j+k-1)]: # 문자열의 첫 글자와 끝 글자가 같을 때
                    if txt[(N*i)+j:(N*i)+(j+k)] == txt[(N*i)+j:(N*i)+(j+k)][::-1]: # 해당 문자열이 회문인지 판단하여 회문이면
                        cnt = k # 카운트에 k 담기
                        # 최댓값과 비교하여 최댓값 갱신
                        if max_cnt < cnt:
                            max_cnt = cnt

                # 세로 방향 탐색_ N(100)단위로 슬라이싱
                if txt[(N*j)+i] == txt[(N*(j+k-1))+i]: # 문자열의 첫 글자와 끝 글자가 같을 때
                    if txt[(N*j)+i:(N*(j+k-1))+i+1:N] == txt[(N*j)+i:(N*(j+k-1))+i+1:N][::-1]: # 해당 문자열이 회문인지 판단하여 회문이면
                        cnt = k # 카운트에 k 담기
                        # 최댓값과 비교하여 최댓값 갱신
                        if max_cnt < cnt:
                            max_cnt = cnt

    # 답 출력
    print('#{} {}'.format(tc, max_cnt))



    # for i in range(100):
    #     for j in range(100):
    #         for k in range(99-j,-1,-1):
    #             # 가로
    #             if txt[i][j] == txt[i][j+k]:
    #                 if txt[i][j:j+k+1] == txt[i][j:j+k+1][::-1]:
    #                     cnt = k
    #                     if max_cnt < cnt:
    #                         max_cnt = cnt
    #             # 세로
    #             if txt[j][i] == txt[j+k][i]:
    #
    #                 if txt[j:j+k][i] == txt[j:j+k][i][::-1]:
    #                     cnt = k
    #                     if max_cnt < cnt:
    #                         max_cnt = cnt

