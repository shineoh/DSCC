// 프로그래머스_모의고사
// 2022-03-15

#include <string>
#include <vector>
using namespace std;

// 각 수험생의 찍기 방식 정의
int tester1[5] = {1,2,3,4,5};
int tester2[8] = {2,1,2,3,2,4,2,5};
int tester3[10] = {3,3,1,1,2,2,4,4,5,5};

// 최댓값 반환하는 함수 정의
int max(int a, int b){
    return a < b ? b : a;
}


vector<int> solution(vector<int> answers) {
    vector<int> answer;
    // 3명 수험생의 점수 담을 배열 정의
    vector<int> score(3);

    // 최댓값 담을 변수
    int maxScore = 0;
    
    // 각 문제의 답을 순회하며 해당 답과 수험생들의 답변이 일치하는지 확인
    for(int i=0; i < answers.size(); i++){
        // 각 배열을 반복하며 점수 plus
        if(tester1[i % 5] == answers[i]) score[0]++; 
        if(tester2[i % 8] == answers[i]) score[1]++;     
        if(tester3[i % 10] == answers[i]) score[2]++;
    }

    // max 함수 이용해서 최댓값 찾기
    maxScore = max(max(score[0],score[1]),score[2]);
    
    // 각 수험생의 점수를 확인하여 최댓값과 일치하면 답변에 추가
    for (int i=0; i<3; i++){
        if(score[i] == maxScore) answer.push_back(i+1);
    }
    
    // 답 반환
    return answer;
}