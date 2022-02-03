##5단계 배열
#Q1 #10818 최소, 최대
#n = int(input())
#nums = list(map(int, input().split()))
#max = nums[0]
#min = nums[0]
#for i in range(n):
#    if max < nums[i]:
#        max = nums[i]
#    elif min > nums[i]:
#        min = nums[i]
#
#print(min, max)
#    
##Q2 #2562 최댓값
#max = 0
#cnt = 0
#for i in range(1,10):
#    n = int(input())
#    if max < n:
#        max = n
#        cnt = i
#print(max)
#print(cnt)

#Q3 #2577 숫자의 개수
a = int(input())
b = int(input())
c = int(input())
x = str(a*b*c)
for i in range(10):
    cnt=0
    for s in x:
        if str(i) == s:
            cnt+=1
    print(cnt)

