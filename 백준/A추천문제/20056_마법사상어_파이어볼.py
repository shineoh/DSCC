
N, M, K = map(int, input().split())
lst = [[[] for _ in range(N)] for _ in range(N)]
dir = [(-1,0), (-1, 1), (0, 1), (1, 1), (1, 0), (1,-1), (0, -1), (-1, -1)]
q = []
for _ in range(M):
    r, c, m, d, s = list(map(int, input().split()))
    q.append([r-1, c-1, m, s, d])
for _ in range(K):
    while q:
        cr, cc, cm, cd, cs = q.pop(0)
        nr = (cr + cs * dir[cd][0]) % N
        nc = (cr + cs * dir[cd][1]) % N
        lst[nr][nc].append([cm, cs, cd])

    for i in range(N):
        for j in range(N):
            if len(lst[i][j]) >= 2:
                sum_m, sum_s, flag_odd, flag_even, cnt = 0, 0, 0, 0, len(lst[i][j])
                while lst[i][j]:
                    m, s, d = lst[i][j].pop(0)
                    sum_m += m
                    sum_s += s
                    if d % 2:
                        flag_odd = 1
                    else:
                        flag_even = 1
                if flag_odd + flag_even == 1:  # 모두 홀수이거나 모두 짝수인 경우
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sum_m // 5 == 0:
                    continue # 질량 0이면 소멸
                for d in nd:
                    q.append([i, j, sum_m//5, sum_s//cnt, d])

            # 1개인 경우
            if len(lst[i][j]) == 1:
                q.append([i, j] + lst[i][j].pop())

print(q)
ans = 0
for _,_,m,_,_ in q:
    ans += m
print(ans)
