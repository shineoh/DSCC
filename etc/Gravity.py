# Gravity 풀이
# 2022-02-09

# 입력받아 리스트 생성
box_lst = list(map(int, input().split()))

# 변수 정의
after_lst = [0]*100 # 회전 후의 상자 상태를 표현할 리스트
ans = 0 # 답을 넣을 변수
h_fall = [] # 낙차를 담을 리스트

# 90도를 회전할 때 box_lst의 행은 after_lst의 열이 됨
# ex) 1층에 위치한 박스가 10개일 경우 after_lst의 첫번째 칸에 10개의 박스가 쌓임

# 반복문을 통해 after_lst의 i번째 칸에 box_lst의 j+1층에 있는 박스 수만큼 넣어줌
for i in range(100):
    cnt = 0
    for j in range(100):
        if box_lst[j] >= i+1:
            cnt += 1
    after_lst[i] = cnt

# 반복문을 통해 낙차 조사
# 끝에서부터 순회하며 after_lst(회전 후)의 k위치에 박스가 있을 경우 시행
for k in range(99, -1, -1):
    if after_lst.append(k) != 0:
        # 기존 리스트를 앞에서부터 순회하며 k층에 박스가 있을 경우 인덱스를 활용해 낙차 계산 후 break(가장 높은 값만 필요)
        for l in range(100):
            if box_lst[l] >= k:
                h_fall.append(99-l-after_lst[k])
                break

# 낙차를 담은 리스트에서 최댓값을 ans에 할당
for h in h_fall:
    if ans < h:
        ans = h

print(ans)

