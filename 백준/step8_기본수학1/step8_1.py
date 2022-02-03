#Q1 #1712 손익분기점

# fixed_cost, variable_cost, sales_price = map(int,input().split())

# def break_even_point():
#     cnt = 0
#     if variable_cost >= sales_price:
#         cnt = -1
#         return cnt
#     else:
#         cnt = (fixed_cost // (sales_price-variable_cost)) + 1
#     return cnt 

# print(break_even_point())

#Q2 #2292 벌집

n = int(input())
ans=1
while n>1:
    n=n-6*ans
    ans+=1
print(ans)

#q3 #1193 분수찾기
x = int(input())
num_list = []

num = 0
num_count = 0

while num_count < x:
    num += 1
    num_count += num

num_count -= num

if num % 2 == 0:
    i = x - num_count
    j = num - i + 1
else:
    i = num - (x - num_count) + 1
    j = x - num_count

print(f"{i}/{j}")