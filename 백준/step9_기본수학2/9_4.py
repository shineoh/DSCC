#1929 #소수 구하기

#시간초과
# from os import remove

# m,n = map(int, input().split())

# lst=list()
# for num in range(m, n+1):
#     lst.append(num)

# for i in range(2, int(n**0.5)+1):
#     for x in lst:
#         if x>i and x%i==0:
#             lst.remove(x)

# for ans in lst:
#     print(ans)


m,n = map(int, input().split())

lst= [True] * (n+1)
lst[0], lst[1] = False, False
for i in range(2, int(n**0.5)+1):
    for j in range(i+i, n+1, i):
        lst[j] = False
        
for ans in range(m,n+1):
    if lst[ans] ==True:
        print(ans)