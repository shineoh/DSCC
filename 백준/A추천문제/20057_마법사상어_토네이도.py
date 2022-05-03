N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]
cnt = 1

x = N // 2
y = N // 2
ans = 0

def tornado(x, y, nx, ny, ratio):
    global lst, N, ans
    if (x < 0 or x >= N or y < 0 or y >= N):
        ans += int(lst[nx][ny] * ratio)
        return int(lst[nx][ny] * ratio)
    lst[x][y] += int(lst[nx][ny] * ratio)
    return int(lst[nx][ny] * ratio)


while True:
    if cnt % 2 == 0:
        for _ in range(cnt):  # 우
            dust = 0
            dust += tornado(x-1, y, x, y+1, 0.01)
            dust += tornado(x+1, y, x, y+1, 0.01)
            dust += tornado(x-1, y+1, x, y+1, 0.07)
            dust += tornado(x+1, y+1, x, y+1, 0.07)
            dust += tornado(x-2, y+1, x, y+1, 0.02)
            dust += tornado(x+2, y+1, x, y+1, 0.02)
            dust += tornado(x-1, y+2, x, y+1, 0.1)
            dust += tornado(x+1, y+2, x, y+1, 0.1)
            dust += tornado(x, y+3, x, y+1, 0.05)
            lst[x][y+1] -= dust
            if y+2 >= N:
                ans += lst[x][y+1]
            else:
                lst[x][y+2] += lst[x][y+1]
            lst[x][y+1] = 0
            y = y + 1

        for _ in range(cnt):  # 상
            dust = 0
            dust += tornado(x, y-1, x-1, y, 0.01)
            dust += tornado(x, y+1, x-1, y, 0.01)
            dust += tornado(x-1, y-1, x-1, y, 0.07)
            dust += tornado(x-1, y+1, x-1, y, 0.07)
            dust += tornado(x-1, y-2, x-1, y, 0.02)
            dust += tornado(x-1, y+2, x-1, y, 0.02)
            dust += tornado(x-2, y-1, x-1, y, 0.1)
            dust += tornado(x-2, y+1, x-1, y, 0.1)
            dust += tornado(x-3, y, x-1, y, 0.05)
            lst[x-1][y] -= dust
            if x-2 < 0:
                ans += lst[x-1][y]
            else:
                lst[x-2][y] += lst[x-1][y]

            lst[x-1][y] = 0
            x = x-1
    else:
        for _ in range(cnt):  # 좌
            dust = 0
            dust += tornado(x+1, y, x, y-1, 0.01)
            dust += tornado(x-1, y, x, y-1, 0.01)
            dust += tornado(x-1, y-1, x, y-1, 0.07)
            dust += tornado(x+1, y-1, x, y-1, 0.07)
            dust += tornado(x-2, y-1, x, y-1, 0.02)
            dust += tornado(x+2, y-1, x, y-1, 0.02)
            dust += tornado(x+1, y-2, x, y-1, 0.1)
            dust += tornado(x-1, y-2, x, y-1, 0.1)
            dust += tornado(x, y-3, x, y-1, 0.05)
            lst[x][y-1] -= dust
            if y-2 < 0:
                ans += lst[x][y-1]
            else:
                lst[x][y-2] += lst[x][y-1]

            lst[x][y-1] = 0
            y = y-1

        if x == 0 and y == -1:
            break
        for _ in range(cnt):  # 하
            dust = 0
            dust += tornado(x, y-1, x+1, y, 0.01)
            dust += tornado(x, y+1, x+1, y, 0.01)
            dust += tornado(x+1, y-1, x+1, y, 0.07)
            dust += tornado(x+1, y+1, x+1, y, 0.07)
            dust += tornado(x+1, y-2, x+1, y, 0.02)
            dust += tornado(x+1, y+2, x+1, y, 0.02)
            dust += tornado(x+2, y-1, x+1, y, 0.1)
            dust += tornado(x+2, y+1, x+1, y, 0.1)
            dust += tornado(x+3, y, x+1, y, 0.05)
            lst[x+1][y] -= dust
            if x+2 >= N:
                ans += lst[x+1][y]
            else:
                lst[x+2][y] += lst[x+1][y]
            lst[x+1][y] = 0
            x = x+1
    cnt += 1
print(ans)