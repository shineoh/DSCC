# 1232 사칙연산
# 2022-03-18

import sys

sys.stdin = open('input.txt', 'r')

# 트리 읽기
def read(v): #후위순회
    if not tree[v][0] in operator: # 정점이 숫자이면 숫자 리턴
        return tree[v][0]
    else: # 정점이 연산자이면
        l = read(tree[v][1]) # 좌측
        r = read(tree[v][2]) # 우측
        # 각 연산자에 맞게 연산 시행
        if tree[v][0] == '+':
            result = l + r
        elif tree[v][0] == '-':
            result = l - r
        elif tree[v][0] == '*':
            result = l * r
        elif tree[v][0] == '/':
            result = l // r

        return result # 연산 결과 리턴


operator = ['+','-','*','/']

for tc in range(1, 11):
    N = int(input())
    tree=[[[] for _ in range(3)] for _ in range(N+1)] # 트리
    for i in range(N): # 노드 번호에 해당하는 노드 값 담아주기
        info = input().split()
        temp_0 = int(info[0])
        temp_1 = info[1]
        if temp_1 not in operator: # 숫자 일때 int로 넣기
            tree[temp_0][0] = int(temp_1)
        else: # 연산자면 그대로(string)으로 넣기
            tree[temp_0][0] = temp_1
        if len(info) == 4: # 사칙연산 -> 자식이 다 있을 때 넣기
            tree[temp_0][1] = int(info[2])
            tree[temp_0][2] = int(info[3])

    ans = read(1) # 트리 읽어서 답에 담기
    # 답 출력
    print('#{} {}' .format(tc, ans))