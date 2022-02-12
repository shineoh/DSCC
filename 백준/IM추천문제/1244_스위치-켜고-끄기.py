# boj_1244_스위치-켜고-끄기 풀이
# 2022-02-12

# 스위치 변경함수
def switching(i):
    if lst_switch[i-1] == 0:
        lst_switch[i-1] = 1
    else:
        lst_switch[i-1] = 0
    return

# 스위치 수, 스위치 상태(리스트로), 학생 수 입력받기
num_switch = int(input())
lst_switch = list(map(int, input().split()))
num_student = int(input())

# 학생 수만큼 반복
for _ in range(num_student):
    # 성별, 제시 숫자 받기 
    s, n = map(int, input().split())
    # 남학생일 경우
    if s == 1:
        # 배수에 해당하는 수 스위칭
        for i in range(n, num_switch+1, n):
            switching(i)

    # 여학생일 경우
    if s == 2:
        # 제시 받은 수 스위칭
        switching(n) 
        
        # j를 하나씩 늘리며 앞 뒤 비교
        j = 1
        while 1<=n-j and n+j<=num_switch:
            # n-j와 n+j의 상태가 같으면 스위칭
            if lst_switch[n-1-j]==lst_switch[n-1+j]:
                switching(n-j)
                switching(n+j)
                j+=1
            else:
                break

# 출력(20줄 넘으면 끊기게)
for ans in range(num_switch):
    print(lst_switch[ans], end=' ')
    if (ans+1) % 20 == 0 :
        print()
    
