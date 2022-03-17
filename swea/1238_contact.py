# swea 1238_contact
# 2022-03-16

import sys

sys.stdin = open('input.txt', 'r')

def contact(q):
    while q:
        q_temp = [] # 임시큐
        max_v = 0 # 최댓값
        while q:
            v = q.pop() # 연락할 노드 뽑기
            if max_v < v: # 최댓값 갱신
                max_v = v
            check[v] = 1  # 반복 방지를 위한 체크
            while lst[v]: # 해당 노드의 하부트리를 돌며
                vv = lst[v].pop() # 연락받을 노드 뽑기
                if check[vv]: # 이미 연락받았으면 continue
                    continue
                q_temp.append(vv) # 연락받은 노드들 임시큐에 넣기
        if q_temp: # 임시 큐가 있으면(마지막 연락이 아니면)
            q = q_temp
    return max_v



for tc in range(1, 11):
    lst = [[] for _ in range(102)]
    N, start = map(int, input().split())
    lst_input = list(map(int, input().split()))
    # 입력데이터 전처리
    for i in range(0, N, 2):
        lst[lst_input[i]].append(lst_input[i+1])
    # 시작점 넣은 큐 형성
    q = [start]
    check = [0 for _ in range(102)]
    ans = contact(q)
    print('#{} {}' .format(tc, ans))