#Q6 #10250 ACM호텔

t = int(input())

for i in range(t):
    r_h = 0
    r_w = 1
    h,w,n = map(int, input().split())
    for j in range(n):
        if r_h < h:
            r_h += 1
            
        else:
            r_h = 1
            r_w += 1
            
    if r_w<10:
        print(f'{r_h}0{r_w}')
    else:
        print(f'{r_h}{r_w}')
