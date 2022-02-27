# 2304 창고다각형

N = int(input())
lst = []
max_L = 0 # 가장 우측에 위치한 기둥의 왼쪽 면 위치
max_H = 0 # 가장 높은 기둥의 높이
max_H_l = 0 # 가장 높은 기둥의 왼쪽 면 위치

# 기둥 정보 받아서 변수들의 값 찾기
for _ in range(N):
    L, H = map(int, input().split())
    lst.append((L,H))
    if L > max_L:
        max_L = L
    if H > max_H:
        max_H = H
        max_H_l = L

# 기둥 개수에 맞춰 리스트 구현
lst_warehouse = [0] * (max_L + 1)
# 리스트에 기둥 정보 입력(왼쪽 면 위치에 해당하는 인덱스에 높이 저장)
for l, h in lst:
    lst_warehouse[l] = h

ans = 0 # 답 담을 변수
now_h = 0 # 기둥의 기준 높이
# 가장 높은 기둥의 좌측을 순회하며
for i in range(max_H_l+1):
    if now_h < lst_warehouse[i]: # 기둥의 기준 높이보다 현재 기둥이 높으면
        now_h = lst_warehouse[i] # 기준 높이 업데이트
    ans += now_h # 기준 높이만큼 답에 카운트
now_h = 0 # 우측을 순회하기 위한 기준 초기화
for j in range(max_L, max_H_l, -1): # 우측을 순회하며 위의 작업 반복
    if now_h < lst_warehouse[j]:
        now_h = lst_warehouse[j]
    ans += now_h

# 답 출력
print(ans)



