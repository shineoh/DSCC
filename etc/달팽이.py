# practice2_달팽이
# 2022-02-14

# 제시된 초기 배열
lst = [[9, 20, 2, 18, 11],
       [19, 1, 25, 3, 21],
       [8, 24, 10, 17, 7],
       [15, 4, 16, 5, 6],
       [12, 13, 22, 23, 14]]

# 숫자리스트 담을 배열
num_lst = []

# 제시된 리스트에서 숫자를 하나씩 뽑아 숫자 리스트 만들기
for i in range(5):
    num_lst.extend(lst[i])
    lst[i] = [0, 0, 0, 0, 0]  # 기존 리스트는 0으로 초기화

# 숫자리스트 정렬
num_lst = sorted(num_lst)
# 방향 결정 -> 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

direction = 0 # 방향(dx,dy의 인덱스 값)
tx, ty = 0, 0 # 현재 좌표

# 숫자리스트를 순회하며 시행
for num in num_lst:
    lst[tx][ty] = num    # 해당 위치에 숫자 넣기
    tx += dx[direction]  # x좌표 값 더해주기
    ty += dy[direction]  # y좌표 값 더해주기

    # 인덱스 범위가 유효한지, 예정된 좌표가 0인지 확인
    if 0 <= tx+dx[direction] < 5 and 0 <= ty+dy[direction] <5 and lst[tx+dx[direction]][ty+dy[direction]]==0: #조건 맞으면 continue
        continue
    else: # 조건이 안맞으면 방향바꾸기
        if direction < 3:
           direction += 1
        else:
           direction = 0

#답 출력
print(lst)
