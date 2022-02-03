##3단계
#Q1. #2739 구구단
# N = int(input())
# for i in range(1,10):
#     print(f'{N} * {i} = {N*i}')

# #Q2. #10950 A+B-3
# t = int(input())
# for i in range(t):
#     a,b = map(int,input().split())
#     print(a+b)

#Q3. #8393 합
N = int(input())
total = 0
for i in range(1,N+1):
    total += i
print(total)

#Q4. #15552번 빠른 A+B
# import sys
 
# inp = int(input())
# for i in range(inp):
#         a,b = map(int, sys.stdin.readline().split())
#         print(a+b)
