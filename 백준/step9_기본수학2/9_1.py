#1978 #소수찾기

def is_prime_num(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False # i로 나누어 떨어지면 소수가 아니므로 False 리턴   
    return True # False가 리턴되지 않고 for문을 빠져나왔다면 소수이므로 True 리턴

t = int(input())
lst = []
lst.extend(map(int, input().split()))
cnt = 0
for x in lst:
    if is_prime_num(x):
        cnt+=1
print(cnt)
