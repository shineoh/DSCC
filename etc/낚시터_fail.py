# 낚시터 풀이

def find_place(ans, x, y):
    cnt = 0
    lst_check = [0 for _ in range(N+1)]
    ans_n = ans
    global k
    x_n = x
    y_n = y
    a, b = lst_m[sequence[k][y]]
    # 거리를 담은 리스트 만들기
    for i in range(1, N + 1):
        if lst_p[i] == 0:
            lst_check[i] = abs(a-i) + 1

    while cnt < b:
        min_d = N +2
        min_p = -1
        if cnt == b - 1: #2개 남았을때
            min_p2 = 0
            for i in range(1, N + 1):
                if lst_p[i] == 0:
                    if lst_check[i] < min_d:
                        min_d = lst_check[i]
                        min_p = i
                        min_p2 = 0
                    elif lst_check[i] == min_d: # 같은게 2개면
                        min_p2 = i
            if x == 0: # x가 0이면
                if min_p2 == 0:
                    lst_p[min_p] = 1
                    ans_n += lst_check[min_p]
                else:  # 마지막턴에 2개 선택해야할 때?
                    x_n = min_p2
                    return ans, x_n, y
            else: # x가 0이 아니면
                lst_p[x] = 1
                ans_n += lst_check[x]
                x_n = 0
        else:
            for i in range(1, N + 1):
                if lst_p[i] == 0:
                    if lst_check[i] < min_d:
                        min_d = lst_check[i]
                        min_p = i
            lst_p[min_p] = 1
            ans_n += lst_check[min_p]
        cnt += 1
        # print(lst_check)
        # print(lst_p)

    return ans_n, x_n, y_n

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst_p = [0 for _ in range(N+1)]
    lst_m = []
    ans = 0
    for _ in range(3):
        a, b = map(int, input().split())
        lst_m.append((a, b))

    lst_final = []
    sequence = [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]]
    for k in range(6):
        stack = []
        x = 0
        y = 0
        stack.append(find_place(ans, x, y))
        while stack:
            ans, x, y = stack.pop()
            if x == 0:
                if y == 2:
                    lst_final.append(ans)
                else:
                    stack.append(find_place(ans, x, y + 1))
            else:#x가 0이 아니면
                # ans_t, x_t, y_t = find_place(ans, x, y)
                # if ans > ans_t:
                #     ans = ans_t
                # x = 0
                if y == 2:
                    lst_final.append(ans)
                else:
                    stack.append(find_place(ans, x, y+1))

    ans_real = lst_final[0]
    for ans_final in lst_final:
        ans_real > ans_final
        ans_real = ans_final

    print('#{} {}'.format(tc, ans_real))
