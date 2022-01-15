#흐름제어, if, for 연습문제
#Q6_1 if 흐름제어
a=int(input())
for i in range(1,a+1):
   if not (a % i) :
          print("%d(은)는 %d의 약수입니다." % (i, a))

#Q6_2 모든 약수 표시, 2개일 경우 소수 표시
b=int(input())
count = 0
for i in range(1,b+1):
   if not (b % i) :
          print("%d(은)는 %d의 약수입니다." % (i, b))
          count += 1
if count == 2:
   print("%d(은)는 1과 %d로만 나눌 수 있는 소수입니다." % (b, b))

#Q6_3 대소문자 구분
a = input()
if 'a' <= a <= 'z':
   print("%s 는 소문자 입니다." % (a))
elif 'A' <= a <= 'Z' :
   print("%s 는 대문자 입니다." % (a)) 

#Q7_1 합불 결정
score = [88, 30, 61, 55, 95]
for i in range(0, 5):
   if score[i] >= 60:
      result = "합격"
   else:
      result = "불합격"
   print("%d번 학생은 %d점으로 %s입니다." % (i+1, score[i], result))

#Q7_2 1~100출력
for i in range(1,101):
    print(i)

#Q7_3 1~100 짝수 출력
for i in range(1,101):
    if not i & 1:
        print(i, end=" ")

