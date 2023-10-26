
#include <iostream>
#include <vector>

using namespace std;

int main() {
    // int N = 10; // 여기에 적절한 값을 넣어주세요
    // std::vector<std::vector<int>> line(N + 1, std::vector<int>());

    vector<int>a(10);
    // int형 a 변수명으로 원소10개 선언후 각 원소는 0으로 초기화

    vector<int>arr = {1,3,5,3,2};

    vector<vector<int>> v; // 2차원 백터 선언

    for(int i=0; i< arr.size();i++)
    {
      printf("%d",arr[i]);
    }


    cout << endl;
    
    // 범위 기반 for문

    for (int i:a){
      cout << i;
    }


    return 0;
}