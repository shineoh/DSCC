#Q4 #3052 나머지
#x_lst = list()
#for i in range(10):
#    n = int(input())
#    x_lst.append(n%42)

#ans = set(x_lst)
#print(len(ans))

#Q5 #1546 평균
n = int(input())
s_lst=list(map(int, input().split()))
s_max = max(s_lst)
for i in range(n):
    s_lst[i] = s_lst[i]/s_max*100
s_avg = sum(s_lst)/n
print(s_avg)
