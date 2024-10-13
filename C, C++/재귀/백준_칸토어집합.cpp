#include <iostream>
#include <cmath>
using namespace std;

void cantor(int n) {
	int size = pow(3, n - 1); // size를 3의 n-1 제곱으로 초기화

	// N = 0 인 경우
    // base 케이스
	if (n == 0) {
		cout << "-";
		return;
	}

	// N번째 칸토어 집합 = N -1 번째 칸토어 집합을 2개 이은 것
	// 사이에 공백이 N - 1번째 칸토어 집합의 사이즈만큼 있어야 함
	cantor(n - 1);

	for (int i = 0; i < size; i++) {
		cout << " ";
	} // 공백 설정
	cantor(n - 1);

}

int main() {
	int N;
    // 유용한 cin 문법
    // cin이 정상적인지 확인 후 while 문 반복
	while (cin >> N) {
		cantor(N);
		cout << "\n";
	}

	return 0;
}