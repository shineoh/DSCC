# Gravity 풀이
# 2022-02-09

# 입력받아 리스트 생성
box_lst = list(map(int, input().split()))

# 변수 정의
ans = 0 # 답을 넣을 변수
h_fall = [] # 낙차를 담을 리스트

# 반복문을 통해 낙차 조사
for i in range(99, -1, -1):
    cnt = 0
    first_location = 0
    # 뒤에서부터 순회하며, i번째 위치에 상자가 있으면 시행(기존 리스트를 순회했을 때 해당하는 높이만큼 상자가 쌓여있을 경우)
    for j in range(99, -1, -1):
        if box_lst[j] < i+1:
            continue
        else:
            cnt += 1  # 회전 후 쌓이는 상자 수 --> 최종 값은 회전 후 가장 높은 박스의 위치와 같음
            first_location = j # 회전했을 때 가장 높은 박스와 천장간의 거리
    if cnt != 0:
        h_fall.append(100 - first_location - cnt)
    # (99)-(first_location)-(cnt) = 낙차


# 낙차를 담은 리스트에서 최댓값을 ans에 할당
for h in h_fall:
    if ans < h:
        ans = h

print(ans)

