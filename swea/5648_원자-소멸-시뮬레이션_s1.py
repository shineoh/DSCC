# 1952_수영장 풀이
# 2022-03-25

import sys
sys.stdin = open('input.txt', 'r')

def move(lst, energy , cnt):
    if cnt >1000:
        return energy
    temp = [[(0, 0)] * 2002 for _ in range(2002)]
    for i in range(2000):
        for j in range(2000):
            if lst[i][j] != (0,0):
                di, dj = dir[lst[i][j][0]]
                # 1칸못가고 충돌할 때
                if lst[i+di][j+dj] != (0,0):
                    #방향확인
                    if lst[i][j][0] == 0 and lst[i+di][j+dj] == 1:
                        lst[i][j] = (0, 0)
                        lst[i + di][j + dj] = (0, 0)
                        energy += lst[i][j][1] + lst[i+di][j+dj][1]
                    elif lst[i][j][0] == 1 and lst[i+di][j+dj] == 0:
                        lst[i][j] = (0, 0)
                        lst[i + di][j + dj] = (0, 0)
                        energy += lst[i][j][1] + lst[i + di][j + dj][1]
                    elif lst[i][j][0] == 2 and lst[i+di][j+dj] == 3:
                        lst[i][j] = (0, 0)
                        lst[i + di][j + dj] = (0, 0)
                        energy += lst[i][j][1] + lst[i + di][j + dj][1]
                    elif lst[i][j][0] == 3 and lst[i+di][j+dj] == 2:
                        lst[i][j] = (0, 0)
                        lst[i + di][j + dj] = (0, 0)
                        energy += lst[i][j][1] + lst[i + di][j + dj][1]
                # 한칸가서 부딪힐때
                if temp[i+di][j+dj] != (0,0):
                    lst[i][j] = (0,0)
                    temp[i + di][j + dj] = (0,0)
                    energy += lst[i][j][1] + temp[i + di][j + dj][1]
                temp[i+di][j+dj] += lst[i][j]
    move(temp, energy, cnt+1)


T=int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [[(0,0)]*2002 for _ in range(2002)]
    dir= [(-1, 0), (1, 0), (0, -1), (0, 1)]
    energy = 0
    for _ in range(N):
        si,sj, d, k = map(int, input().split())
        lst[si+1000][sj+1000] = (d,k)

    ans = move(lst, 0, 0)
    print('#{} {}' .format(tc, ans))