#3009 #네 번째 점

x_lst = []
y_lst = []
for i in range(3):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)

if x_lst[0] == x_lst[1]:
    ans_x = x_lst[2]
elif x_lst[1] == x_lst[2]:
    ans_x = x_lst[0]
elif x_lst[0] == x_lst[2]:
    ans_x = x_lst[1]


if y_lst[0] == y_lst[1]:
    ans_y = y_lst[2]
elif y_lst[1] == y_lst[2]:
    ans_y = y_lst[0]
elif y_lst[0] == y_lst[2]:
    ans_y = y_lst[1]

print(f'{ans_x} {ans_y}')


## 코드 줄이기 with Jay

for i in range(3):
    x_lst.append(x_lst[i])
    y_lst.append(y_lst[i])
    if x_lst[i] == x_lst[i+1]:
        ans_x = x_lst[i+2]
    if y_lst[i] == y_lst[i+1]:
        ans_y = y_lst[i+2]