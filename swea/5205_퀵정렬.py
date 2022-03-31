# 5205_퀵정렬
# 2022-03-31

import sys

sys.stdin = open('input.txt', 'r')

def quick_sort(lst, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 값을 찾을 때까지 반복
        while(left <= end and lst[left] <= lst[pivot]):
            left += 1
        # 피벗보다 작은 값을 찾을 때까지 반복
        while(right > start and lst[right] >= lst[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 값과 피벗 교체
            lst[right], lst[pivot] = lst[pivot], lst[right]
        else: # 엇갈리지 않았다면 작은 값과 큰 값 교체
            lst[left], lst[right] = lst[right], lst[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(lst, start, right - 1)
    quick_sort(lst, right + 1, end)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    quick_sort(lst, 0, N-1)
    print('#{} {}' .format(tc, lst[N//2]))