#백준 1단계
#10172. 개출력
print("|\\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\\__|")

#1000, A+B
a, b = map(int, input().split())
print(a+b)

#1001, A-B
a, b = map(int, input().split())
print(a-b)

#10998, A*B
a, b = map(int, input().split())
print(a*b)

#1008, A/B
a, b = map(int, input().split())
print(a/b)

#10869, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력
a, b = map(int, input().split())
print("{}\n{}\n{}\n{}\n{}".format(a+b, a-b, a*b, int(a/b), a%b))

#10430, (A+B)%C, ((A%C) + (B%C))%C, (A×B)%C, ((A%C) × (B%C))%C를 출력
a, b, c = map(int, input().split())
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

#2588, 곱셈과정보여주기
a = int(input())
b = input()
print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))
