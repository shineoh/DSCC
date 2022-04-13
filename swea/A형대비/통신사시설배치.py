import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())

# 비용 편익을 최대화하도록 기지국을 건설했을 때, 계산한 비용 편익 값을 출력하는 프로그램을 작성하라
# 비용 편익은 다음과 같이 계산한다.
#
#         Ui = i번째 기지국이 건설된 Cell의 사용자 수
#         비용 편익(Cost-Benefit) = (U1 + U2 + U3 + U4)2
#

for tc in range(1, T+1):
    #  지도의 가로(M)와 세로(N) 크기
    M, N = map(int, input().split())
    # HN에 걸쳐 한 줄에 W개씩 Cell의 사용자 수
    lst = [list(map(int, input().split())) for _ in range(N)]
    num_lst = [[0]*M for _ in range(N)]

    odd = [(1,0), (0,1), (0, -1), (-1, -1), (-1, 0), (-1,1)]
    even = [(-1,0), (0,1), (0, -1), (1, -1), (1, 0), (1,1)]

    num = 1
    for i in range(N):
        for j in range(M):
            num_lst[i][j] = num
            num+=1

    stack =[]
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            visited[i][j] = 1
            stack.append((i,j,1, lst[i][j], visited))
            #stack.append(([(i,j)], 1))

    ans = 0
    # print(lst)
    # print(num_lst)
    # for i in range(N):
    #     for j in range(M):
    #         haha = num_lst[i][j]
    #         while haha > M:
    #             haha -= M
    #         print(haha)
    #         # a = num_lst[i][j] % M
    #         # print((num_lst[i][j] % M)//2)
    #         # print(a // 2)

    while stack:
        #s_lst, sc = stack.pop()
        si, sj, sc, an, sv = stack.pop()
        if sc==4:
            # s=0
            # for (ai, aj) in s_lst:
            #     s+=lst[ai][aj]
            if ans < an:
                ans = an

        haha = num_lst[si][sj]
        while haha>M:
            haha -= M
        if haha % 2 == 1:
            for di, dj in odd:
                ni = si+di
                nj = sj+dj
                if 0<=ni<N and 0<=nj<M:
                    #and (ni,nj) not in sv:
                    # s_lst.append((ni,nj))
                    #stack.append((s_lst, sc+1))
                    #n=s_lst.pop()
                    sv.
                    stack.append((ni, nj, sc+1, an+lst[ni][nj], sv))
        elif haha % 2 == 0:
            for di, dj in even:
                ni = si+di
                nj = sj +dj
                if 0<=ni<N and 0<=nj<M:
                    #and (ni,nj) not in sv:
                    # s_lst.append((ni, nj))
                    # stack.append((s_lst, sc + 1))
                    # n=s_lst.pop()
                    # # sv.append((ni,nj))
                    # # stack.append((ni, nj, sc+1, sv))

                    stack.append((ni, nj, sc + 1, an + lst[ni][nj]))
                    # sv[ni][nj]=1
                    # stack.append((ni, nj, sc + 1, an + lst[ni][nj], sv))
                    # sv[ni][nj]=0


            # if num_lst[si][sj] // 2 == 1 :
            #     if M //2 ==0:
            #         for di, dj in odd:
            #             ni = si+di
            #             nj = sj +dj
            #             if 0<=ni<N and 0<=nj<M and (ni,nj) not in sv:
            #                 #sv[ni][nj] = 1
            #                 sv.append((ni,nj))
            #                 stack.append((ni, nj, sc+1, sv))
            #     else:
            #         for di, dj in even:
            #             ni = si + di
            #             nj = sj + dj
            #             if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in sv:
            #                 # sv[ni][nj] = 1
            #                 sv.append((ni, nj))
            #                 stack.append((ni, nj, sc + 1, sv))
            #
            #
            # elif num_lst[si][sj] // 2 ==0:
            #     if M // 2 == 0:
            #         for di, dj in even:
            #             ni = si + di
            #             nj = sj + dj
            #             if 0 <= ni < N and 0 <= nj < M and (ni,nj) not in sv:
            #                 # sv[ni][nj] = 1
            #                 sv.append((ni, nj))
            #                 stack.append((ni, nj, sc + 1, sv))
            #     else:
            #         for di, dj in odd:
            #             ni = si+di
            #             nj = sj +dj
            #             if 0<=ni<N and 0<=nj<M and (ni,nj) not in sv:
            #                 #sv[ni][nj] = 1
            #                 sv.append((ni,nj))
            #                 stack.append((ni, nj, sc+1, sv))


    print('#{} {}' .format(tc, ans**2))