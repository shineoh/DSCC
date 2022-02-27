# 2309_일곱난쟁이

lst = [int(input()) for _ in range(9)]
lst.sort() # 리스트 오름차순 정렬
sum_n = 0 # 난쟁이 키의 합
# 주어진 난쟁이들 키의 총합 구하기
for n in range(9):
    sum_n += lst[n]
# 마피아 2명
mafia1 = -1
mafia2 = -1
# 이중 포문을 통해
for i in range(8):
    for j in range(i+1, 9):
        # 두명을 제외한 키의 합이 100이 될 경우를 찾아서
        if sum_n - lst[i] - lst[j] == 100:
            mafia1 = i # 해당하는 난쟁이(마피아) 정보 저장
            mafia2 = j

# 찾아낸 마피아를 제외한 난쟁이들의 키를 출력
for k in range(9):
    if k == mafia1 or k == mafia2:
        continue
    print(lst[k])
