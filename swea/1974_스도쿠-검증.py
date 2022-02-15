# 1974_스도쿠-검증 풀이
# 2022-02-15

import sys
sys.stdin = open('input.txt', 'r')

# 스도쿠 검증 함수 -> 리스트를 받아서 해당 리스트에 1~9 숫자가 하나씩 들어가는지 확인
def check_sdoku(lst):
    lst_check = [0] * 9       # 0으로 구성된 길이 9의 체크리스트
    for num in lst:           # 리스트의 숫자를 순회하며
        lst_check[num-1] = 1  # 숫자에 대응하는 인덱스의 값을 1로 변경
    if 0 in lst_check :       # 체크리스트 내에 0이 있으면 0 반환
        return 0
    else:                     # 체크리스트가 모두 1이면 1 반환
        return 1

T = int(input())
for tc in range(1, T+1):
    # 9*9의 숫자 배열 받기
    lst = [list(map(int, input().split())) for _ in range(9)]
    ans = 1 # 답 담을 변수 1로 초기화

    for i in range(9):
        # 테스트할 리스트를 담을 공간
        lst_test1 = []
        lst_test2 = []
        for j in range(9): # 각 행, 열별로 테스트리스트 생성
            lst_test1.append(lst[i][j])
            lst_test2.append(lst[j][i])

        # 테스트리스트로 스도쿠 검증 함수 시행 -> 하나라도 0이면 0반환하고 break
        if check_sdoku(lst_test1) == 0 or check_sdoku(lst_test2) == 0:
            ans = 0
            break

    # 작은 사각형 별로 테스트리스트 생성
    for j in range(0, 7, 3):
        for k in range(0, 7, 3):
            lst_test3 = []
            for l in range(3):
                for m in range(3):
                    lst_test3.append(lst[j + l][k + m])

            # 테스트리스트로 스도쿠 검증 함수 시행 -> 0이면 0반환하고 break
            if check_sdoku(lst_test3) == 0:
                ans = 0
                break

    # 답출력 -> 모든 테스트를 통과한 배열은 1반환
    print('#{} {}' .format(tc, ans))

