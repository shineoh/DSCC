# 땅 사기
# 2022-03-28

T = int(input())

def buy(i,j): # 땅 구매 함수
    cnt = 1 # 땅의 넓이 
    price = lst[i][j] # 땅의 가격
    stack = [(i, j)] # 땅 구매 -> 스택에 담기
    lst[i][j] = 0  # 구매한 땅 방문표시(0)
    
    while stack: # while stack 이용
        ci,cj = stack.pop() 
        for di, dj in dir: # 4방향 탐색하며
            ni = ci + di
            nj = cj + dj
            if 0<= ni<N and 0<= nj <N and lst[ni][nj]!=0: # 범위가 유효하고 구매가능한 땅일 경우
                stack.append((ni,nj)) # 땅 구매 -> 스택에 담기
                cnt += 1  # 넓이 갱신
                price += lst[ni][nj] # 가격 갱신
                lst[ni][nj] = 0 # 방문표시
    return cnt, price # 땅의 넓이, 가격 반환


for tc in range(1, T+1):
    N = int(input()) # 땅의 유효 범위
    lst = [list(map(int, input().split())) for _ in range(N)] # 인풋 리스트

    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 방향인덱스
    max_cnt = 0 # 땅의 최대넓이 담을 변수
    min_price = 500 # 땅의 가격(같은 크기일 경우 최소가격) 담을 변수
    for i in range(N): # 모든 땅을 순회하며
        for j in range(N):
            if lst[i][j] != 0: # 구매가능한 땅일 경우
                temp_cnt, temp_price = buy(i,j) # 땅 사기 -> 넓이, 가격 받기
                if max_cnt < temp_cnt: # 구매하는 땅의 최대 넓이 갱신(갱신될 경우 가격도 함께 갱신)
                    max_cnt = temp_cnt
                    min_price = temp_price
                elif max_cnt == temp_cnt: # 땅의 최대 넓이가 같을 경우 최소 가격 갱신
                    if min_price > temp_price:
                        min_price = temp_price
    # 답 출력
    print('#{} {} {}' .format(tc, max_cnt, min_price))
