#1085 # 직사각형에서 탈출

x, y, w, h = map(int, input().split())

lst=[x,y]
if x<w:
    lst.append(w-x)
if y<h:
    lst.append(h-y)

ans = min(lst)

print(ans)
