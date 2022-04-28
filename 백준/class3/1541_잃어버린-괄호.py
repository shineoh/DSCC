# 괄호로 최솟값 만들기
# -기준으로 괄호치기
# 2022-04-28

f = input().split('-')
num = []
for i in f:
    cnt = 0
    x = i.split('+')
    for j in x:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)