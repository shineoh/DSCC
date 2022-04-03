import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    ans = 0 # 답 담을 변수
    for i in range(N):
        for j in range(N):
            if j+M-1 < N: # 인덱스가 유효하면
                scv1 = [] # 일꾼 1이 채취할 벌통 리스트 만들기
                for k in range(M): # 벌통 추가해주기
                    scv1.append(lst[i][j+k])

                for ii in range(i, N): # 가지치기 -> 일꾼 1 라인부터 탐색
                    for jj in range(N):
                        if ii == i and jj <= j+M-1 : # 겹침 방지
                            continue
                        elif jj + M-1 < N: # 인덱스가 유효하면
                            scv2=[] # 일꾼 2가 채취할 벌통 리스트 만들기
                            for kk in range(M): # 벌통추가
                                scv2.append(lst[ii][jj + kk])
                            scv1.sort(reverse=True) # 내림차순 정렬
                            scv2.sort(reverse=True) # 내림차순 정렬
                            temp = 0 # 부분합 담을 변수
                            c11 = c12 = c21 = c22 = 0 # 채취할 벌통
                            r11 = r12 = r21 = r22 = 0 # 채취한 벌꿀
                            for l in range(M):
                                if c11 + scv1[l] <= C: # 채취 제한 범위 안이면
                                    c11 += scv1[l] # 벌꿀 채취량 카운트
                                    r11 += scv1[l]**2 # 꿀 이익 카운트
                                # 나머지에 대해서 반복
                                if c12 + scv1[M-1-l] <= C:
                                    c12 += scv1[M-1-l]
                                    r12 += scv1[M-1-l]**2
                                if c21 + scv2[l] <= C:
                                    c21 += scv2[l]
                                    r21 += scv2[l]**2
                                if c22 + scv2[M-1-l] <= C:
                                    c22 += scv2[M-1-l]
                                    r22 += scv2[M-1-l] ** 2
                            temp = max(r11, r12) + max(r21, r22) #
                            if ans < temp: # 최대값 갱신
                                ans = temp
    # 답출력
    print('#{} {}' .format(tc, ans))