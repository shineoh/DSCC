#Q6 #1152 단어의 개수
# words = input().split()
# lst = list(words)
# print(len(lst))


#Q7 #2908 상수
a, b = input().split()
a_re = ''
b_re = ''

for i in range(len(a)):
    a_re+=a[len(a)-1-i]

for i in range(len(b)):
    b_re+=b[len(a)-1-i]

if a_re > b_re:
    print(a_re)
else:
    print(b_re)
