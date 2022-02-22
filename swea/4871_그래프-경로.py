# 4871_그래프-경로 풀이
# 2022-02-22

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split()) # V = 노드 개수, E = 간선 개수
    start = [0] * E # 경로의 출발노드
    end = [0] * E # 경로의 도착노드
    stack = [] # 경로탐색에 활용할 스택

    # E개의 경로를 받아 출발노드와 도착노드 저장
    for i in range(E):
        start[i], end[i] = map(int, input().split())

    # 시작점과 도착점 받기
    starting_point, destination = map(int, input().split())
    # 시작점을 스택에 담기
    stack.append(starting_point)
    ans = 0 # 답(0으로 초기화)
    i = 0 # 경로를 표시하는 인덱스
    num_start_node = E # 탐색 가능한 start 노드의 개수

    # 반복문을 통한 경로 탐색 -> stack[-1]은 현재 위치를 표시
    while True:
        if not stack: # 스택이 비었으면 break
            break
        if start[i] == stack[-1]: # 현재 위치에서 갈 수 있는 경로가 있으면
            stack.append(end[i]) # 1) 해당 경로의 도착노드를 스택에 담고
            num_start_node -= 1  # 2) 탐색가능한 시작노드 -1 카운트
            start[i] = 0 # 3) 사용한 시작노드 0 으로 변경 (재탐색 하지 않도록)
            i = 0 # 경로를 처음부터 탐색하도록 i =0으로 초기화

        if stack[-1] == destination: # 현재위치가 도착점과 같으면
            ans = 1 # ans = 1 넣고 break
            break

        elif i == E-1: # 출발노드를 모두 탐색했으면 (가능 경로를 찾지 못하고)
            stack.pop() # 경로를 되돌아가서 탐색
            i = 0

        elif num_start_node == 0 : # 더 이상 경로 탐색이 가능한 노드가 없으면 break
            break

        else: # 다음 출발노드 탐색
            i += 1
    
    # 답 출력
    print('#{} {}' .format(tc, ans))