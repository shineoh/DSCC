# 나선주행로
# R, C (범위) 주고 어디서부터 어디까지 가는지(S, T) 주어짐
# 조건 2<= R, C <= 50, S< T
# input
# tc1:
# 4 5
# 8 13
#
# tc2:
# 3 3
# 3 9
#
# output
# 2
# 3


R, C = map(int, input().split())
S, T = map(int, input().split())

dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

lst = [[0 for _ in range(C)] for _ in range(R)]
ni = nj = 0
d = 0
cnt = 0
ans = 0
lst[0][0] = 1
num = 1

while True:
    di, dj = dir[d]
    if num > T:
        break
    if 0 <= ni + di < R and 0 <= nj + dj < C and lst[ni + di][nj + dj] == 0:
        ni += di
        nj += dj
        lst[ni][nj] = 1
        num += 1
        if cnt != 0:
            if S < num < T:
                ans += 1
            cnt = 0
    else:
        cnt += 1
        if cnt == 3:
            break
        if d == 3:
            d = 0
        else:
            d += 1

print(ans+1)