# 고지식한 패턴 검색풀이
# 2022-02-16

str_find = 'is'  # 찾을 패턴
str_gived = 'This is a book~!'  # 제시 텍스트
i = 0 # str_find의 인덱스
j = 0 # str_gived의 인덱스

# 텍스트의 길이 내에서 반복문을 돌며
while j < len(str_find) and i < len(str_gived):
    if str_gived[i] != str_find[j]: # 찾을 패턴이 없을 경우
        i -= j  # i는 j만큼 앞으로 돌리고
        j = -1  # j는 -1로 초기화 (다음 요소를 패턴의 첫글자와 비교하기 위해)
    i += 1
    j += 1

# 일치하는 요소의 길이가 패턴의 길이와 같으면
if j == len(str_find):
    print(i-len(str_find)) # 찾은 위치 값(i-패턴길이) 출력
else: # 검색 실패 시
    print('텍스트 내에 패턴이 없습니다')


