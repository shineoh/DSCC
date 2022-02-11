# 4153_직각삼각형 풀이
# 2022-02-11


while True:
    lst=[0]*3
    lst[0], lst[1], lst[2] = (map(int, input().split()))
    if lst == [0, 0, 0]:
        break
    max_num = 0
    for i in range(3):
        if lst[i] > max_num:
            max_num = lst[i]
    lst.remove(max_num)
    if max_num**2 == lst[0]**2 + lst[1]**2:
        print('right')
    else:
        print('wrong')
