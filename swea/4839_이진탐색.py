# 4839 이진탐색 풀이
# 2022-02-15

import sys

sys.stdin = open('input.txt', 'r')


# 이진탐색 함수(파라메타= 전체쪽수, 좌측 끝 값, 우측 끝 값, 찾는 페이지, 탐색횟수)
def binary_search(P, l, r, key, cnt):
    c = (l + r) // 2 # c에 중간값 넣기
    cnt += 1         # 탐색횟수 +1카운트
    if c == key:     # 검색성공 -> cnt 반환
        return cnt
    elif key < c:    # 찾는 페이지가 중간값보다 작을 경우 -> 우측 끝값을 중간값으로 두고 탐색
        return binary_search(P, l, c, key, cnt)
    elif c < key:   # 찾는 페이지가 중간값보다 클 경우 -> 좌측 끝값을 중간값으로 두고 탐색
        return binary_search(P, c, r, key, cnt)


T = int(input())

for tc in range(1, T + 1):
    # P=전체쪽수, Pa=A가 찾을 쪽 번호, Pb=B가 찾을 쪽 번호
    P, Pa, Pb = map(int, input().split())
    # l=좌측끝값(1로 초기화) , r=우측끝값(전체쪽수로 초기화)
    l, r = 1, P
    # A와 B의 탐색횟수(0으로 초기화)
    cnt_a = cnt_b = 0
    # 이진탐색을 시행해서 탐색횟수가 적은 사람을 답에 담기 -> 승부가 나지 않으면 ans = 0
    if binary_search(P, l, r, Pa, cnt_a) < binary_search(P, l, r, Pb, cnt_b):
        ans = 'A'
    elif binary_search(P, l, r, Pa, cnt_a) > binary_search(P, l, r, Pb, cnt_b):
        ans = 'B'
    else:
        ans = 0

    # 답 출력
    print('#{} {}'.format(tc, ans))
