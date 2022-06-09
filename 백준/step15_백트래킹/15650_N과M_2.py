# 2022-06-05

N,M = list(map(int,input().split()))
 
lst = []
 
def dfs(x):
    if len(lst)==M:
        print(' '.join(map(str,lst)))
        return
    
    for i in range(x,N+1):
        if i not in lst:
            lst.append(i)
            dfs(i+1)
            lst.pop()
 
dfs(1)
 