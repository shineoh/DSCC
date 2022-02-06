#11653 #소인수분해

def is_prime_num(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input())
while True:
    x = 2
    if is_prime_num(n):
        print(n)
        break

    while True:
        if n % x == 0:
            n = n // x
            print(x)
            break
        else:
            x += 1
    