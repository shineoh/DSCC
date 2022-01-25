# step6
# Q1 # 15596 정수 N개의 합
# def solve(a):
#     ans = 0
#     for x in a:
#         ans += x
#     return ans

# Q2 #4673 셀프넘버
def notselfnum(x):
    lst = list()
    lst.extend(str(x))
    total = x
    for y in lst:
        total += int(y)
    return total

numbers = list(range(1,10001))
for i in range(1, 10001):
    if notselfnum(i) in numbers:
        numbers.remove(notselfnum(i))
for j in numbers:
    print(j)

## 다른 풀이 - set 사용
# natural_num = set(range(1, 10001))
# generated_num = set()

# for i in range(1, 10001):
#     for j in str(i):
#         i += int(j)
#     generated_num.add(i)

# self_num = sorted(natural_num - generated_num)
# for i in self_num:
#     print(i)

# Q3 #1065 한수
def hansu(x):
    lst = list()
    lst.extend(str(x))
    total = x
    for y in lst:
        total += int(y)
    return total