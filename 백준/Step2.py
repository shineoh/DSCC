#Q1. #1330번 두 수 비교하기
# A,B = map(int, input().split())
# if -10000 <= A <=10000 and -10000 <= B <= 10000:
#     if A > B:
#         print('>')
#     elif A < B:
#         print('<')
#     elif A==B:
#         print('==')

#Q2. #9498 시험성적
# score = int(input())
# if 90<= score <= 100:
#     print('A')
# elif 80 <= score:
#     print('B')
# elif 70 <= score:
#     print('C')
# elif 60 <= score:
#     print('D')   
# else:
#     print('F')

#Q3. #2753 윤년
# year = int(input())
# if year % 400 == 0:
#     print('1')
# elif year % 4 ==0 :
#     if year % 100 != 0:
#         print('1')
#     else:
#        print('0') 
# else:
#     print('0')

#Q4. #14681 사분면 고르기
x = int(input())
y = int(input())
if x>0:
    if y>0:
        print('1')
    elif y<0:
        print('4')
elif x<0:
    if y>0:
        print('2')
    elif y<0:
        print('3')