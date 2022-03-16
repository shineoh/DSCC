#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int a = brown/2-1;
    int b = 3;
    for(int i=0; i< brown/2; i++){
        int na = a-i;
        int nb = b+i;
        if((na-2)*(nb-2)==yellow){
            if(na>nb){answer.push_back(na);
            answer.push_back(nb);}
            else{answer.push_back(nb);
            answer.push_back(na);}
            
            break;
        }

    }
    
    return answer;
}