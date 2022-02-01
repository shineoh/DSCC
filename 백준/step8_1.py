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
