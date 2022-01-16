#함수 연습문제
#Q8.1 회문
def palindrome(a_str):
    answer = ""
    for i in range(len(a_str)-1, -1, -1):
        answer += a_str[i]
    return answer
 
b = input()
check_str = palindrome(b)
print(check_str)
if b == check_str: 
    print("입력하신 단어는 회문(Palindrome)입니다.")
else:
    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")

#Q8.2 가위바위보게임
lis = ["가위", "바위", "보"]
def Game(a , b):
   if (a == b):
      print("비겼습니다!")
   elif (a == lis[0] and b == lis[1]) or (b == lis[0] and a == lis[1]):
      print("바위가 이겼습니다!")
   elif (a == lis[0] and b == lis[2]) or (b == lis[0] and a == lis[2]):
      print("가위가 이겼습니다!")
   elif (a == lis[1] and b == lis[2]) or (b == lis[1] and a == lis[2]):
      print("보가 이겼습니다!")
   
p1, p2 = input(), input()
t1, t2 = input(), input()
Game(t1, t2)

#Q8.3 소수확인
def CheckPrimenum(k):
    count = 0
    for i in range(1,k+1):
        if not (k % i) :
            count += 1
    if count == 2:
        return True
    elif count != 2:
        return False

a=int(input())
if CheckPrimenum(a):
    print("소수입니다.")
else:
    print("소수가 아닙니다.")
