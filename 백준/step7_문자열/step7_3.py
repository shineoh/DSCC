#Q6 #1152 단어의 개수
# words = input().split()
# lst = list(words)
# print(len(lst))


#Q7 #2908 상수
# a, b = input().split()
# a_re = ''
# b_re = ''

# for i in range(len(a)):
#     a_re+=a[len(a)-1-i]

# for i in range(len(b)):
#     b_re+=b[len(a)-1-i]

# if a_re > b_re:
#     print(a_re)
# else:
#     print(b_re)

#Q8 #5622 다이얼
n = 0
word = input()
ans = 0
n_lst = [['A','B','C'], ['D','E','F'],['G','H','I'],['J','K','L'], ['M','N','O'], ['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
for w in word:
    for i in range(len(n_lst)):
        if w in n_lst[i]:
            ans += (i +3)
print(ans)
