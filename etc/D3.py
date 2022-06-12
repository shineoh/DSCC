#내장함수 연습문제
#Q1. datetime
import datetime
name = input()
age = int(input())
t = 100-int(age)
#출력이 2099년에 100세 -> 2019년 기준이므로 -3
year = datetime.datetime.now().year-3 +t
print("%s(은)는 %d년에 100세가 될 것입니다." % (name, year))

#Q2. map함수와 람다식
t_str = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
str_list = list(t_str)
t = list(map(lambda c : ord('E') - ord(c) , str_list))
print(sum(t))

#Q3. 에러 예외처리
def multiplication(*param):
   result = 1
   for i in param:
      if type(i) != int:
         print("에러발생")
         return
      result *= i
   print(result)
      
multiplication(1, 2, '4', 3)