# 특별이벤트
# 선물리스트(각 상자엔 랜덤으로 포인트가 들어가있음) 중 주어진 선물 선택
# 주어진 상자 수의 절반 이하로 선택할 수 있음
# 인접한 선물들을 선택할 수 없음(1개 이상 건너 뛰어서 선택가능
# 최대 얼마의 포인트를 받을 수 있는가?

# 조건 : 2<= N <= 2X 10^5 , |Ai| <= 10^9

# input 선물 상자의 수와 각각에 들어있는 포인트
# tc1:
# 6
# 1 2 3 4 5 6
#
# tc2:
# 5
# -20 -10 -5 0 5
#
# tc3:
# 7
# 9 -5 2 7 4 -3 2
#
# output
# 12
# 0
# 18

N = int(input())
lst = list(map(int, input().split()))
k = N //2
kk = 0
around = [-1, 0, 1]
visited = [0] *N
stack = []
for i in range(N):
    stack.append([i])
max_lst = []
while stack:
    ans_lst = stack.pop()
    if kk == k:
        ss = 0
        for i in ans_lst:
            ss += lst[i]
        max_lst.append((ss, i))
    else:
        for i in range(len(ans_lst)):
            visited[i] = 1
            for j in around:
                if 0<= i+j < k:
                    visited[i+j] =1
            # not visited = []
            for i in range(N):
                if visited[i] == 0:
                    temp = ans_lst + [i]
                    stack.append((temp, kk+1))
ans = max(max_lst)
print(ans)