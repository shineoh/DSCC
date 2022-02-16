# 델타탐색 풀이
# 2022-02-14

# 인풋 받기
lst = [list(map(int, input().split())) for _ in range(5)]

# 방향 결정 위한 리스트 -> 우하좌상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# 차이값 담을 변수
diff = 0
for i in range(5): # 행에 대한 반복
    for j in range(5): # 열에 대한 반복
        for k in range(4): # 각 방향 순회하며 인접한 값 탐색
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<5 and 0<=nj<5: # 인접한 인덱스가 유효하면
                diff += abs(lst[i][j] - lst[ni][nj]) # 차의 절댓값을 diff에 더하기

print(diff)




