#Q6 #8958 OX퀴즈
#n = int(input())
#ans = list()
#for i in range(n):
#    quiz = list(input())
#    total = 0
#    score = 0
#    for m in range(len(quiz)):
#        if quiz[m] == 'O':
#            score += 1
#            total += score
#        elif quiz[m] == 'X':
#            score = 0
#    # print(total) --> 그냥 바로 프린트 가능
#    ans.append(total)
#for i in range(n):
#    print(ans[i]) 

#Q7 #4344 평균은 넘겠지
n_case = int(input())
for i in range(n_case):
    q = list(map(int,input().split()))
    n_student = q[0]
    del q[0]
    win = 0
    avg_s = sum(q)/len(q)
    for t in range(n_student):
        if q[t] > avg_s:
            win += 1
    ans = (win/n_student)*100
    print(f'{ans:.3f}%')

        

        


