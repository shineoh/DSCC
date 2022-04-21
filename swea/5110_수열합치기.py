# swea 5110
# 2022-04-21

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    for _ in range(M-1):
        lst_insert = list(map(int, input().split()))
        flag = 0
        for i in range(len(lst)):
            if lst[i] > lst_insert[0]:
                lst[i:i] = lst_insert
                flag = 1
                break
        if flag == 0:
            lst.extend(lst_insert)
    ans = lst[-1:-11:-1]
    print('#{} '.format(tc), end='')
    print(*ans)