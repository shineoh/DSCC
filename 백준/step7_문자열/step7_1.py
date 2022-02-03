##7단계
#Q1. #11654 아스키코드
# alpha = input()
# ans= ord(alpha)
# print(ans)

#Q2. #11720 숫자의 합
n = int(input())
sum = 0
nums = []
nums.extend(input())
for i in range(n):
    sum += int(nums[i])
print(sum)

# sum이용
# n = input()
# print(sum(map(int,input())))
# for문 이용
# n = input()
# nums = input()
# total = 0
# for i in nums :
#     total += int(i)  # total= total+int(i)
# print(total)

