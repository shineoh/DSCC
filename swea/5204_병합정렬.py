# 5204_병합정렬 풀이
# 2022-03-30


def merge(left, right):
    global answer
    if right[-1] < left[-1]: # 좌측 끝 원소가 우측 끝 원소보다 크면 count
        answer += 1

    len_l = len(left)
    len_r = len(right)
    result = [0 for _ in range(len_l+len_r)]
    l = r = i = 0
    while l < len_l or r < len_r: # left, right에 추가할 원소 남아있을 때까지 반복
        if l < len_l and r < len_r: # left, right에 둘다 원소가 남아 있다면
            if left[l] <= right[r]: # 좌측이 작은 경우
                result[i] = left[l] # 좌측 값 추가
                i += 1 # result 다음 자리로 이동
                l += 1 # left의 다음 원소 지목
            else:
                result[i] = right[r] # 우측이 작은 경우, 우측 값 추가
                i += 1 # result 다음 자리로 이동
                r += 1 # right의 다음 원소 지목
        elif l < len_l: # left에만 원소 남아있으면
            result[i] = left[l]
            i += 1
            l += 1
        elif r < len_r: # right에만 원소 남아있으면
            result[i] = right[r]
            i += 1
            r += 1
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    answer = 0
    result = merge(lst)

    # 답출력
    print('#{} {} {}'.format(tc, result[N//2], answer))


