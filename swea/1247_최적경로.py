#swea 1247 최적 경로
#2022-02-09

#거리계산
def find_optimalpath(index, x, y, distance):
    global min_cnt
    if min_cnt < distance: # 거리계산 중 최솟값 넘으면 바로 return
        return

    #모든경로 탐색이 완료되면 거리를 계산하여 최솟값 리턴
    if index == n_client:
        distance += abs(x - home_position[0]) + abs(y - home_position[1])
        if distance < min_cnt:
            min_cnt = distance
        return

    #경로를 하나씩 추가한다.
    for i in range(n_client):
        # 방문체크 후 재귀
        if check_lst[i]:
            check_lst[i] = False
            temp = distance + abs(x - position_lst[i][0]) + abs(y - position_lst[i][1])
            find_optimalpath(index+1, position_lst[i][0], position_lst[i][1], temp)
            #돌아오면 사용체크 해제
            check_lst[i] = True

T = int(input())
for tc in range(1, T+1):
    n_client = int(input()) # 고객의 수
    location_lst = list(map(int, input().split())) #위치리스트
    position_lst = []
    check_lst = [True]*n_client #방문여부 체크리스트
    min_cnt = 10000 #최솟값 count위한 변수

    company_position = []
    home_position = []

    #고객별 위치 넣기
    for i in range(0, len(location_lst), 2):
        position_lst.append([location_lst[i], location_lst[i+1]])
    company_position = position_lst.pop(0) #시작지점 ->회사위치
    home_position = position_lst.pop(0) #종료지점 ->집 위치
    
    #최적경로 탐색
    find_optimalpath(0, company_position[0], company_position[1], 0)
    print("#{} {}".format(tc, min_cnt))





