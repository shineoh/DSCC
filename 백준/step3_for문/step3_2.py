##3단계
#Q5. #2741 N찍기
#N = int(input())
#for i in range(1,N+1):
#    print(i)

#Q6. #2742 기찍N
N = int(input())
for i in range(N,0,-1):
    print(i)

#Q7. #11021 A+B-7
N = int(input())
for i in range(1,N+1):
    a,b = map(int, input().split())
    print(f'Case #{i}: {a+b}')

#Q8. #11022 A+B-8
N = int(input())
for i in range(1,N+1):
    a,b = map(int, input().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')

