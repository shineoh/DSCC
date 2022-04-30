# 백준 듣보잡
# 2022-04-28

N,M = map(int,input().split())
lst1 = set()
lst2 = set()

for _ in range(N):
    lst1.add(input())
for _ in range(M):
    lst2.add(input())
# list(lst1 & lst2) -> lst1과 lst2에 둘다 들어있는 값
lst = sorted(list(lst1 & lst2))
print(len(lst))

for ans in lst:
    print(ans)