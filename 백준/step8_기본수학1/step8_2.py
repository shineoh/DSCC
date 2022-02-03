#Q4 #2869 달팽이는 올라가고 싶다
# a,b,v = map(int, input().split())
# cnt = 0

# while True:
#     v-=a
#     cnt+=1
#     if v<=0:
#         print(cnt)
#         break
#     v+=b

#제한시간 걸려서 반복문 없이
a,b,v = map(int, input().split())
cnt = 0
if (v-b) % (a-b) == 0:
    cnt = (v-b) //(a-b)
else:
    cnt = (v-b) //(a-b) +1
print(cnt)