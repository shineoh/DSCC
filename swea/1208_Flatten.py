# 1208_Flatten 풀이
# 2022-02-10

import sys
sys.stdin = open('input.txt', 'r')

T = 10 # 제시된 Testcase

for tc in range(1, T + 1):

    # n_dump = 덤프 횟수, box_lst = 제시된 박스 리스트
    n_dump = int(input())
    box_lst = list(map(int, input().split()))
    ans = 0 # 답 넣을 변수

    # 덤프 횟수+1 만큼 반복 --> 덤핑 종료 후 최고점, 최소점을 한 번 더 탐색
    for i in range(n_dump+1):
        # 최고점, 최소점, 각각에 해당하는 index값을 표현하기 위한 변수 정의
        max_height = 0
        min_height = 101
        i_max_height = 0
        i_min_height = 0

        # 박스리스트를 순회하며 최고점, 최저점, 각각에 해당하는 index값 구하기
        for j in range(len(box_lst)):
            if box_lst[j] <= min_height:
                min_height = box_lst[j]
                i_min_height = j
            if box_lst[j] >= max_height:
                max_height = box_lst[j]
                i_max_height = j

        # 덤핑 횟수가 끝났을 경우 탐색이 끝난 시점에서 ans에 최고점과 최저점의 높이 차 할당
        if i == n_dump:
            ans = max_height - min_height

        # 덤핑 --> 최고점의 박스 -1, 최소점의 박스 +1
        box_lst[i_max_height] -= 1
        box_lst[i_min_height] += 1

        # 평탄화 작업이 완료됐을 경우, 작업 중단하고 최고점과 최저점의 높이 차 출력
        if max_height - min_height <= 1:
            ans = max_height - min_height
            break
    
    #답 출력
    print('#{} {}'.format(tc, ans))