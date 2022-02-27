# 2116_주사위 쌓기

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

# 바닥면과 윗면 관계
bottom_top = {0:5, 5:0, 1:3, 3:1, 2:4, 4:2,}

ans = 0 # 답 담을 변수

for i in range(6): # 첫 주사위 여섯면을 순회하며 바닥면으로 설정
    max_lst = []  # 각 주사위의 최댓값 담을 리스트
    t = lst[0][bottom_top[i]] # 윗면
    max_num = 0 # 주사위의 옆면 중 최댓값 담을 변수
    sum_num = 0

    for j in range(6): # 6면 중
        if j == i or j == t: # 바닥면, 윗면 제외
            continue
        if max_num < j: # 옆면 중 최댓값 찾기
            max_num = j
    max_lst.append(max_num) # 최댓값 리스트에 저장

    for k in range(1,N): # 2~N번째 주사위
        max_num = 0 # 옆면 중 최대값 담을 변수
        num_lst = [1, 2, 3, 4, 5, 6] # 주사위 범위 리스트
        num_lst.remove(t) # 바닥면 빼기
        t = lst[k][bottom_top[lst[k].index(t)]]  # 윗면(전 주사위 윗면의 윗면)
        num_lst.remove(t) # 윗면 빼기
        for l in num_lst: # 주사위의 범위를 순회하며
            if max_num < l: # 최대값 찾기
                max_num = l
        max_lst.append(max_num) # 최대값 리스트에 저장

    for num in max_lst: # 최대값 리스트에 저장된 값들의 합 구하기
        sum_num += num
    if ans < sum_num: # 합이 답보다 크면 답 갱신
        ans = sum_num

print(ans)
