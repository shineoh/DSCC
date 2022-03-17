# 1231_중위순회 풀이
# 2022-03-17

import sys

sys.stdin = open('input.txt', 'r')

# 트리 읽기
def read(tree, i):
    s='' #문자열 담을 공간
    if i*2 <= N: # 왼쪽 읽기
        s+=read(tree, i*2)
    s+=tree[i] # 문자열에 정점 추가
    if i*2+1 <= N: # 오른쪽 읽기
        s+=read(tree, i*2+1)
    return s

for tc in range(1, 11):
    N = int(input())
    tree=[[0] for _ in range(N+1)] # 트리
    for i in range(1, N+1): # 노드 번호에 해당하는 노드 값 담아주기
        peak = input().split()
        tree[int(peak[0])] = peak[1]
    ans = read(tree, 1) # 트리 읽어서 답에 담기
    # 답 출력
    print('#{} {}' .format(tc, ans))