# 4831_전기버스
# 2022-02-10

import sys
sys.stdin = open('input.txt', 'r')

# 주행을 수행하는 함수 정의(인자 : 현재위치, 목적지, 주행가능거리)
def drive(cur_stop, destination, possible_distance):
    cnt = 0 # 충전횟수 카운트를 위한 변수 설정
    while True:
        check = 0 # 목적지를 찾았는지 여부를 확인하는 변수

        # 주행가능 범위내에 목적지가 있으면 카운트 return
        if cur_stop + possible_distance >= destination:
            return cnt

        # 최대 주행가능 거리에서부터 현재위치 앞까지 탐색하며 범위 내에 충전소 있는지 확인
        for k in range(possible_distance, 0, -1):
            # 범위 안에 충전소가 있으면 이동 후 break
            if bus_stop_lst[cur_stop + k] == True:
                cur_stop += k  # 이동 후 위치
                cnt += 1       # 카운트 +1
                check = 1      # 충전소 찾았는지 여부에 체크(=1)
                break

        # 주행가능범위 내에 충전소를 못찾았으면 0 return
        if check == 0:
            return 0


T = int(input())
for tc in range(1, T + 1):
    # K = 한번에 이동할 수 있는 정류장 수
    # N = 종점 -> 총 정류장 수 = N+1
    # M = 충전기가 설치된 정류장 번호
    K, N, M = map(int, input().split())

    # 정류장 리스트 생성
    bus_stop_lst = [False] * (N + 1)
    # 제시되는 충전소 목록 리스트에 담기
    charge_lst = list(map(int, input().split()))

    # 충전소가 있는 정류장 True로 표시
    for charge in charge_lst:
        bus_stop_lst[charge] = True

    start = 0 # 현재 위치 시작 지점(0)으로 초기화

    # drive 함수 시행 후 return 값 ans에 담기
    ans = drive(start, N, K)

    #답 출력
    print('#{} {}'.format(tc, ans))
