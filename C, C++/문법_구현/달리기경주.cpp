#include <string>
#include <vector>
#include <iostream>
using namespace std;

/*
얀에서는 매년 달리기 경주가 열립니다. 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때, 해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다. 즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.

선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.

5 ≤ players의 길이 ≤ 50,000
players[i]는 i번째 선수의 이름을 의미합니다.
players의 원소들은 알파벳 소문자로만 이루어져 있습니다.
players에는 중복된 값이 들어가 있지 않습니다.
3 ≤ players[i]의 길이 ≤ 10
2 ≤ callings의 길이 ≤ 1,000,000
callings는 players의 원소들로만 이루어져 있습니다.
경주 진행중 1등인 선수의 이름은 불리지 않습니다.

*/

// 추월
// kai

vector<string> solution(vector<string> players, vector<string> callings) {
    vector<string> answer;
    int size = players.size();
    string temp;

    for (string call : callings){
        for (int i = 1; i < size; i++){
            if ( players[i] == call)
            {
                temp = players[i-1];
                players[i-1] = call;
                players[i] = temp;
            }  
        }
    } 
    answer = players;
    return answer;
}

vector<string> solution(vector<string> players, vector<string> callings) {
    for (string call : callings) {
        for (int i = 1; i < players.size(); i++) {
            if (players[i] == call) {
                swap(players[i - 1], players[i]);
            }
        }
    }
    return players;
}

#include <unordered_map>

using namespace std;

vector<string> solution(const vector<string>& players, const vector<string>& callings) {
    unordered_map<string, int> playerIndex;

    // 해시맵을 사용하여 각 플레이어의 인덱스를 초기화
    

int main() {
    vector<string> players = {"mumu", "soe", "poe", "kai", "mine"};
    vector<string> callings = {"kai", "kai", "mine", "mine"};

    for (string i : solution(players,callings)){
        cout << i << endl;
    }

    return 0;
}

