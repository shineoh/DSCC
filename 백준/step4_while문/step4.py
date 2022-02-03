##4단계 while문
#Q1. #10952 A+B-5
while True:
    a,b = map(int,input().split())
    if a == 0 and b ==0:
        break
    print(a+b)

#Q2. #10951 A+B-4
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
        #print('error')

#Q3. #1110 더하기 사이클
n = int(input())
num = n
cnt =0

while True:
    a = num // 10 
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c

    cnt += 1
    if(num == n):
        break

print(cnt)
    
#Q3_1 문자열 풀이
n = input()
num = n
cnt = 0

while 1:
    if len(num) == 1:
        num = '0' + num
    plus = str(int(num[0]) + int(num[1]))
    num = num[-1] + plus[-1] # 맨 마지막 index의 수(문자) 받기
    cnt += 1
    if num ==n:
        print(cnt)
        break

