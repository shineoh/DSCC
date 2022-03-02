# 백준 1874_스택-수열 풀이
# 2022-03-02

N = int(input())
cnt = 1
stack = []
ans = []
check = 1
for _ in range(N):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        ans.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        check = 0
if check == 0:
    print('NO')
else:
    for s in ans:
        print(s)