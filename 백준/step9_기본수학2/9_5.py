#4948 #베트르랑 공준

def PrimeNum_Eratos(N):
    nums = [True]*(N)
    for i in range(2, int(N**0.5)+1):
        if nums[i] == True:
            for j in range(i+i, N, i):
                nums[j] =False
    return [i for i in range(2,N) if nums[i] == True]

while True:
    N = int(input())

    if N == 0:
        break
    lst_prime = PrimeNum_Eratos(2*N + 1)
    ans = [num for num in lst_prime if num > N]
    print(len(ans))






##시간초과
# while True:
#     n = int(input())
#     if n==0:
#         break
#     cnt = 0
#     for i in range(n+1, (2*n)+1) :
#         if i == 2:
#             cnt+=1

#         else:
#             for j in range(2, int(((2*n)**0.5))+1):
#                 if i % j == 0:
#                     break
#             else:
#                 cnt+=1
#     print(cnt)




