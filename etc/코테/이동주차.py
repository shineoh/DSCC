# 이동주차 최소비용
# 각 차량이 알파벳으로 주어지고, 같은 알파벳끼리 연속되게 주차하기 위해 이동주차를 했을 때
# 이동칸수를 최소로하는 주차 횟수(비용)을 구하라
# 제한 :  10초, 2048MB

#input
# tc 1:
# 4
# DBBD
#
# tc 2:
# 5
# CDBDA
#
# tc 3:
# 7
# DAADCAC
#
# output
# 4
# 2
# 6

N = int(input())
lst = list(input())
si = 0
ans = 0
while True:
    temp = lst[si]
    flag = 0
    for i in range(si+1, N):
        if flag == 0 and temp != lst[i]:
            flag = 1
            flag_i = i
        elif flag == 1 and temp ==lst[i]:
            lst[flag_i], lst[i] =lst[i], lst[flag_i]
            ans += ((i-flag_i)*2)
            si = flag_i + 1
            break
    if flag == 1:
        si = flag_i
    else:
        break
print(ans)