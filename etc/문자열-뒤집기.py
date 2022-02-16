# 문자열 뒤집기 풀이
# 2022-02-16

# 슬라이싱 이용
word = 'reverse this strings'
word = word[::-1]
print(word)

# for문 이용
word = 'reverse this strings'
word_print = '' # 뒤집은 문자열을 담을 변수
for w in range(len(word)-1,-1,-1): # 문자열의 뒤부터 하나씩
    word_print += word[w]          # 새 문자열에 추가
print(word_print)