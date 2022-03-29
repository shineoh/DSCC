# 5201_컨테이너-운반
# 2022-03-29
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    w_lst = list(map(int, input().split())) # 화물의 무게
    w_lst.sort(reverse=True) # 역방향 정렬 -> 무거운 것 부터 옮기기 위해
    t_lst = list(map(int, input().split())) # 적재용량
    t_lst.sort() # 순방향 정렬 -> 같은 무게의 화물에 대해 적재용량이 적은 트럭부터 사용
    used = [0]*M # 트럭 사용여부 체크
    ans = 0 # 답 담을 변수

    for i in range(N): # 화물 순회
        temp = 0 # 트럭이 결정됐는지 여부 확인할 변수
        for j in range(M): # 트럭 순회
            if temp==1: # 트럭이 결정됐으면 continue
                continue
            if used[j] ==0 and w_lst[i]<=t_lst[j]: # 트럭이 사용되지 않았고 화물을 실을 수 있으면
                ans += w_lst[i] # ans에 해당 화물용량 추가
                used[j] = 1 # 사용 표시
                temp =1 # 트럭 결정됐음을 표시

    # 답출력
    print('#{} {}' .format(tc, ans))

