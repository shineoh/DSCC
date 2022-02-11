# Baby-Gin 풀이
# 2022-02-09

# 입력 받기
num = int(input())

# 카운트 리스트 생성 (while문에서 index 에러 방지를 위해 i+2)
cnt_lst = [0] * 12


while num > 0:
    cnt_lst[num%10] += 1
    num //= 10

# triplete, run 조사를 위한 변수 설정
i = 0
tri, run = 0, 0

# 0~9 까지 한자리 숫자 각각에서 조건 검사
while i < 10:
    # triplete일 경우 카운터 리스트의 데이터 삭제, tri 횟수 추가
    if cnt_lst[i] >= 3: #같은 숫자가 3개면 triplete
        cnt_lst[i] -= 3
        tri += 1
        continue
    # run일 경우 카운터리스트의 데이터 삭제, run 횟수 추가
    if cnt_lst[i] >= 1 and cnt_lst[i+1] >= 1 and cnt_lst[i+2] >= 1: #숫자 3개가 연속죄면 run
        cnt_lst[i] -= 1
        cnt_lst[i+1] -= 1
        run += 1
        continue
    i += 1


# 출력 --> tri와 run을 합쳐 2가 나오면 Baby Gin
if run + tri == 2:
    print("Baby Gin")
else:
    print("Lose")



