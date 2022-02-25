# boj 10773_제로 풀이
# 2022-02-25

K = int(input())
stack = []
for _ in range(K):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

ans = 0
for n in stack:
    ans += n

print(ans)
