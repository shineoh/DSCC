# 1206_View 풀이
# 2022-02-09

T =10 #주어진 케이스 수

for tc in range(1, T+1):
    n = int(input()) #가로 길이(땅 길이) 받기
    lst = list(map(int, input().split())) #리스트로 케이스 받기(맨 앞, 맨 뒤 두칸은 건물 없는 땅)
    ans = 0 #답 넣을 변수

    # 빈 땅을 제외한 전체 구간에서 반복문 시행
    for i in range(2, n):
        view_l = 0 #좌측 조망권
        view_r = 0 #우측 조망권

        # 좌측 2칸에 대한 조망권이 확보되면 시행 --> 좌측 2칸 중 더 낮은 값을 조망권에 할당
        if lst[i-1] < lst[i] and lst[i-2] < lst[i]:
            if lst[i-1] > lst[i-2]:
                view_l = lst[i] - lst[i-1]
            else:
                view_l = lst[i] - lst[i-2]

            # 우측 2칸에 대한 조망권 확보 --> 우측 2칸 중 더 낮은 값을 조망권에 할당
            if lst[i+1] < lst[i] and lst[i+2] < lst[i]:
                if lst[i+1] > lst[i+2]:
                    view_r = lst[i] - lst[i+1]
                else:
                    view_r = lst[i] - lst[i+2]

        # 좌측 조망권과 우측 조망권 중 더 낮은 값을 ans에 추가
        if view_r < view_l:
            ans += view_r
        else:
            ans += view_l

    # 답 출력
    print('#{} {}' .format(tc, ans))