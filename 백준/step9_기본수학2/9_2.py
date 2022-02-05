#2581 # 소수

def is_prime_num(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

m = int(input())
n = int(input())
lst = []
for num in range(m, n+1):
    if is_prime_num(num):
        lst.append(num)

if lst == []:
    print(-1)

else:
    ans_1 = sum(lst)
    ans_2= 100
    for number in lst:
        if number < ans_2:
            ans_2 = number
    print(ans_1)
    print(ans_2)