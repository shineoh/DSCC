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
T = int(input())
for i in range(T):
    R,S = input().split()
    ans = ''
    for S_w in S:
        ans += S_w * int(R)
    print(ans)
