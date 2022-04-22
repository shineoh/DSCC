# swea 5120
# 2022-04-22

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    header = 0 # 헤더가 가르키는 위치
    for _ in range(K):
        header = (header + M) % N
        if header == 0: # 나눠떨어지면 -> 리스트의 끝이면
            lst.append(lst[-1] + lst[0])
            header = -1 # 헤더 위치 -1로 조정(나눠떨어지는 바람에 끝이 아닌 0이 됐으므로)
        else:
            lst.insert(header, lst[header-1] + lst[header])
        N += 1
    # 뒤에서 역순으로 10개 출력
    ans = lst[-1:-11:-1]
    print('#{} '.format(tc), end='')
    print(*ans)

    # 헤더 위치를 옮길 때 나눠떨어지는 경우에 헤더위치를 조정하지 않아 틀렸었음

