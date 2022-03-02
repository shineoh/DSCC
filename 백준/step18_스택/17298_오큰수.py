# 백준 17298_오큰수
# 2022-03-22
import sys

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
stack = []
ans = [-1] * N

stack.append(0)
for i in range(1,N):
    while stack and lst[stack[-1]]<lst[i]:
        ans[stack.pop()] = lst[i]
    stack.append(i)

print(*ans)

