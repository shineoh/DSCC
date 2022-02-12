# swea 1209_Sum
# 2022-02-12

import sys
sys.stdin = open('input.txt', 'r')


T = 10
for tc in range(1, T+1):
    num_tc = int(input())
    lst_num = []
    # 각 line의 최댓값을 담을 변수 설정
    max_sum_row = max_sum_col = max_sum_cross = 0
    # 최종 답을 담을 변수
    max_ans = 0
    # 입력되는 행을 반복적으로 추가하여 2차원 배열 생성
    for _ in range(100):
        lst_num.append(list(map(int, input().split())))
    # 각 방향별 대각선의 합을 담을 변수 
    sum_cross_r = sum_cross_l = 0

    # 1차(외부),2차(내부) 반복문을 돌며 최댓값 구하기
    for i in range(100):
        # 행, 열의 합을 담을 변수
        sum_row = sum_col = 0
        # 2차 반복문을 돌며 각 행과 열의 합 구하기
        for j in range(100):
            sum_row += lst_num[i][j]
            sum_col += lst_num[j][i]
        # 2차 반복문을 빠져나온 뒤 최댓값 최신화
        if sum_row > max_sum_row:
            max_sum_row = sum_row
        if sum_col > max_sum_col:
            max_sum_col = sum_col
        # 1차 반복문을 돌며 대각선의 합 구하기
        sum_cross_r += lst_num[i][i]
        sum_cross_l += lst_num[i][99-i]
    # 1차 반복문을 빠져나와 최댓값 최신화
    if sum_cross_l > sum_cross_r:
        max_sum_cross = sum_cross_l
    else:
        max_sum_cross = sum_cross_r

    # 각 라인의 합 중 최댓값을 담은 리스트
    ans_lst = [max_sum_row, max_sum_col, max_sum_cross]
    # 리스트에 담긴 값들을 비교하여 전체 최댓값 도출
    for ans in ans_lst:
        if ans>max_ans:
            max_ans = ans
    
    #답 출력
    print('#{} {}' .format(tc, max_ans))


