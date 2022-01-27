#3 #10809 알파벳 찾기
word = input()
s_lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']
for i in range(len(s_lst)):
    n = word.find(s_lst[i])
    s_lst[i] = n
for s in s_lst:
    print(s, end=' ')

