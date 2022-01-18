#D4

#Q1. 중간값 찾기 
numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24,
]
#정렬하기
for i in range(len(numbers)-1):
    for j in range(len(numbers)-1-i):
        if numbers[j] > numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
print(numbers)

#중간값 찾기
median = 0
idx =0
if len(numbers)%2 != 0:
    idx = len(numbers)//2+1
    median = numbers[idx-1]
else:
    idx = len(numbers)//2
    median = (numbers[idx-1]+numbers[idx])/2
print(median)

#Q2. 홀수만 담기
Nums = [n for n in range(1, 51)]
odds_list = Nums[::2]
print(odds_list)

#Q3. 평균 구하기
scores = [80, 89, 99, 83]
total = 0
for i in scores:
    total += i 
print(total/len(scores))