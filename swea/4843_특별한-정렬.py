# 4843 특별한 정렬 풀이
# 2022-02-15
import sys

sys.stdin = open('input.txt', 'r')


# 정렬 함수(인자= 리스트, 숫자 개수)
def zigzag_sort(lst, N):
    # 1~10까지 순회하며 정렬 수행
    for i in range(10):
        Idx = i    # 찾는 값의 인덱스를 담을 변수
        if i % 2:  # i가 홀 수일 때
            for j in range(i + 1, N): # i 뒤의 요소들을 순회하며 최솟값 찾기
                if lst[Idx] > lst[j]:
                    Idx = j
            lst[i], lst[Idx] = lst[Idx], lst[i] # i와 Idx의 수를 교환
        else:      # i가 짝 수일 때
            for j in range(i + 1, N): # i 뒤의 요소들을 순회하며 최댓값 찾기
                if lst[Idx] < lst[j]:
                    Idx = j
            lst[i], lst[Idx] = lst[Idx], lst[i] # i와 Idx의 수를 교환
    return lst # 정렬된 리스트 반환


T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # 리스트 내 숫자 개수
    lst = list(map(int, input().split())) # 제시된 숫자 담은 리스트
    zigzag_sort(lst, N) # 정렬 시행

    # 답 출력
    print('#{}'.format(tc), end=' ')
    for i in range(10):
        print(lst[i], end=' ')
    print()
