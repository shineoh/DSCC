# 정수를 문자열로 변환 풀이
# 2022-02-16

def itoa(n):
    j = '' # 문자열로 변환된 n을 담을 변수

    # n을 10으로 나누며 반복
    while 0<n:
        # 나머지를 활용해 뒤에서부터 변환
        j = chr(n % 10 + 48) + j # chr(48) -> ord('0')의 역
        n //= 10
    return j #변환된 값 반환

print(itoa(123)) # =>123(문자열)


# 역 -> 문자열을 정수로 변환
# def atoi(s):
#     i = 0
#     for x in s:
#         i = i*10 + ord(x)-ord('0')
#     return i
# print(atoi('123'))