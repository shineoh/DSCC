#Q9. #2438 별찍기-1
n = int(input())
for i in range(1,n+1):
    print('*'*i)

#Q10. #2439 별찍기-2
n = int(input())
for i in range(1,n+1):
    print(' '*(n-i)+'*'*i)

#Q11. #10871 X보다 작은 수
n,x = map(int, input().split())
lst = list(map(int, input().split()))
for i in range(n):
    if lst[i] < x:
        print(lst[i], end=" ")
