# swea 5110
# 2022-04-21

# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    for _ in range(M-1):
        # 삽입할 리스트
        lst_insert = list(map(int, input().split()))
        print(lst_insert)
        flag = 0
        for i in range(len(lst)):
            if lst[i] > lst_insert[0]: # 삽입할 위치 찾기
                print(lst)
                lst[i:i] = lst_insert # i에 리스트 삽입
                print(lst)
                flag = 1
                break
        if flag == 0: # 위치 못찾았으면
            lst.extend(lst_insert) # 뒤에다가 달아주기

    ans = lst[-1:-11:-1] # 뒤에서 역순으로 10개 담기
    print('#{} '.format(tc), end='')
    print(*ans)