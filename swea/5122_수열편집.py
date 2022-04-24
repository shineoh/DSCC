# swea 5122
# 2022-04-23

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    lst = list(map(int, input().split()))
    for _ in range(M):
        temp = list(input().split())  # 어디에[1] 무엇을[2] 어떻게[0] 할지
        where = int(temp[1]) # 어디에
        if temp[0] == 'D': # [1] 빼기
            lst.pop(where)
        else:
            what = int(temp[2]) # 무엇을
            if temp[0] == 'I': # [1]에 [2]를 추가하기
                lst.insert(where, what)
            elif temp[0] == 'C': # [1]에 [2] 담기
                lst[where] = what

    print('#{} '.format(tc), end='')
    if len(lst) < L:
        print(-1)
    else:
        print(lst[L])