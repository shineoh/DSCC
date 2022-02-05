#1011 #Fly me to the mmon

t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    cnt = 0
    d = y-x
    n=1
    while d>n:
        d -= (2*n)
        n += 1
        cnt += 2
    if 0<d<=n:
        cnt+=1
    print(cnt)
        