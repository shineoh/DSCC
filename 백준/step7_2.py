#3 #10809 알파벳 찾기
# word = input()
# s_lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u', 'v', 'w','x','y','z']
# for i in range(len(s_lst)):
#     n = word.find(s_lst[i])
#     s_lst[i] = n
# for s in s_lst:
#     print(s, end=' ')

##다른사람코드
# word = input()
# alphabet = list(range(97,123))  # 아스키코드 숫자 범위

# for x in alphabet :
#     print(word.find(chr(x)),end=' ') 

#4 #2675 문자열 반복
# T = int(input())
# for i in range(T):
#     R,S = input().split()
#     ans = ''
#     for S_w in S:
#         ans += S_w * int(R)
#     print(ans)

#5 $1157 단어공부
word = input().upper()
lst = list()
lst.extend(word.upper())
max = 0
ans = ''
for w in word:
    n = lst.count(w)
    if n > max:
        max = n
        ans = w
    if n == max:
        if w == ans:
            continue
        else:
            ans += w
if len(ans) == 1:
    print(ans)
else:
    print('?')

# 다른코드
word = input().upper()
lst = list(set(word))
cnt =list()

for w in lst:
    n = word.count(w)
    cnt.append(n)

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(lst[(cnt.index(max(cnt)))])