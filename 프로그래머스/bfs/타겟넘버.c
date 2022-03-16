#include <string>
#include <vector>

using namespace std;

void dfs(vector<int>& numbers, int& answer, int target, int cnt=0, int sum=0){
    
    if(cnt==numbers.size()-1){
        if(sum+numbers[cnt] == target){
            answer++;
        }
        if(sum-numbers[cnt] == target){
            answer++;
        return;
        }
    }
    else{
    dfs(numbers, answer, target, cnt +1, sum + numbers[cnt]);
    dfs(numbers, answer, target, cnt +1, sum - numbers[cnt]);
    }
    
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    dfs(numbers, answer, target);

    return answer;
}