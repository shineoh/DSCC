# 1952_수영장 풀이
# 2022-03-22

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def DFS(n, ssum):
    global ans
    if n>12:
        if ans > ssum:
            ans = ssum
        return

    DFS(n+1, ssum + lst[n]*day) #일일권
    DFS(n+1, ssum + mon) #월
    DFS(n+3, ssum + mon3) # 분기
    DFS(n+12, ssum + year) #년


for tc in range(1, T+1):
    day, mon, mon3, year = (map(int, input().split()))
    lst = [0]+list(map(int, input().split()))
    ans = 12345678
    DFS(1, 0)
    print('#{} {}' .format(tc, ans))