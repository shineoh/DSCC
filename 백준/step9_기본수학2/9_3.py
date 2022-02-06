#11653 #소인수분해

n = int(input())
x = 2
while n!=1:
    if n % x == 0:
        n = n // x
        print(x)
    else:
        x += 1
    